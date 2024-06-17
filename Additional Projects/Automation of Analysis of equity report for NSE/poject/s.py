import requests
import shutil
import os

url = "https://archives.nseindia.com/content/historical/EQUITIES/2023/SEP/cm21SEP2023bhav.csv.zip"

def fileValues(url_1):
 local_filename =url_1.split('/')[-1]
 with requests.get(url=url_1,stream=True) as r:
   print("Hello")
   with open(local_filename ,'wb')as f:
      shutil.copyfileobj(r.raw,f)
      print("copied")
 return local_filename   

fileValues(url) 




