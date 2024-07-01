from PIL import Image
import os
import re
from ..services.logger import logger

""" 
This function helps in sorting the images in alphanumeric order.
"""
def natural_sort_key(string):
    return [int(s) if s.isdigit() else s for s in re.split(r'(\d+)', string)]

""" 
This function generates the final image output by combining all the question and answer images.
"""
def generate_image_output(folder):
    try:
        logger(f"Filtering and sorting images")
        # Get all images in the folder
        all_images = [os.path.join(folder, file_name) for file_name in os.listdir(folder)]

        if not all_images:
            logger(f"No images found in the output folder")
            return

        # Filter out non-image files, categorize questions and answers, and sort them in alphanumeric order
        all_questions = sorted([image for image in all_images if image.endswith(".png") and image.startswith(os.path.join(folder, "question_"))], key = natural_sort_key)
        all_answers = sorted([image for image in all_images if image.endswith(".png") and image.startswith(os.path.join(folder, "answer_"))], key = natural_sort_key)

        # logger(f"{all_questions}")
        # logger(f"{all_answers}")

        logger(f"Creating canvas for final image")
        # Calculate the maximum width and total height needed for the combined image
        max_width = 0
        total_height = 0
        for image_path in all_questions + all_answers:
            temp_image = Image.open(image_path)
            width, height = temp_image.size
            max_width = max(max_width, width)
            total_height += height

        # Create a blank image with the calculated maximum width and total height
        combined_image = Image.new("RGB", (max_width, total_height), color = "white")

        logger(f"Pasting images to canvas")
        # Paste all question images one below the other
        y_offset = 0
        for question_image_path in all_questions:
            question_image = Image.open(question_image_path)
            combined_image.paste(question_image, (0, y_offset))
            y_offset += question_image.size[1]  # Increment y_offset by height of current image

        # Paste all answer images one below the other
        for answer_image_path in all_answers:
            answer_image = Image.open(answer_image_path)
            combined_image.paste(answer_image, (0, y_offset))
            y_offset += answer_image.size[1]  # Increment y_offset by height of current image

        logger(f"Saving the final image")
        # Save the combined image
        combined_image.save(os.path.join(folder, "final_image_output.jpeg"), format = "JPEG")

    except Exception as exception:
        logger(f"An error occured while creating the image output - {exception}")
