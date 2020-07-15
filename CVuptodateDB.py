import csv
import datetime
from datetime import timedelta
import pandas as pd
import urllib
import pymysql.cursors
import CVcheckfiles
import os
import numpy as np

def __DataTableUpToDate(file):
    #Open the .csv file for read the data.
    df = pd.read_csv('COVID-19-REPORTS/'+file)
    try:
        df = df[['Province/State','Country/Region','Confirmed', 'Deaths', 'Recovered']]
    except KeyError:
        df = df[['Province_State','Country_Region','Confirmed', 'Deaths', 'Recovered']]
    df.columns.values[0]="ProvinceState" #Changing name of first column
    df.columns.values[1]="CountryRegion" #Changing name of second column
    #Trying to connect to db
    try:
        connection = pymysql.connect(host='127.0.0.1', user='root',db='COVID')
        try:
            with connection.cursor() as cursor:
                #Executing the query and putting the result in row_count
                row_count=cursor.execute("SELECT * FROM `DATA` d WHERE d.ReportName = " + "\"" + file + "\"")
                if (row_count == 0): #Checking if the # of rows is 0 -> if row_count != 0 means that there are the values of the file in the db.
                    #Cycling on the rows of the df file.
                    for cr,pc,conf,dth,rcd in zip(df.CountryRegion.tolist(),df.ProvinceState.tolist(),df.Confirmed.tolist(),df.Deaths.tolist(),df.Recovered.tolist()):
                        #Query Insert create
                        string = ("INSERT INTO `DATA` (`ReportName`,`CountryName`,`ProvinceName`,`Confirmed`,`Death`,`Recovered`) VALUES(%s,%s,%s,%s,%s,%s)")
                        #Checking if values are nan
                        if (np.isnan(rcd)): rcd=None
                        if (np.isnan(conf)): conf=None
                        if (np.isnan(dth)): dth = None 
                        if (type(pc)==float): pc=None
                        try:
                            #Execute the insert query
                            cursor.execute(string,(file,cr,pc,conf,dth,rcd))
                            print("DATA ADDED WITH SUCCESS:",cr,pc,conf,dth,rcd)
                        except pymysql.err.IntegrityError:
                            print("INTEGRITY ERROR")
                else: print("FILE'S VALUE ALREADY IN THE DB")
            connection.commit()
        finally:
            connection.close()
    except pymysql.err.OperationalError:
        print("ERROR! Can't connect to the DB.")

def uptodate():
    file=CVcheckfiles.downloadCVfiles("uptodate") #Download of yesterday's and today's file
    if (file[0]!="not found"): 
        print("Putting yesterday's file values in the DB: ", end='')
        __DataTableUpToDate(file[0]) 
    if (file[1]!="not found"): 
        print("Putting today's file values in the DB", end='')
        __DataTableUpToDate(file[1])
