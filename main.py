import requests
import json
import sys

stop_code='0180BAC30592'

#class Bus:
#    def __init__(self, atco,sms,request_time,name,stop_name,bearing,indicator):
#        self.date = date
#        self.from_account = acc_from
#        self.to_account = acc_to
#        self.narrative = narrative
#        self.amount = amount
#
#    def __repr__(self):
#        return f"""********************************************
#        Date: {self.date}
#        From: {self.from_account}
#        To: {self.to_account}
#        Narrative: {self.narrative}
#        Amount: £{self.amount}"""

#    def export(self):
#        return [self.date, self.from_account, self.to_account, self.narrative, self.amount]

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
    URL=URL+"&group=no&limit=5&nextbuses=yes"
    bus_data=requests.get(URL)
    bus_data=bus_data.json()
    output_data=[]
    for key in bus_data:
        if key == 'departures':
            print(bus_data[key])


    sys.exit()

main(stop_code,AppID,Key)
#if __name__ == "__main__": main()