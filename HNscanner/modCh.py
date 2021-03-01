#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2/22/21 2:35 PM
#@Author: Haoxin Shi
#@File  : modCh.py

import socket
import os
import requests
import platform
import execjs
import json
import outputall

def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def banner():
    print("""\033[96m
 1) DNS Lookup                 13) Host DNS Finder
 2) Whois Lookup               14) Reserve IP Lookup
 3) GeoIP Lookup               15) Email Gathering (use Infoga)
 4) Subnet Lookup              16) Subdomain listing (use Sublist3r)
 5) Port Scanner               17) Find Admin login site (use Breacher)
 6) Page Links                 18) Check and Bypass CloudFlare (use HatCloud)
 7) Zone Transfer              19) Cloud Ip Range Detection
 8) HTTP Header                20) Host Info Scanner (use WhatWeb)
 9) Host Finder                21) Cloud App Detection
 10) IP-Locator                22) Banner grabbing
 11) Find Shared DNS Servers   23) Exit
 12) Get Robots.txt""")
    print()


def iseeverything(what, choose, victim):
    print('\033[91m',what,choose,victim)
    try:
        #what = input('\033[92mDo you want to collect information of a website or IP address? [website/IP]: ')
        if what[0].upper() == 'W':
            victim = input('Enter the website address: ')
            #banner()
        elif what[0].upper() == 'I':
            #victim = input('Enter the IP address (or domain to get IP address of that domain): ')
            victim = socket.gethostbyname(victim)
            print('The IP address of target is:', victim)
            #banner()
        else:
            #print('?')
            iseeverything()

        #choose = input('What information would you like to collect? (1-20): ')

        if choose == '1':
            dnslook = 'https://api.hackertarget.com/dnslookup/?q=' + victim
            info = requests.get(dnslook)
            print('\033[91m', info.text)


        elif choose == '2':
            whois = 'https://api.hackertarget.com/whois/?q=' + victim
            info = requests.get(whois)
            print('\033[91m', info.text)
            

        elif choose == '3':
            ipgeo = 'https://api.hackertarget.com/geoip/?q=' + victim
            info = requests.get(ipgeo)
            print('\033[91m', info.text)
            #

        elif choose == '4':
            subnet = 'http://api.hackertarget.com/subnetcalc/?q=' + victim
            info = requests.get(subnet)
            print('\033[91m', info.text)
            

        elif choose == '5':
            port = 'https://api.hackertarget.com/nmap/?q=' + victim
            info = requests.get(port)
            print('\033[91m', info.text)
            

        elif choose == '6':
            pagelink = 'https://api.hackertarget.com/pagelinks/?q=' + victim
            info = requests.get(pagelink)
            print('\033[91m', info.text)
            

        elif choose == '7':
            zone = 'https://api.hackertarget.com/zonetransfer/?q=' + victim
            info = requests.get(zone)
            print('\033[91m', info.text)
            

        elif choose == '8':
            header = 'https://api.hackertarget.com/httpheaders/?q=' + victim
            info = requests.get(header)
            print('\033[91m', info.text)
            

        elif choose == '9':
            host = 'https://api.hackertarget.com/hostsearch/?q=' + victim
            info = requests.get(host)
            print('\033[91m', info.text)
            

        elif choose == '10':
            iplt = 'https://ipinfo.io/' + victim + '/json'
            info = requests.get(iplt)
            print('\033[91m', info.text)
            outputall.outputall(info.text)
            

        elif choose == '11':
            shared = 'https://api.hackertarget.com/findshareddns/?q=' + victim
            info = requests.get(shared)
            print('\033[91m', info.text)
            

        elif choose == '12':
            robots = 'http://' + victim + '/robots.txt'
            info = requests.get(robots)
            print('\033[91m', info.text)
            

        elif choose == '13':
            hostdns = 'https://api.hackertarget.com/mtr/?q=' + victim
            info = requests.get(hostdns)
            print('\033[91m', info.text)
            

        elif choose == '14':
            reserve = 'https://api.hackertarget.com/reverseiplookup/?q=' + victim
            info = requests.get(reserve)
            print('\033[91m', info.text)
            

        elif choose == '15':
            clear()
            os.system('cd modules/Infoga && python3 infoga.py --domain ' + victim)
            

        elif choose == '16':
            clear()
            os.system('cd modules/Sublist3r && python3 sublist3r.py -d ' + victim)
            

        elif choose == '17':
            clear()
            os.system('cd modules/Breacher && python breacher.py -u ' + victim)
            

        elif choose == '18':
            clear()
            os.system('ruby ./modules/HatCloud/hatcloud.rb -b ' + victim)
            

        elif choose == '19':
            os.system('cd websource && mkdir ' + victim)
            os.system('cd websource && cd ' + victim + ' && httrack ' + victim)
            print("The website source code was saved in folder 'websource'")
            

        elif choose == '20':
            clear()
            os.system('whatweb -v ' + victim)
            

        elif choose == '21':
            print("""\033[ Information Gathering of a Website or IP address

AUTHOR: Haoxin Shi""")
            

        # elif choose == '22':
        #     reserve = 'https://api.hackertarget.com/bannerlookup/?q=' + victim
        #     info = requests.get(reverse)
        #     print('\033[91m', info.text)
        #     

        elif choose == '23':
            exit

        else:
            print('?')
            #iseeverything('ip', '3', '91.226.26.62')

    except socket.gaierror:
        print('Name or service unknown!\033[93m')


    except UnboundLocalError:
        print('The information you entered is incorrect')


    except requests.exceptions.ConnectionError:
        print('Your Internet Offline')
        exit
    except IndexError:
        print('?')



#iseeverything('ip', '3', '91.226.26.62')
