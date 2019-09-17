import requests
import json
import sys
import argparse

parser = argparse.ArgumentParser(description='Script to generate website based on bus data')
parser.add_argument('-p','--postcode', help='Valid UK postcode', required=False)
args = parser.parse_args()
write=False

class Bus_data:
    def __init__(self, line_name, direction, operator, departure_time):
        self.line_name = line_name
        self.direction = direction
        self.operator = operator
        self.departure_time = departure_time

    def __repr__(self):
        return f"""\n
        Line Number: {self.line_name}
        To: {self.direction}
        Operated By: {self.operator}
        Expected Departure: {self.departure_time}\n"""

def BusStopFinder(postcode,AppID,Key,required_stops):
    URL = "https://api.postcodes.io/postcodes?q=" + postcode
    postcode_data = requests.get(URL)
    postcode_data = postcode_data.json()
    postcode_data = postcode_data['result'][0]
    longitude=str(postcode_data['longitude'])
    latitude=str(postcode_data['latitude'])
    URL = "https://transportapi.com/v3/uk/places.json?app_id="+AppID+"&app_key="+Key+"&lat="+latitude+"&lon="+longitude
    URL = URL + "&type=bus_stop"
    bus_stops=requests.get(URL)
    bus_stops=bus_stops.json()
    bus_stops=bus_stops['member']
    stop_codes=[]
    for x in range(0,required_stops):
        item=[]
        stop=bus_stops[x]
        stop_code=stop['atcocode']
        stop_name=stop['name']
        item.append(stop_code)
        item.append(stop_name)
        stop_codes.append(item)
    return stop_codes

def main(stop_code, AppID, Key,group_key,limit):
    URL='https://transportapi.com/v3/uk/bus/stop/'+stop_code+"/live.json?app_id="+AppID+"&app_key="+Key
    URL=URL+"&group="+group+"&limit="+limit+"&nextbuses=no"
    bus_data=requests.get(URL)
    bus_data=bus_data.json()
    bus_data=bus_data['departures'][group_key]
    for bus in bus_data:
        line_name=bus['line_name']
        direction = bus['direction']
        operator = bus['operator']
        departure_time = bus['best_departure_estimate']
        bus_entry=Bus_data(line_name,direction,operator,departure_time)
        if write == True:
            with open(outfile,'a') as out:
                out.write(str(bus_entry))
        else:
            print(bus_entry)

if args.postcode == None:
    postcode=input("Please enter a valid UK postcode")
else:
    postcode=args.postcode
    write=True

group='no'
limit='5'
group_key='all'
required_stops=2
if write == True:
    outfile=postcode+".txt"
    with open(outfile,'w') as out:
        out.write("BUS INFORMATION FOR THE NEAREST "+str(required_stops)+" BUS STOPS TO "+postcode+"\n\n")
    out.close()

KeyInfo_file=open("TransportAPIKey.txt",'r')
KeyInfo=[]
for line in KeyInfo_file:
    line=line.split(':')
    KeyInfo.append(line[1])
KeyInfo_file.close()
AppID=KeyInfo[0]
AppID=AppID[1:-1]
Key=KeyInfo[1]
Key=Key[1:]

try:
    stop_codes=BusStopFinder(postcode,AppID,Key,required_stops)
except TypeError:
    print("Error! The provided postcode does not exist.")
    sys.exit()

for item in stop_codes:
    stop_code=item[0]
    stop_name=item[1]
    if write == True:
        with open(outfile,'a') as out:
            out.write("\n")
            out.write("**************************************************\n")
            out.write(stop_name+"\n")
            out.write("**************************************************\n")
        out.close()
    else:
        print("\n")
        print("Data for bus stop "+stop_name+": (ATCO code "+stop_code+")")
    try:
        main(stop_code,AppID,Key,group_key,limit)
    except KeyError:
        print("Error! Bus data is not available for stop: "+stop_name)