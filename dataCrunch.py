import numpy as np
import csv as csv
import sys

data = list()
#parameters: output filename, data file
#prints list to csv format
def csvWriter(path, outputData):
	with open(path, 'wb') as csvFile:
		writer = csv.writer(csvFile, delimiter = ',')
		for line in outputData:
			writer.writerow(line)


#strips key from first part of data file
def splitTables(data):
	data = filter(None, data)

	i = 0
	for row in data:
		if row[0] == "GROUP_DATA":
			groupStart = i
		if row[0] == "DETAIL_DATA":
			detailStart = i
		if row[0] == "TOTAL_DATA":
			totalStart = i
		i = i+1

	#pointers to start of each table
	print("groupStart: ", groupStart)
	print("detailStart:   ", detailStart)
	print("totalStart:   ", totalStart)

	#get first table - key
	keyTable = [data[x] for x in xrange(groupStart, detailStart)]
	detailTable = [data[y] for y in xrange(detailStart, totalStart)]
	totalTable = [data[z] for z in xrange(totalStart, len(data))]


	return keyTable, detailTable, totalTable







def main(): 


	#open data file 
	with open('detailsOfContributionsFromAssociations.csv', 'rb') as csvFile:
	    	fileReader = csv.reader(csvFile)
	    	data = [row for row in csv.reader(csvFile.read().splitlines())]


	"""
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
	"""

	tables = splitTables(data)
	
	for x in tables[1]:
		print x

	

	outputFile = 'output.csv'
	csvWriter(outputFile, data)


if __name__ == "__main__":
	main()



