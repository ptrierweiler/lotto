#!/usr/bin/python
import os
import shutil

url = "http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_lotfac.zip"
lotto_zip = 'D_lotfac.zip'
#Chaning Direction
os.chdir('/home/ptrierweiler/Documents/lotto')

#checking for zip file and deleting if exists
if os.path.isfile(lotto_zip) == True:
    print "Deleting previous vertion of " + lotto_zip + "\n"
    os.remove(lotto_zip)

#checking for data directory and deleting if exists
if os.path.isdir("data") == True:
    shutil.rmtree("data")

#downloading file using wget
#should figure out how via python
os.system("wget {url}".format(url = url))

#unziping data to data directory
#should figure out using python
os.system("unzip {zip} -d data".format(zip = lotto_zip))

os.chdir('/home/ptrierweiler/Documents/lotto/data')


#unzip
