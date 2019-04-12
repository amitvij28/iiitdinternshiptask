from utils import readStops,readStopTimes,readTrips
import sys


def workondata(sp,ep):
    stops = readStops()
    trips = readStopTimes()
    for s in stops:
        if sp == s['stop_name']:
            start = s['stop_id']
            break
    for s in stops:
        if ep == s['stop_name']:
            end = s['stop_id']
            break
    #print(start +" "+end,file=sys.stdout)
    #zero hop ----------------------------------------------------
    possibletrips = []
    for t in trips:
        try:
            si = t['stop_id'].index(start)
            ei =t['stop_id'].index(end)
            if  si<=ei:
                possibletrips.append(t['trip_id'])
        except:
            pass
        
    possibleroutes=[]
    triproute = readTrips()
    tripss = [x[0] for x in triproute]
    routess = [x[1] for x in triproute]
    # print(tripss)
    # print(routess)
    for t in possibletrips:
        i = tripss.index(t)
        r = routess[i]
        if r not in possibleroutes:
            possibleroutes.append(r)

    return possibleroutes