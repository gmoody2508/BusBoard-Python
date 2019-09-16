import requests
import json
import sys

stop_code='0180BAC30592'

#data=requests.get('https://api.github.com/events')

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
print(AppID)
print(Key)

def main(stop_code, AppID, Key):
    print("Welcome to BusBoard.")
    URL='https://transportapi.com/v3/uk/bus/stop/'
    URL=URL+stop_code
    URL=URL+"/live.json?app_id="
    URL=URL+AppID
    URL=URL+"&app_key="
    URL=URL+Key
    URL=URL+"&group=route&limit=5&nextbuses=yes"
    print(URL)
    bus_data=requests.get(URL)
    print(bus_data)
    bus_data=bus_data.json()
    print(bus_data)
    sys.exit()

main(stop_code,AppID,Key)
#if __name__ == "__main__": main()