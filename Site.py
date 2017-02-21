import requests
from datetime import datetime, date, time, timedelta

open('request.txt', 'w').close()
f = open('request.txt', 'r+')

print(f.read())

START_DATE = datetime.strptime("21/02/2017", '%d/%m/%Y')  # excange the hardcoded date for today, datatitme.today()
DAYS2CHECK = 10
#end_date = datetime.strptime("23/02/2017", '%d/%m/%Y')

for i in range(1, DAYS2CHECK):
    date = START_DATE + timedelta(days = i)
    date = date.strftime('%d/%m/%Y')
    r = requests.get('https://reentryvisa.inis.gov.ie/website/INISOA/IOA.nsf/(getApps4DT)?openagent&dt='+ date +'&type=I&num=1&_=1486826956189')  # string has a .format method better use it
    f.write(str(d)+ " : " + str(r.text) + '\n')
