#!/usr/bin/python
import sys
import os
import shutil


# clone the repot to be scannned by cloc tool.
gitrep = sys.argv[1]
tmp = "temp-cloc-repot"
clone = "git clone --depth 1 "+ gitrep+ tmp 
os.system(clone) # Cloning

# lunch cloc
cloc = "cloc " + tmp
os.system(cloc)

#remove tmp
shutil.rmtree(tmp)