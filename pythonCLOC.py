#!/usr/bin/python
import sys
import subprocess
import smtplib
import shutil
import subprocess
import shutil
import os
import stat
from os import path
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

#****************HELP*****************#
import argparse

parser=argparse.ArgumentParser(
    description='''Script to scan a gitub source repository and send the ouput to an email ''',
    epilog="""**************END*************.""")

parser.add_argument('repo', default='https://github.com/hsanfo/clocwithgithub.git', help='GITHUB URL IN HTTPS!')
parser.add_argument('email', default='cloctogithubmail@gmail.com', help='CLOC scan result will be sent to this Email adress!')
args=parser.parse_args()
print(args)
#****************HELP*****************#

#*******Clean repo*********#
def removerepo(rep):
    for root, dirs, files in os.walk(rep):
        for dir in dirs:
            os.chmod(path.join(root, dir), stat.S_IRWXU)
        for file in files:
            os.chmod(path.join(root, file), stat.S_IRWXU)
    shutil.rmtree(rep)
#*******Clean repo*********#
tmp = "temp-cloc-repot"
cloc = "cloc " + tmp
isExist = os.path.isdir(tmp)

#check if the temp repot file exist
gitrep = args.repo
destEmail = args.email
if isExist:
    removerepo(tmp)

# clone the repot to be scannned by cloc tool.
clone = "git clone --depth 1 "+ gitrep+ " " +  tmp
os.system(clone)

# lunch cloc
try :
    result = subprocess.check_output(cloc,shell=True, stderr=subprocess.STDOUT)
    print('\n ***********************result*********************** \n')
    print(str(result, 'utf-8'))
    print('\n')
except:
    print('May be you should install the cloc tool before :)')
#remove the temporary cloned repository
removerepo(tmp)

#send result to  email (for local smtp serveur)
try :
    s=smtplib.SMTP(host='localhost', port=1025)
    s.sendmail("halidsanfo@gmail.com", destEmail, "the cloc scan result : "+str(result, 'utf-8') )
    s.quit()
except :
    tips = 'In LINUX : python -m smtpd -n -c DebuggingServer localhost:1025'
    print('You may need to start a local smtp server to test the mail sending part of the demo :)')
    print(tips)


''' 
#cloctogithubmail@gmail.com/Igivethispassfortest0506
mail_content = str(result, 'utf-8') 
#The mail addresses and password
sender_address = 'cloctogithubmail@gmail.com'
sender_pass = 'Igivethispassfortest0506'
receiver_address = destEmail
#Setup the MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'The result of the cloc scan of the github repot '+ gitrep  #The subject line
#The body and the attachments for the mail
message.attach(MIMEText(mail_content, 'plain'))
#Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
session.starttls() #enable security
session.login(sender_address, sender_pass) #login with mail_id and password
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print('Mail Sent')
'''