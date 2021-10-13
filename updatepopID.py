#!/usr/bin/python

"""
May 2015

Gulsah

Usage: updatepopID.py *.pedind *.ped > *.new.ped

"""


import sys

filein = open(sys.argv[1], 'r')
filein2 = open(sys.argv[2], 'r')


popDict = {}

for line in filein:

        fields=line.split()
	
	popDict[fields[1]] = fields[5]


for line in filein2:

	fields2 = line.split()
	sampleID = fields2[1]

	if sampleID in popDict:

		popID = popDict[sampleID]
		line = line.replace(fields2[5],popID)
		sys.stdout.write(line)
