import csv
import sys

#This program was written in Python 3.6.3 by Henry Caushi. You are free to use it for any reason, without my permission, without having to inform myself or anyone else
#This program was was written to aid other programs, by providing a list of all event IDs so that they appear only once


#List of all event IDs
list_ids = []

filename = "Higgs_Hunters_data_ALL.csv"

#Open the data file
f = open(filename+,"r")
reader = csv.reader(f)
for row in reader:
    #If an event ID is not already added to the list, add it to the list
    if row[3] not in list_ids:
        list_ids.append(row[3])
f.close()

#Open a new file, and dump the event IDs
f = open("List IDs.txt","w")
for row in list_ids:
    f.write(row+"\n")
f.close()
