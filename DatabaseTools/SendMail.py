# script to send email to list of recipients

import smtplib
import ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import CSV_Read_Write as CSV

import config as cfg

PORT = 587  # for SSL
SMTP_server = "smtp.gmail.com"
csvFile = 'EmailList.csv'

senderEmail = cfg.Gmail['email']  # Enter your address
PASSWORD = cfg.Gmail['password']

# receiverEmail = "sambajracharya@icimod.org"  # Enter receiver address

MESSAGE = """\
Subject: Hi there
This message is sent from Python."""


def sendEmail(*args):
    # Create a multipart message and set headers
    msg = MIMEMultipart("alternative")
    msg["From"] = args[0]
    msg["To"] = args[1]
    msg["Subject"] = "Notification from python script"

    # Create the plain-text and HTML version of your message

    text = """\
    Hi,
    Test Email:
    Real Python has many great tutorials:
    www.realpython.com
    Best Regards,
    Sameer"""

    html = """\
    <html>
      <body>
        <p>Hi, <b>""" + args[2] + """</b></br></br>
           Attention:<br>""" + MESSAGE + """
        </p>
        <p><i>This is an automated message from script. Do not reply to this e-mail.</i></p>
      </body>
    </html>
    """

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    msg.attach(part1)
    msg.attach(part2)

    # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(SMTP_server, PORT)

        server.starttls(context=context)  # Secure the connection

        # Login to Email
        server.login(args[0], PASSWORD)

        # Send Email
        server.sendmail(args[0], args[1], msg.as_string())
        print("Email sent to {}".format(args[1]))
    except Exception as e:
        # Print any error messages to stdout
        print("Login Failed ...", e)
    finally:
        server.quit()


csvData = CSV.readCSV_pd(csvFile)
for index, row in csvData.iterrows():
    name = row['name']
    email = row['email']
    # print(name, email)
    sendEmail(senderEmail, email, name)
