#!/usr/bin/env python3

from colorama import Fore, Back, Style
from checking_app_helpers import clear_screen, menu_display, get_my_ip, get_ip_info,get_apache_log_info, get_failed_login


if __name__ == '__main__':

    while True:
        clear_screen()
        menu_display()
        app_option = input(Style.BRIGHT + "Votre choix: " + Style.RESET_ALL)

        if app_option == '1':
            my_ip = get_my_ip()
            ip_info = get_ip_info(my_ip)
            print(f"ip: {ip_info['ip']} - country: {ip_info['country_name']} - city: {ip_info['city']}")
            input("")
        elif app_option == '2':
            ip_list = None
            with open('notes/ip-list.txt', "r") as f:
                ip_list = f.readlines()

            for ip in ip_list:
                ip_info = get_ip_info(ip.rstrip())
                print(f"ip: {ip_info['ip']} - country: {ip_info['country_name']} - city: {ip_info['city']}")

            input("")
        elif app_option == '3':
            counter = get_apache_log_info("./notes/vps_access.log")
            counter_podium = counter.most_common()

            for (ip,rank) in counter_podium:
                # print(ip, counter[ip])
                ip_info = get_ip_info(ip)
                print(f"rank: {counter[ip]} - ip: {ip_info['ip']} - country: {ip_info['country_name']} - city: {ip_info['city']}")

            input("")
        elif app_option == '4':
            pass
            get_failed_login()
        else:
            print("Bye !")
            break

