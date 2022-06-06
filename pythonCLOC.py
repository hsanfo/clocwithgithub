#!/usr/bin/python
import sys
import os
import subprocess
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


#****************HELP*****************#
import argparse

parser=argparse.ArgumentParser(
    description='''Script to scan a gitub source repository and send the ouput to an email ''',
    epilog="""**************END*************.""")

parser.add_argument('repo', default='https://github.com/hsanfo/clocwithgithub.git', help='GITHUB URL IN HTTPS!')
parser.add_argument('email', default='cloctogithubmail@gmail.com', help='CLOC scan result will be sent to this Email adress!')
args=parser.parse_args()

#****************HELP*****************#

tmp = "temp-cloc-repot"
cloc = "cloc " + tmp
isExist = os.path.isdir(tmp)

#check if the temp repot file exist
gitrep = args.repo #sys.argv[1]
destEmail = args.email # sys.argv[2]
if isExist:
    #os.system(cloc)
    result = subprocess.check_output(cloc,shell=True, stderr=subprocess.STDOUT)
    print(result)

else:
    # clone the repot to be scannned by cloc tool.
    
    clone = "git clone --depth 1 "+ gitrep+ " " +  tmp 
    os.system(clone)
    
    # lunch cloc
    #os.system(cloc)
    result = subprocess.check_output(cloc,shell=True, stderr=subprocess.STDOUT)
    print(result)
#os.system("python -m smtpd -n -c DebuggingServer localhost:1025")
#send result to  email
s=smtplib.SMTP(host='localhost', port=1025)
s.sendmail("halidsanfo@gmail.com", destEmail, "the cloc scan result : "+str(result, 'utf-8') )
s.quit()


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