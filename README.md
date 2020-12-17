# CovidDownloader
This repository contains the algorithms used to save Covid's reports and store them in a Database.  
The reports are downloaded from the repo:  
"https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports"  
To test it, you can download the "XAMPP" program to create a local db! XAMPP link: https://www.apachefriends.org/it/index.html  
Covid's reports must be save in the directory 'COVID-19-REPORTS'

Programs:
1) CVbuildDataDB -> Creates the DB with all the csv files data of the COVID's reports downloaded;
2) CVcheckfiles ->  
	a) If the params is 'begin' downloads all the report files from the repo from 22/01/20 and save them in the 'COVID-19-REPORTS' folder  
	b) If the params is 'uptodate' downloads the today's and yesterday's report files and save them in the 'COVID-19-REPORTS' folder  
3) CVuptodateDB -> Updates the db with the today's and yesterday's report files (downloading them if not downloaded yet!);
4) CVmenu -> Use this to have a menu to select the actions to do.

How to use:
1) Copy the repo
2) Create virtualenv -> "virtualenv my_project"
3) Activate virtualenv -> source my_project/bin/activate
4) Download requirements -> pip install -r requirements.txt
5) Use the CVmenu to select what you want to do -> python3 CVmenu.py

ATTENTION: To use the db in local   
1) Install XAMPP and active it
2) Create the db "COVID"
3) Create the table "DATA"  
![Alt text](/Images/TableConfig.png?raw=true "Optional Title")


Please cite the repo if you want to use these in your programs -> https://github.com/ImBadnick/CovidDownloader







