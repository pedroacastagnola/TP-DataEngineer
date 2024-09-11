import csv
import json


def writeCSV(dataBD):
    with open('data/data_BD.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(dataBD)

def readCSV():
    lista=[]
    with open('data/data_BD.csv', 'r',newline='') as csvfile:
        reader = csv.reader(csvfile,delimiter=',')
        for row in reader:
            if(row):
                lista=[int(i) for i in row]
    
    return lista

def readJson():
    with open("data/new_data.json", "r") as read_file:
        obj = json.load(read_file)
 
        pretty_json = json.dumps(obj, indent=2)
    return pretty_json