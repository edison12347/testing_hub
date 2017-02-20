import requests
import datetime
from datetime import datetime, date, time, timedelta

r = str(requests.get('https://reentryvisa.inis.gov.ie/website/INISOA/IOA.nsf/(getApps4DT)?openagent&dt=20/02/2017&type=I&num=1&_=1486826956189'))

#print(r.text)

print("In the file you see:")

f = open('request.txt', 'r+')

f.write(r)

print(f.read())

start_date = datetime.strptime("20/02/2017", '%d/%m/%Y')
end_date = datetime.strptime("23/02/2017", '%d/%m/%Y')

d = date.today() + timedelta(days = 1)
d = datetime.strptime('20-02-2017', '%d-%m-%Y')+ timedelta(days = 1)

print(d)
