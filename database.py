import sqlite3 as lite
import pandas as pd
import sys

con = lite.connect('getting_started.db')

cities = (('New York City', 'NY'),('Boston', 'MA'),('Chicago', 'IL'),('Miami', 'FL'),('Dallas', 'TX'),('Seattle', 'WA'),('Portland', 'OR'),('San Francisco', 'CA'),('Los Angeles', 'CA'))
weather = (('New York City','2013','July','January','62'),('Boston','2013','July','January','59'),('Chicago','2013','July','January','59'),('Miami','2013','August','January','84'),('Dallas','2013','July','January','77'),('Seattle','2013','July','January','61'),('Portland','2013','July','December','63'),('San Francisco','2013','September','December','64'),('Los Angeles','2013','September','December','75'))

warm_city = raw_input("Show me which cities are warm in this month: ")

with con:
	cur = con.cursor()

	cur.execute("DROP TABLE IF EXISTS cities;")
	cur.execute("DROP TABLE IF EXISTS weather;")
	cur.execute("create table cities (name text, state text)")
	cur.execute("create table weather (city text, year integer, warm_month text, cold_month text, average_high integer)")
	cur.executemany("INSERT INTO cities VALUES(?,?)", cities)
	cur.executemany("INSERT INTO weather VALUES(?,?,?,?,?)", weather)
	query = "select cities.name, cities.state from weather join cities on cities.name = weather.city where warm_month = :warm_city" 
	cur.execute(query,{'warm_city':warm_city})

	rows = cur.fetchall()
	cols = [desc[0] for desc in cur.description]

	try:
		df = pd.DataFrame(rows, columns=cols)
	except ValueError:
		print "No cities have as the warmest month"

	for row in rows:
		city = row[0].rstrip()
		state = row[1].lstrip()
		str = ", "
		city_state = (city, state)
		print str.join( city_state ),

#add in lowercase edgecase