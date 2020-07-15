import csv
import datetime
from datetime import timedelta
import pandas as pd
import urllib
import pymysql.cursors
import os
import numpy as np


def data():
    #Trying to connect to db
    try:
        connection = pymysql.connect(host='127.0.0.1', user='root',db='COVID')
        try:
            with connection.cursor() as cursor:
                #Foreach file in the directory "COVID-19-REPORTS"
                for filename in os.listdir('COVID-19-REPORTS/'):
                    if filename.endswith(".csv"):
                        #Checking if the file values are already in the db
                        row_count=cursor.execute("SELECT * FROM `DATA` d WHERE d.ReportName = " + "\"" + filename + "\"")
                        if (row_count == 0):
                            #Taking columns and values from .csv file
                            df = pd.read_csv('COVID-19-REPORTS/'+filename)
                            try:
                                df = df[['Province/State','Country/Region','Confirmed', 'Deaths', 'Recovered']]
                            except KeyError:
                                df = df[['Province_State','Country_Region','Confirmed', 'Deaths', 'Recovered']]
                            df.columns.values[0]="ProvinceState"
                            df.columns.values[1]="CountryRegion"
                            #Foreach row in the file, it does insert in the db.
                            for cr,pc,conf,dth,rcd in zip(df.CountryRegion.tolist(),df.ProvinceState.tolist(),df.Confirmed.tolist(),df.Deaths.tolist(),df.Recovered.tolist()):
                                string = ("INSERT INTO `DATA` (`ReportName`,`CountryName`,`ProvinceName`,`Confirmed`,`Death`,`Recovered`) VALUES(%s,%s,%s,%s,%s,%s)")
                                #Checking if not nan
                                if (np.isnan(rcd)): rcd=None
                                if (np.isnan(conf)): conf=None
                                if (np.isnan(dth)): dth = None 
                                if (type(pc)==float): pc=None
                                print(rcd,conf,dth,pc)
                                try:
                                    cursor.execute(string,(filename,cr,pc,conf,dth,rcd))
                                    print("DATA ADDED WITH SUCCESS")
                                except pymysql.err.IntegrityError:
                                    print("Value already exists")
                        else: print("DataTable: File values already in the DB")
            connection.commit()
        finally:
            connection.close()
    except pymysql.err.OperationalError:
        print("ERROR! Can't connect to the DB.")


