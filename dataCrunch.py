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

	fileName = sys.argv[1]
	with open(fileName, 'rb') as csvFile:
		fileReader = csv.reader(csvFile)
		data = [row for row in csv.reader(csvFile.read().splitlines())]


	data = filter(None, data)
	tables = splitTables(data)
	
#sort key table
	groupData = tables[0]	
	
	#header = groupData[:1]
	groupData = groupData[2:]

	groupData.sort(key = lambda row: row[0])	
	#groupData = header + groupData

#sort detailTable
	detailTable = tables[1]
	
	#header2 = detailTable[:1]
	detailTable = detailTable[2:]

	detailTable.sort(key = lambda row: row[0])
	#detailTable = hleader2 + detailTable

#match two lists
	
	finalCopy = []
	#append the tables based on Client ID
	i = 0
	for dataRow in detailTable:
		for keyRow in groupData:
			if keyRow[0] == dataRow[0]:
				joinedL = keyRow + dataRow
				print joinedL
				finalCopy.append(joinedL)


		i = i + 1






	outputFile = 'output.csv'
	csvWriter(outputFile, finalCopy)


if __name__ == "__main__":
	main()





