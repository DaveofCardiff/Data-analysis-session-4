# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 14:06:20 2024

@author: Dave
"""

import pandas as pd

path = "C:\\Users\\Dave\\Desktop\\PfDA\\Spreadsheets\\"

airbnb = pd.read_csv(path + "airbnb.csv")

#1.	Find out the info about the data.

airbnb.info

#2.	View the top 5 rows of the data

airbnb.head(5)

#3.	Check for how many null items are in each column - if any then remove them.

airbnb.isnull().sum()
airbnb.dropna(subset=['host_response_rate', 'neighbourhood',
                      'review_scores_rating'], inplace=True)

#4.	Check for any duplicates - if any then remove them. 

airbnb.duplicated().sum()

#5.	You then need to remove the value - SF from the city column.

airbnb = airbnb[airbnb['city'] != 'SF']

#6.	Find out the unique values from city to check the above has worked.

airbnb['city'].unique()

#7.	Rename the following columns (you can do it as one or separately). 
#– cleaning_fee (cleaning_price), room_type(type_of_room) & zipcode(postcode)

airbnb.rename(columns={'cleaning_fee': 'cleaning_price',
                       'room_type': 'type_of_room',
                       'zipcode': 'postcode'}, inplace=True)


#8.	Drop the columns amenities and host_identity_verified

airbnb = airbnb.drop(['amenities'], axis=1)

airbnb = airbnb.drop(['host_identity_verified'], axis=1)

#9.	You need to replace strict & flexible from the cancellation_policy Column 
#with really_strict & really_flexible.


airbnb['cancellation_policy'] = airbnb['cancellation_policy'].replace(['strict',
                                                                       'flexible'],
                                                                      ['really_strict',
                                                                       'really_flexible'])

#10.	You then need to complete a value count of how many of each policy.

airbnb['cancellation_policy'].value_counts()

#11.	You then need to find all of the Airbnb’s that accommodate over 10

acc_over_10 = airbnb[airbnb['accommodates'] >10].reset_index(drop=False)

#12.	You then need to find all of the Airbnb’s that have over 50 reviews

rev_over_50 = airbnb[airbnb['number_of_reviews'] >50].reset_index(drop=False)

#13.	Now create a day, month and year column from the host_since column.

airbnb_dates = pd.read_csv(path + "airbnb.csv", parse_dates=['host_since'])

airbnb_dates['year'] = airbnb_dates['host_since'].dt.year

airbnb_dates['month'] = airbnb_dates['host_since'].dt.month

airbnb_dates['day'] = airbnb_dates['host_since'].dt.day

#14.	Sort the data by city.

airbnb.sort_values(['city'], ascending=True, inplace=True)

#15.	Save this updated file.

airbnb.to_csv(path + 'airbnb_update.csv', index=False)
airbnb.to_excel(path + 'airbnb_update.xlsx', index=False)

#Create 3 groupby following the correct specification:

#1.	Average Price & Average Number of Reviews per city - 
#with the index reset and the data rounded to 1 decimal place.

av_per_city = airbnb.groupby(['city'])[['price',
                                        'number_of_reviews']].mean().round(1).reset_index()
    
#2.	Lowest Price per neighbourhood with the index reset.

per_neighbourhood = airbnb.groupby(['neighbourhood'])[['price']].min().reset_index()

#3.	Highest price per accommodates - index reset - data rounded to 1 decimal 
#place & then sorted by accommodates (ascending False)

per_accommodates = airbnb.groupby(['accommodates'])[['price']].max().round(1).reset_index()
per_accommodates.sort_values(['accommodates'], ascending=False, inplace=True)

#4.	Finally - Save the 3 groupby - Feel free to add any other functions along the way.

av_per_city.to_csv(path +"av_per_citye.csv", index = False)
per_neighbourhood.to_csv(path +"per_neighbourhood.csv", index = False)
per_accommodates.to_csv(path +"per_accommodates.csv", index = False)


    


