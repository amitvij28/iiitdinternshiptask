import os

#read stops.txt for dropdown data
def readStops():
    f  = open('./data/stops.txt','r')
    stopslist = []
    f.readline()
    for line in f:
        line=line.split(',')
        stop={}
        stop['stop_id']=line[0]
        stop['stp_code']=line[1]
        stop['stop_name']=line[2]
        stopslist.append(stop)
    f.close()
    return stopslist

def readStopTimes():
    f = open('./data/stop_times.txt','r')
    trips = []
    f.readline()
    prev='-1'
    trip={}
    for line in f:
        values = line.split(',')
        if values[0]!=prev:
            prev=values[0]
            trips.append(trip)
            trip={}
            trip['trip_id']=values[0]   
            trip['stop_id']=[values[3]]
        else:
            trip['stop_id'].append(values[3])
    f.close()
    del trips[0]
    return trips

def readTrips():
    f=open('./data/trips.txt','r')
    trips = []
    f.readline()
    for line in f:
        values = line.split(',')
        t = []
        t.append(values[2].split('\n')[0])
        t.append(values[0])
        trips.append(t)

    f.close()
    return trips