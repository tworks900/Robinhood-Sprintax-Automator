# Robinhood-Sprintax-Automator 2024

From one International to another! Robinhood 1099-B -> Sprintax Tax Filing. Automates the tedious task of typing in individual trades that you have done in a year into individual 1099-B pages on the Sprintax Page.  

## Release Notes : 
- Added Wash-sale entry 
- Added date formatting for Buy and Sale of stocks & options
- Added feature to estimate the number of of 1099-B forms needed - trades()
- Now its possible to import Robinhood’s exported .csv directly without changing the column titles
- Added “click” on the question for trading property at the bottom of 1099-B page in Sprintax
- Added function to automatically download ChromeDriver for Selenium
- Updated find Xpath function for updated python Selenium Libraries
- Added both Short-term and Long-term stock entry.
- Added clear() to all fields before adding data.
- Added ability to add losses:  Sprintax advices adding losses as cost basis because the "Proceeds Field" on the website cannot be a negative number.

## Important Notes: 
- Save your trades from Robinhood as trades_robinhood.csv
- Crypto entry function is non-functional. (Will add it shortly, can’t promise though)

## How to use this script : 
- Download and install Google Chrome 
- Download your trades from Robinhood as a .csv 
- Save .csv in the same directory as this main.py file. 
- Note : You do not need to download ChromeDriver for Selenium. The program takes care of automatically downloading the driver
- In main.py , adjust details for your brokerage if it is different from RobinHood. Also change the xpath for your state (Currently set to MA, Check "State Option Code_Robinhood.xlsx" to see what’s your state code)
- Run main.py in interactive mode with the -i flag.
- Run trades() to get the number of 1099-B forms need. This function gives the number of trades in the .csv file 
- Run openChrome() in the terminal in the interactive Python shell. This will open the window and navigate to Sprintax's login.
- Complete reCaptcha, log in, and navigate to the 1099B page.
- Close any pop ups for cookies or other information in the 1099-B page. This is important because the “click” function cannot click on the fields and buttons if there are popups blocking it. An example is the “share cookies” prompt at the bottom of the page after login into  Sprintax. 
- Run loop(start, end, cryp=False). Example loop(1,50,False) adds the first 50 entries from the .csv.
-Sit back as the program completes each entry in time.sleep(5) seconds. Feel free to increase or decrease the time. (Any change on the code needs you to restart the program and enter interactive mode)
- Feel free to play around with individual functions especially runTrade(index, False) which helps to add individual entries.  
-  For debugging and testing, you can also run setupInfo(),setupTrade(),runInfo(cryp), and runTrade(index) individually.


## Python Lib. Requirements : 
You don’t need all of them. This is a list of what's on my side.

attrs             23.2.0
certifi           2024.2.2
h11               0.14.0
idna              3.6
numpy             1.26.4
outcome           1.3.0.post0
pandas            2.2.1
pip               24.0
PySocks           1.7.1
python-dateutil   2.8.2
pytz              2021.1
selenium          4.18.1
setuptools        65.5.1
six               1.16.0
sniffio           1.3.0
sortedcontainers  2.4.0
trio              0.24.0
trio-websocket    0.11.1
typing_extensions 4.9.0
tzdata            2024.1
urllib3           1.26.4
wheel             0.38.4
wsproto           1.2.0

Credits to humblef00ls for the initial code