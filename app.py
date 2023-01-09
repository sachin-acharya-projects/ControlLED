# Communication between python and nodemcu
import urllib.request as request
from colorama import Fore, init
init(autoreset=True)

# url = "http://192.168.4.1"
url = "http://192.168.1.67/"

def sendrequest(url: str):
    req = request.urlopen(url)

def ledOn():
    sendrequest(url + "ledon")
def ledOff():
    sendrequest(url + "ledoff")
    
while True:
    print(f"{Fore.LIGHTCYAN_EX}Please INPUT [1] to TURN on the LED otherwise [0]")
    request_item = input()
    request_item = int(request_item) if request_item else 0
    try:
        if request_item == 1:
            ledOn()
            continue
        ledOff()
    except:
        pass