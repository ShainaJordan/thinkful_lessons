import darksky
from urllib import urlopen
import datetime
import time
import requests
import sqlite3 as lite
from pandas.io.json import json_normalize
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

con = lite.connect('weather.db')
cur = con.cursor()

df = pd.read_sql_query("SELECT * FROM daily_temp", con)

print df

print str(df['Denver'].mean()) + " is the mean in Denver"
print str(df['New_Orleans'].mean()) + " is the mean in New_Orleans"
print str(df['New_York'].mean()) + " is the mean in New_York"
print str(df['Philadelphia'].mean()) + " is the mean in Philadelphia"
print str(df['Seattle'].mean()) + " is the mean in Seattle"


print str(df['Denver'].median()) + " is the median in Denver"
print str(df['New_Orleans'].median()) + " is the median in New_Orleans"
print str(df['New_York'].median()) + " is the median in New_York"
print str(df['Philadelphia'].median()) + " is the median in Philadelphia"
print str(df['Seattle'].median()) + " is the median in Seattle"

print str(df['Denver'].max()-df['Denver'].min()) + " is the difference in Denver"
print str(df['New_Orleans'].max()-df['New_Orleans'].min()) + " is the difference in New_Orleans"
print str(df['New_York'].max()-df['New_York'].min()) + " is the difference in New_York"
print str(df['Philadelphia'].max()-df['Philadelphia'].min()) + " is the difference in Philadelphia"
print str(df['Seattle'].max()-df['Seattle'].min()) + " is the difference in Seattle"

df['Denver'].hist()
df['New_Orleans'].hist()
df['New_York'].hist()
df['Philadelphia'].hist()
df['Seattle'].hist()

plt.show()

