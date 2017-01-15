import numpy as np
import csv as csv


def csvWriter(path, outputData):

	with open(path, 'wb') as csvFile:
		writer = csv.writer(csvFile, delimiter = ',')
		for line in data:
			writer.writerow(line)

# open key
with open('key2004_2006.csv', 'rb') as csvKey:
    	reader = csv.reader(csvKey)
    	key = [row for row in csv.reader(csvKey.read().splitlines())]

#open data file 
with open('contFromIndividuals2004-2006.csv', 'rb') as csvFile:
    	fileReader = csv.reader(csvFile)
    	data = [row for row in csv.reader(csvFile.read().splitlines())]

#fix the date on the contributions table
for row in data:
	parsedYear = row[3][-2:]
	if parsedYear == "":
		year = ""
	else:
		year = '20' + parsedYear
	row.append(year)


#append the tables based on Client ID
for dataRow in data:
	for keyRow in key:
		if keyRow[0] == dataRow[0]:
			i = 0
			for item in keyRow:
			 dataRow.insert(i,keyRow[i])
			 i = i+1

			
outputFile = 'output.csv'

csvWriter(outputFile, data)

for row in data:
    print(row)
    #print( ",".join(row))


