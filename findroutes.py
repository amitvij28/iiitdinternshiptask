from utils import readStops,readStopTimes,readTrips

#Function to get zero and one hop routes
#Parameters: sp = starting point/stop, ep = ending point/stop
# Return Type: A dictionary containing a list of all zero and one hop routes possible 
def findroutes(sp,ep):
    stops= readStops()
    stoptrips = readStopTimes()
    triproutes  =readTrips()
    triplist = [x[0] for x in triproutes]
    routelist = [x[1] for x in triproutes]
    for s in stops:
        if sp == s['stop_name']:
            start = s['stop_id']
            break
    for s in stops:
        if ep == s['stop_name']:
            end = s['stop_id']
            break 
    
    routes={
        'zero':[],
        'one':[]
    } 
    
    listofstopsfromstart = getStartTrips(start,stoptrips,triplist,routelist)
    listofstopstoend = getEndTrips(end,stoptrips,triplist,routelist)
   
    for key in listofstopsfromstart.keys():
        if end in listofstopsfromstart[key]:
            routes['zero'].append(end)
        else:
            for sts in listofstopsfromstart[key]:
                for l in listofstopstoend.keys():
                    if sts in listofstopstoend[l]:
                        routes['one'].append({'first':key,'jump':sts,'second':l})
    return routes

#Function to get all the stops one can reach from the starting point
#Parameters: stop=Starting point/stop, trips=data from shop_times.txt, triplist=list of trips from trips.txt, routelist= list of routes from trips.txt
#Return: A dictionary which contains the route and all the stops possible to reach in that route
def getStartTrips(stop,trips,triplist,routelist):
    tripids= dict()
    for t in trips:
        if stop in t['stop_id']:
            r=routelist[int(triplist[int(t['trip_id'])])]
            lst=t['stop_id'][t['stop_id'].index(stop)+1:]
            tripids[r]=lst
    return tripids
#Function to get all the stops one can start from to reach the ending point
#Parameters: stop=Ending point/stop, trips=data from shop_times.txt, triplist=list of trips from trips.txt, routelist= list of routes from trips.txt
#Return: A dictionary which contains the route and all the stops possible in that route
def getEndTrips(stop,trips,triplist,routelist):
    tripids= dict()
    for t in trips:
        if stop in t['stop_id']:
            r=routelist[int(triplist[int(t['trip_id'])])]
            lst=t['stop_id'][:t['stop_id'].index(stop)]
            tripids[r]=lst
                

    return tripids