from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import smtplib

URL = "smtp.gmail.com"                   # Url SSL
PORT = 465                               # Port SSL

IMG = '..\\files\\rick.jpeg'
DOC = "..\\files\\doc.txt"

SENDER = 'python_sender@gmail.com'              # Sender E-mail
RECIPIENT = 'python_recipient@gmail.com'        # Recipient E-mail
PASSWORD = '**********'                         # Your Password

# create message object instance
msg = MIMEMultipart()

# setup the parameters of the message
password = PASSWORD
msg['From'] = SENDER
msg['To'] = RECIPIENT
msg['Subject'] = "Subject Test Send - Files"
 
# add in the message body
message = "Test send files in email"
fpImg = open(IMG, 'rb')
fpTxt = open(DOC, 'rb')
 
img = MIMEImage(fpImg.read(), _subtype="jpeg")
doc = MIMEImage(fpTxt.read(), _subtype="txt")
    
fpImg.close()
fpTxt.close()

msg.attach(MIMEText(message, 'plain'))
msg.attach(img)
msg.attach(doc)

print("Sending message...")

server = smtplib.SMTP_SSL(URL, PORT)
server.login(msg['From'], password)
server.sendmail(msg['From'], msg['To'], msg.as_string())

print("Message send sucessfully!")

server.quit()
