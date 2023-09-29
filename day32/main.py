import smtplib
import datetime as dt
import random

my_email = "jackw1689@gmail.com"

password = "eldxlwscmsvxewuv"

with smtplib.SMTP('smtp.gmail.com', port=587) as connection:

    connection.starttls()
    connection.login(user=my_email,password=password)
    connection.sendmail(from_addr=my_email, to_addrs='park.sherrie@gmail.com',msg='Subject:Hello\n\n i do not think we should get another dog')


with open('./quotes.txt','r') as f:
    mylist = f.readlines()
    print(random.sample(mylist,1))