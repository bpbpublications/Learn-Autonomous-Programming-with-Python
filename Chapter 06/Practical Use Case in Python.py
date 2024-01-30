# Importing required libraries
import time
import pandas as pd
import datetime
import pywhatkit
from email.message import EmailMessage
import ssl as objSSL
import smtplib

# Reading the excel in a dataframe
df = pd.read_excel("Data.xlsx")

today = datetime.datetime.now().strftime("%m-%d")

strSender = 'XXXXXXXXX'
strPassword = 'XXXXXXXXXXX'
strSubject = 'Happy Birthday!'
strBody = """ Wish you a very happy birthday! """
# Looping through every row of the table
i=0
for row in df['Birthday']:
    birthday = row.strftime("%m-%d")

	 # Checking if the birth date is same as the date today
    if birthday == today:
        strName = df['Name'].loc[i]
        strWhatsAppNo = df['WhatsApp No'].loc[i]  
            pywhatkit.sendwhatmsg_instantly("+"+str(strWhatsAppNo),"Hello"\
            +strName +" This is a test message sent using Python.")
        time.sleep(15)
        strReceiver = df['Email ID'].loc[i]
        print(strWhatsAppNo)
        print(strReceiver)
        objEmail = EmailMessage()
        objEmail['From'] = strSender
        objEmail['To'] = strReceiver
        objEmail['Subject'] = strSubject
        objEmail.set_content(strBody)

        objContext = objSSL.create_default_context()

        objSMTP = smtplib.SMTP_SSL('smtp.gmail.com',465,context=objContext)
        objSMTP.login(strSender, strPassword)
        objSMTP.sendmail(strSender, strReceiver,objEmail.as_string())
    i+=1 
			
