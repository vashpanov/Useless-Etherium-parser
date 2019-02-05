# coding = utf8
# author Panghu.Xiao 
import requests
import re
import csv
from datetime import datetime
from pyquery import PyQuery as pq
source = "general.csv"
path = "general_output.csv"
table=[]
link_table =[]
a=0
with open(source, "r", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        try:
            print(a)
            domain = "https://etherscan.io/token/"+row[0]+"#tokenInfo"
            tb = (pq(domain)("#tokenInfo > div:nth-child(1) > div:nth-child(1)").text().split("\n"))
            descricption = tb[1]
            web =(pq(domain)("#ContentPlaceHolder1_tr_officialsite_1 > td:nth-child(2)").text())
            pad = (str(pq(domain)(".list-inline")).split("\""))
            link_table=[]
            link_table.append(descricption)
            link_table.append(web)
            for i in pad:
                if "http" in i:
                    i=i.split(": ")
                    if not str(i[-1]) in link_table:
                        link_table.append(str(i[-1]))
            table.append(link_table)
            a+=1

        except:
            link_table.append(" ")
            table.append(link_table)
            continue



def csv_writer(data, path):

    with open(path, "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)


data = table
open(path)
csv_writer(data, path)