import requests
from datetime import datetime, date, time, timedelta

open('request.txt', 'w').close()
f = open('request.txt', 'r+')

print(f.read())

start_date = datetime.strptime("21/02/2017", '%d/%m/%Y')
#end_date = datetime.strptime("23/02/2017", '%d/%m/%Y')

for i in range(1,5):
    d = start_date + timedelta(days = i)
    d = d.strftime('%d/%m/%Y')
    r = requests.get('https://reentryvisa.inis.gov.ie/website/INISOA/IOA.nsf/(getApps4DT)?openagent&dt='+ d +'&type=I&num=1&_=1486826956189')
    f.write(str(d)+ " : " + str(r.text) + '\n')