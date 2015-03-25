import darksky
from urllib import urlopen
import datetime
import time
import requests
import sqlite3 as lite
from pandas.io.json import json_normalize
import matplotlib.pyplot as plt
import pandas as pd

api_key = "cefee5c7bf6d79b9421c19c285ecf15b"
start_date = datetime.datetime.now() - datetime.timedelta(days=30)
unixtime = time.mktime(start_date.timetuple())


cities = {"Denver": '39.76185,-104.881105',
		"New_Orleans": '30.05342,-89.934502',
		"New_York": '40.663619,-73.938589',
		"Philadelphia": '40.009376,-75.133346',
		"Seattle": '47.620499,-122.350876'
		}

#generate url to call to api
#for i in cities.values():
	#call = "https://api.forecast.io/forecast/"+api_key+"/"+i+","+str(int(unixtime))
	#url = urlopen(call).read()
	#r = requests.get(call)

#look at hierarchy of keys

con = lite.connect('weather.db')
cur = con.cursor()



cities.keys()
#with con:
	#cur.execute('CREATE TABLE daily_temp(day_of_reading INT, Atlanta REAL, Austin REAL, Boston REAL, Chicago REAL, Cleveland REAL);')

end_date = datetime.datetime.now()
query_date = end_date - datetime.timedelta(days=30) #the current value being processed
with con:
    while query_date < end_date:
        cur.execute("INSERT INTO daily_temp(day_of_reading) VALUES (?)", (int(query_date.strftime('%s')),))
        query_date += datetime.timedelta(days=1)

#loop through the cities and query the api
for k,v in cities.iteritems():
    query_date = end_date - datetime.timedelta(days=30) #set value each time through the loop of cities
    while query_date < end_date:
        #query for the value
        unixtime = time.mktime(query_date.timetuple())
        call = "https://api.forecast.io/forecast/"+api_key+"/"+v+","+str(int(unixtime))
        url = urlopen(call).read()
        r = requests.get(call)

        with con:
            #insert the temperature max to the database
            cur.execute('UPDATE daily_temp SET ' + k + ' = ' + str(r.json()['daily']['data'][0]['temperatureMax']) + ' WHERE day_of_reading = ' + query_date.strftime('%s'))

        #increment query_date to the next day for next operation of loop
        query_date += datetime.timedelta(days=1) #increment query_date to the next day


con.close() # a good practice to close connection to database

