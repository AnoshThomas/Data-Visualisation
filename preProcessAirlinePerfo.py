# -*- coding: utf-8 -*-
"""
Created on Sun May 21 17:22:43 2017

@author: TH759D
"""

import seaborn as sns
import pandas as pd

inputfile="129994168_32017_1830_airline_delay_causes.csv"

df=pd.read_csv(inputfile,delimiter=';')

print df.columns.values

# create an aggregate for each year for each Airline

yearlyArrivals= df.groupby(by=['carrier','year'])['arr_flights'].sum()
yearlyDelays=df.groupby(by=['carrier','year'])['arr_del15'].sum()
yearlyCancelled=df.groupby(by=['carrier','year'])['arr_cancelled'].sum()
yearlyDiverted=df.groupby(by=['carrier','year'])['arr_diverted'].sum()

#print len(yearlyArrivals),len(yearlyDiverted)

newDf=pd.concat([yearlyArrivals,yearlyDelays,yearlyCancelled,yearlyDiverted],
                axis=1).reset_index()
print newDf.columns.values


newDf["onTime"] = 1.0 - newDf["arr_del15"]/newDf["arr_flights"]

#newDf.to_csv("airlinePerfoPreprocessed.csv",index=False)

# create a separate csv file for each year

yearList=list(set(newDf["year"].tolist()))
#print(yearList)

for year in yearList:
    print year
    tempDf=newDf.loc[newDf['year'] == year]
    print(tempDf)
    outfile="airlinePerfoPreprocessed_%s.csv" %(year)
    tempDf.to_csv(outfile,index=False)