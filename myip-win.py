import sys
import os
import time
import requests


def IP_checker():
    r = requests.get(url='https://api.myip.com')
    myip_info = r.json()
    country = myip_info['country']
    ip = myip_info['ip']
    return(country, ip)


def no_connect():
    try:
        yellow = '\033[93m'
        endcolor = '\033[0m'
        print(f'{yellow}Please, check your internet connection{endcolor} ...')
        time.sleep(2)
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")
    except KeyboardInterrupt:
        kill()


def kill():
    os.system('cls')
    print('Program killed by user')
    time.sleep(0.5)
    os.system('cls')
    sys.exit()


def main():
    try:
        country, ip = IP_checker()
        yellow = '\033[93m'
        endcolor = '\033[0m'
        print(f'Current Location: {yellow}{country}{endcolor}')
        print(f'Current IP: {yellow}{ip}{endcolor}')
        print('\n*Press enter for another try*')
        usr_input = input('').lower().strip(' ')
        if usr_input == ':q':
            os.system('cls')
            sys.exit()
        else:
            os.system('cls')
            main()
    except(requests.exceptions.ConnectionError):
        no_connect()
        os.system('cls')
        main()
    except KeyboardInterrupt:
        kill()


if __name__ == '__main__':
    main()
