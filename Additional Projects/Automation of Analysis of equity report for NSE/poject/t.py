import requests

url = "https://archives.nseindia.com/content/historical/EQUITIES/2023/SEP/cm22SEP2023bhav.csv.zip"


localFile = url.split('/')[-1]
r = requests.get(url=url,stream=True)
open(localFile,'wb').write(r.content)
print(localFile)