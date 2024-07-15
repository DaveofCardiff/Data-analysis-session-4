# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 09:26:09 2024

@author: Dave
"""

#TASK - 
#Read in pandsa(pd)
#Set your file path
#Ready in the following files - 
#police.csv, info.csv, doctor.csv
#Do some EDA (Expolitory Dave Analysis e.g. head, info, etc...)

import pandas as pd

path = "C:\\Users\\Dave\\Desktop\\PfDA\\Spreadsheets\\"

police = pd.read_csv(path + "police.csv")
info = pd.read_csv(path + "info.csv")
doctor = pd.read_csv(path + "doctor.csv")                  

police.head(10)
info.info
doctor.tail(5)
doctor.tail()

#join - Merge - A function that allows us to combine data from two tables.
#Based on a related column between two tables.
#Data in the related columns should be unique.

#Our columns to join are - P_ID because they are both in table and unique.

#Type of Join you want to do - 4 main types of joins to choose from.

#www.w3schools.com/sql/sql_join.asp
#Here are the different types of the JOINs in SQL:

#(INNER) JOIN: Returns records that have matching values in both tables
#LEFT (OUTER) JOIN: Returns all records from the left table, 
#and the matched records from the right table
#RIGHT (OUTER) JOIN: Returns all records from the right table, 
#and the matched records from the left table
#FULL (OUTER) JOIN: Returns all records when there is a match in either left 
#or right table

#table1, table2
#type of join
#How are we joining it?

joined_data = pd.merge(doctor, info, how='inner', on='P_ID')

outer_join = pd.merge(doctor, info, how='outer', on='P_ID')

#Task - now try and do a left join & then a right join

left_join = pd.merge(doctor, info, how='left', on='P_ID')
right_join = pd.merge(doctor, info, how='right', on='P_ID')

#checking the differences between two tables.

differences = pd.merge(doctor, info, how='outer', indicator='Table Name')

differences = differences.loc[differences['Table Name'] != 'both']


#Remove the rows containing certain values
#Update our poice dataframe.
#Store it as DF
#We want to target the column driver_age_raw
#Target a certain value and remove.

police = police[police['driver_age_raw'] != 8801]
police = police[police['driver_age_raw'] != 2919]

#Filter data targeting values.

age = police[police['driver_age'] == 84]

#unique entries
police['driver_race'].unique()
#number of unique entries
police['driver_race'].nunique()
#volumes of each unique entry
police['driver_race'].value_counts()

police.info()

police_dates = pd.read_csv(path + "police.csv", parse_dates=['stop_date'])

police_dates.info()

#police stops in a date range:
#2 variables
#start date
#end date

start_date = '2005-01-01'
end_date = '2005-08-01'    

#logical operators are no good for this - don't compare the data.
#and, or, not - DON'T USE THESE.

#Bitewise Operator - & #and, | #or
#Compare values - Look and give your data between the given ranges.

#Take wjat you ask one by one - unless you use sets brackets.

date_range = (police['stop_date'] >= start_date) & (police['stop_date'] <= end_date)
 
date_range = police.loc[date_range]

#Group by allows us to group our data by a category /multiple categories / columns.
#Along side of it pick another column(s) to analyse that data with.

#Agerage Age of driver per driver race.

average_driver = date_range.groupby(['driver_race'])[['driver_age', 'driver_age_raw']].mean().round(0).reset_index()

#Pandas series
#https://pandas.pydata.org/pandas-docs/stable/reference/series.html

#We can split our data - using pandas series functrions.
#datatime functions - dt

police_dates['year'] = police_dates['stop_date'].dt.year

police_dates['month'] = police_dates['stop_date'].dt.month

police_dates['day'] = police_dates['stop_date'].dt.day

#Monday = 0, Tuesday = 1, etc...
police_dates['Day_of_the_week'] = police_dates['stop_date'].dt.weekday

#We want to change the month number to become a month name.

#Create a dictionary - to pair them up.

months = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
          7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}

police_dates['month'].replace(months, inplace=True)

#Task - Now do the same for Weekday

days = {0: 'Mon', 1: 'Tue', 2: 'Wed', 3: 'Thu', 4: 'Fri', 5: 'Sat', 6: 'Sun'}
police_dates['Day_of_the_week'].replace(days, inplace=True)

police_dates['Month_Number'] = police_dates['stop_date'].dt.month


#Sorting the data - ascenting =True (default) a-z

police_dates.sort_values(['Month_Number'], ascending=False, inplace=True)


#2 variations of saving your data.

police_dates.to_csv(path + 'police_update.csv', index=False)
police_dates.to_excel(path + 'police_update.xlsx', index=False)



