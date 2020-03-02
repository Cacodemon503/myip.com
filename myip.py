#!/usr/bin/python3

import sys
import time
import requests


def IP_checker():
    try:
        r = requests.get(url='https://api.myip.com')
        myip_info = r.json()
        country = myip_info['country']
        ip = myip_info['ip']
        return(country, ip)
    except:
        yellow = '\033[93m'
        endcolor = '\033[0m'
        print(f'{yellow}Please, check your internet connection{endcolor} ...')
        time.sleep(2)
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")
        sys.exit()


country, ip = IP_checker()
yellow = '\033[93m'
endcolor = '\033[0m'
print(f'''Current Location: {yellow}{country}{endcolor}
Current IP: {yellow}{ip}{endcolor}''')
