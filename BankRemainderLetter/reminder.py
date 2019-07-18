#import json file
#iterate every user and append its detail dynamically to text file. create text file using file handling
#file name should be "customername-customerid"

import urllib.request, json 
from jinja2 import Environment, FileSystemLoader

with urllib.request.urlopen("https://raw.githubusercontent.com/shakirshakeelzargar/practice-python/master/assets/fd-reminder.json") as url:
    data = json.loads(url.read())
  
for i in data:
    file_loader = FileSystemLoader('./')
    env = Environment(loader=file_loader)
    template = env.get_template('template.txt')
    output = template.render(cname=i['customer_name'],schemeName=i['deposit_type'],amountDeposited=i['amount_deposited'],maturityAmount=i['maturity_amount'],maturesOn=i['matures_on'],depositDate=i['deposit_date'],depositType=i['deposit_type'],truth=True)
                
    f=open("D:\RemainderLetter\output\{}-{}.txt".format(i['customer_name'],i['customer_id']),"w+")
    f.write("{}".format(output))
