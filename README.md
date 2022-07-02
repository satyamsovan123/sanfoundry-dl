# sanfoundry-dl

This small python app helps to extract all of the multiple choice questions found on "www.sanfoundry.com". This version is better than the first version (v1) in many ways.
<em>sanfoundry-dl v2 is all new and a feature-pack release. This version now supports standalone URLs as well! It's faster and less error prone (upto 40%). This version also uses a "real" user interface (web) instead of boring terminal/console/shell/command_prompt! For this version, the error handling is improved drastically when compared to the previous version. And, now for the bonus part, you can use it as an API, if you so wish!</em>

To use this app, you must have python3+, Google Chrome installed on your computer, and ofcourse a clone of this repository (in your desktop).
Open your terminal/console/shell/command_prompt and change directory to the project's cloned folder and install all requirements using this command: <b>pip install -r requirements.txt</b>

~~As, this project now uses selenium, so you might need to add ChromeDriver to this location: <b>/Desktop/sanfoundry-dl/api/main/helpers/drivers/chromedriver</b>.
Here is the link to download ChromeDriver: <a href="https://chromedriver.chromium.org/downloads">https://chromedriver.chromium.org/downloads</a>. Also, it's important that you must download the same version of ChromeDriver as your Google Chrome browser.
So, for example, if you are using Windows PC and you have cloned the project to your desktop, you need to copy chromedriver_with_same_version_as_chrome_for_windows.exe to this folder path "Desktop/sanfoundry-dl/api/main/helpers/drivers/"~~ <b>P.S. This part is not required anymore. Now it's all automatic.</b>

And, the last step is to run this in your terminal/console/shell/command_prompt: <b>python3 main.py</b> or <b>python main.py</b>. Now you can access the app using a "real" user interface (web). To do that open any browser and go to <a href="[https://chromedriver.chromium.org/downloads](http://127.0.0.1:5000/scrap)">http://127.0.0.1:5000/scrap</a> and enter a valid URL. It will take some time and it will download the PDF file. Alternatively, you can either keep checking the output folder for any changes and see your final file there, or you can check your terminal/console/shell/command_prompt for any progress. It might take sometime (even much longer) or you might encounter some bug here and there. Just say hi to them (Just kidding!). So, try again and keep checking the output folder.

Thanks for checking this project. Feel free to contribute and contact for anything.
