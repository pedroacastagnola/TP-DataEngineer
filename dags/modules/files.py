import csv


def writeCSV(dataBD):
    with open('data/data_BD.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(dataBD)

def readCSV():
    with open('data/data_BD.csv', 'r',newline='') as csvfile:
        reader = csv.reader(csvfile,delimiter=',')
        for row in reader:
            if(row):
                return row