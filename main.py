import requests
import json
import sys

stop_code='0180BAC30592'

data=requests.get('https://api.github.com/events')
print(data.text)

sys.exit()

#def main(stop_code):
#    print("Welcome to BusBoard.")



#if __name__ == "__main__": main()