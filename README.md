# sanfoundry-dl
This script helps to extract all of the multiple choice questions found on "www.sanfoundry.com". 
All question from hyperlinks found inside the URL provided is stored as "result.txt" inside txt-sites folder. 
I've created this small python3 script that would help users on sanfoundry.com to extract all the MCQs. 
My original approach was to convert this txt file to pdf, but wasn't able to get around. I'm still trying and upon any success, i would upload it for sure. 
Some caveats are :  
  1. This script only captures pages from "sanfoudry.com" of format https://www.sanfoundry.com/1000-some-topics-questions-answers/
  Examples are : https://www.sanfoundry.com/1000-electric-drives-questions-answers/ 
                 https://www.sanfoundry.com/1000-data-structures-algorithms-ii-questions-answers/ 
                 https://www.sanfoundry.com/1000-statistical-quality-control-questions-answers/ 
  2. This script has few bugs, for dearth of my knowledge in "Web-Developement".
  3. Any suggestions are welcome. I would love to know my mistakes. Feel free to fork, edit and branch.
  4. I'll be updating it for sure later, because i've too many things on my plate right now.
  5. Pardon me for my horrible sense of humor (in code / output). 

To use it you need to satisfy following requirements :  
python3+, 
pip3 install requests, 
pip3 install glob, 
pip3 install ssl, 
pip3 install beautifulsoup4  

To run it :  
Just download the folder into your "Desktop" only (or you might want to resolve the realtive paths, though i've tried to keep it minimal). 
Hit up your terminal / console and cd into your "Desktop". Please don't change the contents of the folders and file, unless you can fix the error that follows it. 
Then run "python3 main.py the-sanfoundry-url-having-1000-in-it-goes-here". 

Thanks for checking this out. Have a great day ! 
            
