from email.message import EmailMessage
import ssl as objSSL
import smtplib

strSender = 'XXXXXXXX@gmail.com'
strReceiver = 'XXXXXXXX@gmail.com'
strPassword = 'XXXXXXXX'

strSubject = 'Learning Email Sending with Python'

strBody = """ Learning how to send emails using Python. """

objEmail = EmailMessage()
objEmail['From'] = strSender
objEmail['To'] = strReceiver
objEmail['Subject'] = strSubject
objEmail.set_content(strBody)

objContext = objSSL.create_default_context()

objSMTP = smtplib.SMTP_SSL('smtp.gmail.com',465,context=objContext)
objSMTP.login(strSender, strPassword)
objSMTP.sendmail(strSender, strReceiver,objEmail.as_string())
