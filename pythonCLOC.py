#!/usr/bin/python
import sys
import os
import shutil
import subprocess
import smtplib
tmp = "temp-cloc-repot"
cloc = "cloc " + tmp
isExist = os.path.isdir(tmp)

#check if the temp repot file exist
if isExist:
    #os.system(cloc)
    result = subprocess.check_output(cloc)
    print(result)

else:
    # clone the repot to be scannned by cloc tool.
    gitrep = sys.argv[1]
    clone = "git clone --depth 1 "+ gitrep+ " " +  tmp 
    os.system(clone)
    
    # lunch cloc
    #os.system(cloc)
    result = subprocess.check_output(cloc)
    print(result)

#send result to  email
s=smtplib.SMTP('localhost')
s.sendmail("halidsanfo@gmail.com", "halidsanfo@gmail.com", "the cloc scan result : "+result)