import requests
import time
from datetime import datetime, date, timedelta

open('request.txt', 'w').close()
f = open('request.txt', 'r+')

print(f.read())

START_DATE = datetime.today()
DAYS2CHECK = 10
#end_date = datetime.strptime("23/02/2017", '%d/%m/%Y')
while True:
    for i in range(1,DAYS2CHECK):
        d = START_DATE + timedelta(days = i)
        d = d.strftime('%d/%m/%Y')
        r = requests.get('https://reentryvisa.inis.gov.ie/website/INISOA/IOA.nsf/(getApps4DT)?openagent&dt={}&type=I&num=1&_=1486826956189'.format(d))
        f.write(str(d)+ " : " + str(r.text) + '\n')
    time.sleep(60)