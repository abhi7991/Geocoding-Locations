# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 11:28:41 2019

@author: Abhishek.S
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 18:31:40 2019

@author: Abhishek.S
"""
import os
os.chdir(r"C:\Users\Abhishek.S\Anaconda3\Lib\site-packages\tabpy_server")
import pandas as pd
import time as t
import json
from sklearn.cluster import KMeans
import numpy as np
import sys
os.chdir(r"C:\Users\Abhishek.S\Anaconda3\Lib\site-packages\tabpy_server")
import pandas as pd
import random
import requests
from datetime import datetime as dt
import time as t
import json
from sklearn.cluster import KMeans
import numpy as np
import re
import subprocess
import errno
from multiprocessing import Pool

input = pd.read_csv("latlong.csv")
input = input.get("address") 
req = input.values.tolist()
#%%

def getGeocode(location):
  key = "AIzaSyAVv5ZvaIZ1S4od-VMPmQHc-1kgtL01bOM"
  post="https://maps.googleapis.com/maps/api/geocode/json?address="
  url =post+str(location)+"&key="+key
  latlong =[]
  r = requests.get(url = url)
  d = r.json()
  a = d["results"][0]['geometry']["location"]['lat']
  b = d["results"][0]['geometry']["location"]['lng']
  latlong.append(a)
  latlong.append(b)
#  print(a)
#  print(b)
  return latlong

lat_long= []
for i in range(len(req)):
    print(str(i)+'start')    
    b = getGeocode(req[i])
    print(str(i)+'done')
    lat_long.append(b)
#    pd.DataFrame(c)
print(lat_long)
#%%  
d = pd.DataFrame(lat_long)
e = pd.DataFrame(input)
d['address'] = e
d.columns = ['Latitude', 'Longitude', 'Address']
d.to_csv('output.csv',index = False, encoding = 'utf-8')


