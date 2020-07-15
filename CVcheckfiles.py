import csv
import datetime
from datetime import timedelta, date
import pandas as pd
import urllib
import os

pd.set_option('display.max_columns', 5)
pd.set_option('display.max_rows',206)

def downloadCVfiles(whichdate):
    print("Checking directory: ",end='')
    try : 
        os.makedirs('COVID-19-REPORTS/')
        print("Directory created with success.")
    except FileExistsError: print("Directory already exists")
    
    if (whichdate == "uptodate"):
        x = (datetime.datetime.now()).strftime("%x")
        y = (datetime.datetime.now()-timedelta(days=1)).strftime("%x")
        x=x.replace("/","-")
        x=x.replace("20","2020")
        x=x+'.csv'
        y=y.replace("/","-")
        y=y.replace("20","2020")
        y=y+'.csv'

        #Takes the yerstday's file from github and creates a copy
        try:
            print("Checking yesterday's file: ",end='')
            url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/' + y
            df = pd.read_csv(url) #Reading the .csv file from the url
            try:
                #Coping datas from the .csv file in a new .csv file in the "COVID-19-REPORTS" directory
                open('COVID-19-REPORTS/'+y,"x")
                newf=open('COVID-19-REPORTS/'+ y,"w")
                df.to_csv(newf)
                newf.close()
                print("Yesterday's file added with success in the directory")
            except FileExistsError:
                print("Yesterday's file already exists in the directory")
        except urllib.error.HTTPError:
            print("Yesterday's file not found in CV stats files, needs to wait")
            y="not found"

        #Takes the today's file from github and creates a copy
        try:
            print("Checking today's file: ",end='')
            url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/' + x
            df = pd.read_csv(url) #Reading the .csv file from the url
            try:
                #Coping datas from the .csv file in a new .csv file in the "COVID-19-REPORTS" directory
                open('COVID-19-REPORTS/'+ x,"x")
                newf=open('COVID-19-REPORTS/'+ x,"w")
                df.to_csv(newf)
                newf.close()
                print("Today's file added with success in the directory")
            except FileExistsError:
                print("Today's file already exists in the directory")
        except urllib.error.HTTPError:
            print("Today's file not found in CV stats files, needs to wait.")
            x="not found"
        
        return(y,x)


    if (whichdate == "begin"):
        start_date = date(2020,1,22)
        end_date = datetime.datetime.now()
        end_date  = date(end_date.year, end_date.month, end_date.day)
        delta = timedelta(days=1)
        #Cycle from the begin date to now
        while start_date <= end_date:
            y = start_date.strftime("%m-%d-%Y.csv")
            start_date += delta
            try:
                url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/' + y
                df = pd.read_csv(url) #Reading the .csv file from the url
                try:
                    #Coping datas from the .csv file in a new .csv file in the "COVID-19-REPORTS" directory
                    open('COVID-19-REPORTS/'+y,"x")  
                    newf=open('COVID-19-REPORTS/'+ y,"w")
                    df.to_csv(newf)
                    newf.close()
                    print(y + ":file added with success in the directory")
                except FileExistsError:
                    print(y + ":file already exists in the directory")
            except urllib.error.HTTPError:
                print(y + ":file not found in the CV stats files, needs to wait.")
                y="not found"

