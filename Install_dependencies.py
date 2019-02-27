# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 14:25:24 2019

@author: manik
"""

#importing all the required packages
from pyparsing import nestedExpr
import subprocess
import sys

#read the json file
with open('a.json') as f:
     data=f.read()
     
#parsing the curly braces
s=nestedExpr('{','}').parseString(data).asList()

#slicing the libraries in the list
libraries=s[0][2]

#creating empty list to add failed libraries
list1=[]

#install the packages
for package in libraries:
    d=subprocess.call([sys.executable, "-m", "pip", "install", package])
    #checking whether packages is installed or not
    if d!=0:
        list1.append(package)

#checking whether any packages failed to install        
if len(list1)==0:
         print('SUCCESS')
else:
     for package in list1:
         print(package)         
        
    