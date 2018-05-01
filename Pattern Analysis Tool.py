#Please be gentle to me; I was working on this from about 3:00 and it took me until 00:49 to solve a logical issue where most of the clusters would be removed when attempting to weld clusters!

import csv
import sys

#This program was written in Python 3.6.3 by Henry Caushi. You are free to use it for any reason, without my permission, without having to inform myself or anyone else
#This program was developed in order to identify patterns and clusters of clicks. That is, it tries to work out whether there are just two points where everyone has clicked, or whether users were more uncertain about the number of clicks
#There are numerous ways to use the data for this program. For example, you could use data mining to figure out the regression of lines, you could see which clicks were the most obvious to click on, or even work out the mean average of clusters to derive results
#Note that, to run this program, you need a CSV file with data to mine. The default filename is provided below: simply put it in the same folder as this file

filename = "Higgs_Hunters_data_ALL.csv"

#Good luck!

def get_distance(dx,dy):
    #Obtain a Pythagorean distance given two perpendicular components.
    distance = dx**2 + dy**2
    distance = distance ** 0.5
    return distance

class Event:
    #An event is defined as a single incidence of two or more particles
    all_events = {}

    def __init__(self, event_id):
        self.all_clicks = []                                            #List of all clicks associated with the event
        self.click_clusters = {"RZzoom": [], "XY": [], "XYzoom": []}    #A dictionary is used here to separate events by cluster (single lines or points of clicks) and by projection
        Event.all_events[event_id] = self                               #Add the event to a list of all events

class Click:
    #A click is defined as a user-identified decay point
    def __init__(self, event_id, x, y, no_tracks, projection):
        Event.all_events[event_id].all_clicks.append(self)
        self.x = x
        self.y = y
        self.no_tracks = no_tracks

        #List of clusters in which this click would belong
        matched_clusters = []
        
        #Decide which cluster to put the click into: if
        #If
        for cluster in Event.all_events[event_id].click_clusters[projection]:
            for click in cluster:
                if get_distance(x-click.x,y-click.y) <= 40:             #"40" Determines the radius of tolerance: if there is no click inside this radius, a new cluster will be formed
                    if Event.all_events[event_id].click_clusters[projection].index(cluster) not in matched_clusters:
                        matched_clusters.append(Event.all_events[event_id].click_clusters[projection].index(cluster))
        
        #If the cluster would fit into only one cluster, put it in there
        #Otherwise, weld the clusters into one cluster
        if len(matched_clusters) == 1:
            Event.all_events[event_id].click_clusters[projection][matched_clusters[0]].append(self)

        elif len(matched_clusters) > 1:
            new_cluster = [self]
            for cluster in matched_clusters[::-1]:
                new_cluster += Event.all_events[event_id].click_clusters[projection].pop(cluster)

            Event.all_events[event_id].click_clusters[projection].append(new_cluster)            

        else:
            Event.all_events[event_id].click_clusters[projection].append([self])

#Load all clicks from file
f = open(filename,"r")
reader = csv.reader(f)
for row in reader:
    try:
        Event.all_events[row[3]]
        Click(row[3],float(row[5]),float(row[6]),row[7],row[11])
    except:
        Event(row[3])
        try:
            Click(row[3],float(row[5]),float(row[6]),row[7],row[11])
        except:
            print("Error")

#To test that the above code has worked, try the following code
#Event.all_events["AHH0000iyx"].click_clusters

f.close()

#Obtain a list of event IDs
f = open("Big Data Mod 1.txt","r")
event_ids = f.readlines()
f.close()

#Save all data to a new file
for projection in ["XY","XYzoom","RZzoom"]:
    f = open(projection+".txt","w")
    
    for event_id in event_ids:
        event_id = event_id.strip()
        cluster_sizes = []
        for cluster in Event.all_events[event_id].click_clusters["XYzoom"]:
            cluster_sizes.append(len(cluster))
        string = str(event_id)+": "+str(len(Event.all_events[event_id].click_clusters["XYzoom"]))+" ("
        for cluster_size in cluster_sizes:
            string += str(cluster_size)+", "
        string = string[:-2:]
        string += ")"
        f.write(string+"\n")

    f.write
        
    f.close()
