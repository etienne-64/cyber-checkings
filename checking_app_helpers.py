import os
import platform
from colorama import Fore, Back, Style
import pycurl
from io import BytesIO
import subprocess
import json
from collections import Counter

def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def menu_display():
    print(Style.BRIGHT + Back.GREEN + " === MENU === " + Style.RESET_ALL + "\n")
    print("(1) Get infos on my external ip")
    print("(2) Get infos on list of ip (from file: one ip / line)")
    print("(3) Analyse Apache access.log")
    print("(4) ")

    print("(0) Exit\n")

def get_my_ip():
    my_ip = subprocess.check_output(['curl','-s','ifconfig.me/ip'])
    return my_ip.decode('utf-8')


def get_ip_info(ip):
    b_obj = BytesIO()
    request = pycurl.Curl()

    request.setopt(request.URL, f'https://ipapi.co/{ip}/json')
    request.setopt(request.WRITEDATA, b_obj)
    request.perform()
    request.close()
    request_body = b_obj.getvalue().decode('utf8')

    ip_info = json.loads(request_body)
    return ip_info


def get_apache_log_info(file_path)->Counter:
    apache_log_infos = None
    ips = []
    # curl_log=$(cat $LOG_FILE | grep $ip | cut -d"\"" -f2 | cut -d" " -f2 | cut -d'/' -f2 | sort | uniq -c | sort -nr)
    with open(file_path, "r") as f:
        while True:
            line = f.readline()
            if line:
                tokens = line.split()
                ips.append(tokens[0])
            else:
                break
    return Counter(ips)