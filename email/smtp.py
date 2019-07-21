# This Python file uses the following encoding: utf-8
import os, sys
import smtplib
import csv
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText


def sendMail(name, email):
    fromaddr = "trucks@trucksearch.us" #our email Address
    subject = "Commercial Trucks" # email subject

    toaddr = email
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = subject

    #
    # EMAIL MESSAGE
    # %s is what will get replaced by the script everytime you run itself.
    #

    body = """Hello %s,

    I know that State Farm has the best rates for commercial trucks that are filed in specific way with the department of transportation's SAFER site.

    How would you like the ability to generate a list based on their data?

    For example:

        Trucking companies who are filed with the DOT on the SAFER site as:
            Intrastate,
            Beverages,
            In your territory’s zip code.

    Visit www.trucksearch.us and for only $19.99 a month you can generate a custom commercial report. The site is updated weekly with new DOT filings

    Regards

    www.TruckSearch.US
    LJC TECH INC
    303 Nina st
    New Windsor, NY 12553
    347-450-8119

    To stop recieving these emails, reply with the word unsubscribe in the subject line. Please tell us the reason why you wish to stop recieving these emails, thank you.
    """%name


    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('email-smtp.us-east-1.amazonaws.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login("AKIAIGT3YHM7MAJVV6QQ", "Ak9AIjE26rzzTgS7IiIaANswTWwXqUZ/wQCcVM9n3dwG")
    server.ehlo()
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

    print "sent to: '%s'"%toaddr


with open('contact.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for i,row in enumerate(csv_reader):
        print( str(i) +" "+row[2])
        sendMail(row[0], row[2])
