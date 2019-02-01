# coding = utf8
# author Panghu.Xiao 

import csv
from pyquery import PyQuery as pq
domain = "https://etherscan.io/"
table=[]
for page in range(1, 18):
    index_url = (domain+"tokens?p="+str(page))
    print(page)
    for i in range(1, 51):
        tr = []
        name = pq(index_url)(".table > tbody:nth-child(2) > tr:nth-child(%i) > td:nth-child(3) > h5:nth-child(1)" % i).text()
        token_log = name.split('(')[1].replace(')', '')
        token_name = name.replace('('+token_log+')', '')
        token_name = token_name[:-1]
        price = (pq(index_url)(".table > tbody:nth-child(2) > tr:nth-child(%i) > td:nth-child(5) > span:nth-child(1)" % i).text())
        change = (pq(index_url)(".table > tbody:nth-child(2) > tr:nth-child(%i) > td:nth-child(6)" % i).text())
        address = pq(index_url)(".table > tbody:nth-child(2) > tr:nth-child(%i) > td:nth-child(3) > h5:nth-child(1)" % i).html().split('"')[1].replace('/token/', '')
        volume = (pq(index_url)(".table > tbody:nth-child(2) > tr:nth-child(%i) > td:nth-child(7)" % i).text())
        capitalization = (pq(index_url)(".table > tbody:nth-child(2) > tr:nth-child(%i) > td:nth-child(8)" % i).text())
        tr.append(token_log)
        tr.append(token_name)
        tr.append(address)
        tr.append(price)
        tr.append(change)
        tr.append(volume)
        tr.append(capitalization)
        table.append(tr)


def csv_writer(data, path):

    with open(path, "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)

data = table
path = "output.csv"
csv_writer(data, path)

