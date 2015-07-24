#!/usr/bin/python
import os
import shutil
from bs4 import BeautifulSoup
import csv

url = "http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_lotfac.zip"
lotto_zip = 'D_lotfac.zip'
html_file = '/home/ptrierweiler/Documents/lotto/data/D_LOTFAC.HTM'
csv_file = open('/home/ptrierweiler/Documents/lotto/lotofacil.csv','w')

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

#Parse the html file
html = open(html_file,'r')
soup = BeautifulSoup(html, 'html.parser')

html_list = []
for i in soup.find_all('td'):
    line = str(i)
    if '<td rowspan="' in line:
        html_list.append(line)

raw_text = soup.get_text()

html_dict = {}
x = 0
for i in raw_text.split():
    x = x + 1
    tmp_dict = {x:i}
    html_dict.update(tmp_dict)

date_list = []
for i in html_dict:
    v = html_dict[i]
    if '/' in v:
        date_list.append(i)

master_list = []
for d in date_list:
    sd = int(d) -1
    ed = sd + 17
    tmp_list = []
    for d in range(sd,ed):
        v = html_dict[d]
        tmp_list.append(v.strip())
    master_list.append(tmp_list)

def date_func(i):
    nw = i.split('/')[2] + '-' + i.split('/')[1] + '-' + i.split('/')[0]
    return nw

def num_func(i):
    if 'Valor' in i:
        return 1
    else:
        return i

writer = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
writer.writerows(['game','date','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'])
for i in master_list:
    num = num_func(i[0])
    date = date_func(i[1])
    n1 = i[2]
    n2 = i[3]
    n3 = i[4]
    n4 = i[5]
    n5 = i[6]
    n6 = i[7]
    n7 = i[8]
    n8 = i[9]
    n9 = i[10]
    n10 = i[11]
    n11 = i[12]
    n12 = i[13]
    n13 = i[14]
    n14 = i[15]
    n15 = i[16]
    #print num,date,n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12,n13,n14,n15
    writer.writerows([ num,date,n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12,n13,n14,n15])
