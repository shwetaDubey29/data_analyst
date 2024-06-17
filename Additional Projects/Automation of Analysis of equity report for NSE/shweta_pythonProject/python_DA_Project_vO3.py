import requests
import shutil
from datetime import date,timedelta
import calendar
from zipfile import ZipFile
import pandas as pd
from pathlib import Path
import urllib.request
import os

#creating var and string  for path

DATASET = Path("./shweta_pythonProject/dataset")
DATASET_CLEAN = Path("./shweta_pythonProject/dataset_clean")
HOLIDAYS_LIST =Path("./shweta_pythonProject/holiday_list")
DB_Script = Path("./shweta_pythonProject/db_Script")

# file1 = open(".\shweta_pythonProject\dataset\shweta.txt","r").read()
# print(file1)



#delete dir if exits 
if os.path.exists(DATASET) and os.path.isdir(DATASET):
   shutil.rmtree(DATASET)

if os.path.exists(DATASET_CLEAN) and os.path.isdir(DATASET_CLEAN):
   shutil.rmtree(DATASET_CLEAN)

#make new dir if exits

DATASET.mkdir(parents=True,exist_ok=True)
DATASET_CLEAN.mkdir(parents=True,exist_ok=True)
HOLIDAYS_LIST.mkdir(parents=True,exist_ok=True)
DB_Script.mkdir(parents=True,exist_ok=True)


'''function  to download file from URL'''

def downloadFile(url):
   fileName  = url.split('/')[-1]
   with requests.get(url,stream=True) as r:
      print("Inside the download_file function ")
      localFile = DATASET / fileName 
      with open(localFile,"wb") as f:
         shutil.copyfileobj(r.raw,f)   
   return fileName 

referenceDate =  date(2023,11,16)

base_url="https://archives.nseindia.com/content/historical/EQUITIES/2023/#/cm{}bhav.csv.zip"
i=0
j=0

HOLIDAY_NAME = HOLIDAYS_LIST / "holiday_list_nse.csv "
df = pd.read_csv(HOLIDAY_NAME)
df = df[df['YEAR'] == referenceDate.year]
df['DATE'] = pd.to_datetime(df['DATE'])

print(df.head())



# df=pd.read_csv(HOLIDAY_FILE_NAME) # Reading the csv file which contains the holiday list
# df=df[df['YEAR']==reference_date.year] # Filtering the data for year of reference date
# df['DATE'] = pd.to_datetime(df['DATE']) # converting the DATE column into datetime object since by default panda stores it as object data type
# #df['DATE'] = df['DATE'].dt.date
# df.head()
