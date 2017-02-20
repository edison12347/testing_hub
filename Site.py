import requests

r = str(requests.get('https://reentryvisa.inis.gov.ie/website/INISOA/IOA.nsf/(getApps4DT)?openagent&dt=20/02/2017&type=I&num=1&_=1486826956189'))

#print(r.text)

print("In the file you see:")

f = open('request.txt', 'r+')

f.write(r)

print(f.read())
