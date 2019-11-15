#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Amalia Gregori <@am_aliag>
# Version: 3.0.0
# Last modified: 20191115 by @am_aliag

# Little programming script for organizing a Secret Santa game

# Import libraries
try:
    from pandas import read_csv
except:
    print("pandas library needed, try 'pip install -U pandas'")

from sys import exit
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import getpass
import argparse

# Flags & args 
parser = argparse.ArgumentParser()

parser.add_argument("-f", "--file", action="store", dest="file_name",
                    help=".csv file with the participants", required=True)
parser.add_argument("-v", "--version", action="version", version='%(prog)s 2.0.0')

# Function game
def game(file_name, gmailUser, gmailPassword):
    
    # Checking if the file is a .csv
    try:
        # Open the given CSV with the names & emails
        input = read_csv(file_name)
    except:
        print("Filetype ERROR: File must be .csv")
        exit(0)
    
    # First shuffle of input names
    output = input.sample(frac=1).reset_index(drop=True)
    
    # Checking if there are replications between input and output lists
    while (input['NAME'] != output['NAME']).all() != True:
        output = input.sample(frac=1).reset_index(drop=True)
    
    # Sending the emails with the results
    for j in range(0,len(input['NAME']),1):

        # Message
        message = """
        Hello %s, you are %s's Secret Santa. Now it's time to think about a present for this special person (ﾉ◕ヮ◕)ﾉ*:・ﾟ✧\n 
        But remember that the most important thing is to enjoy the party all together. \n \n ✨❤️ (っ＾▿＾)۶٩(˘◡˘ ) ❤️✨
        """%(input['NAME'][j],output['NAME'][j])

        # Email items
        msg = MIMEMultipart()
        msg['From'] = gmailUser
        msg['To'] = input['EMAIL'][j]
        msg['Subject'] = "[RESULT] - Secret Santa" # Subject
        msg.attach(MIMEText(message))

        # Connection settings to SMTP server
        mailServer = smtplib.SMTP('smtp.gmail.com', 587)
        mailServer.ehlo()
        mailServer.starttls()
        mailServer.ehlo()

        # Trying to log into the email account
        try:
            mailServer.login(gmailUser, gmailPassword)

        except:
            print("Authentication ERROR: incorrect username or password")

            # Second try...
            try:
                gmailUser = input("Username: ")
                gmailPassword = getpass.getpass()
                mailServer.login(gmailUser, gmailPassword)
 
            except:
                print("Authentication ERROR: incorrect username or password")
                mailServer.close()
                exit(0)

        # Sending the email & closing connection to server
        mailServer.sendmail(gmailUser, input['EMAIL'][j], msg.as_string())
        mailServer.close()

# MAIN
# Parsing flags
args = parser.parse_args()

if __name__ == "__main__":
        
    file_name = args.file_name
    
    # Asking for gmail credentials
    gmailUser = input("Username: ")
    gmailPassword = getpass.getpass()

    game(file_name, gmailUser, gmailPassword)