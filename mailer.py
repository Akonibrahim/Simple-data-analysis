
# # Tips before proceed
# ## This program has to be executed after 5 days to Die to get the file
# ## Every files has to be in a same folder

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


import pandas as pd
import datetime


today = datetime.date.today()


# ## Reading the file created by the first progra


chronos = pd.read_csv('Tablets That Expire After {}.csv'.format(today))


fromaddr = "malathi336@gmail.com"
toaddr = "dharshanamdh@gmail.com"
  
# instance of MIMEMultipart
msg = MIMEMultipart()
 
# storing the senders email address  
msg['From'] = fromaddr
 
# storing the receivers email address 
msg['To'] = toaddr
 
# storing the subject 
msg['Subject'] = "Tablets that expiring today"


# # I just changed your programs mail body to the tablets name from first progra


body = str(chronos['TABLET NAME'])
 
# attach the body with the msg instance
msg.attach(MIMEText(body, 'plain'))


s = smtplib.SMTP('smtp.gmail.com', 587)
 
# start TLS for security
s.starttls()
 
# Authentication
s.login(fromaddr, "tajmahal29")
 
# Converts the Multipart msg into a string
text = msg.as_string()
 
# sending the mail
s.sendmail(fromaddr, toaddr, text)
 
# terminating the session
s.quit()

print('The mail has been sent!')
