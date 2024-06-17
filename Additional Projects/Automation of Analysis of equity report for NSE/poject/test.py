import requests
import shutil

url = "https://archives.nseindia.com/content/historical/EQUITIES/2023/SEP/cm{}SEP2023bhav.csv.zip"

days =5

def downloadFiles(urls):
 localFile = url.split('/')[-1]
 with requests.get(url=url,stream=True)as r:
#open(localFile,'wb').write(r.content)
  with open(localFile,'wb')as f:
   shutil.copyfileobj(r.raw,f)
 print(localFile)
 return localFile

for i in range(days):
  
