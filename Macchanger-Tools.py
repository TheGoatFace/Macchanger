import os
import subprocess
import time
import random

print('''
    __  __             _____ _                                 
   |  \/  |           / ____| |                                
   | \  / | __ _  ___| |    | |__   __ _ _ __   __ _  ___ _ __ 
   | |\/| |/ _` |/ __| |    | '_ \ / _` | '_ \ / _` |/ _ \ '__|
   | |  | | (_| | (__| |____| | | | (_| | | | | (_| |  __/ |   
   |_|  |_|\__,_|\___|\_____|_| |_|\__,_|_| |_|\__, |\___|_|   
                                                __/ |          
                                                |___/  
   Idan-Tal || Macchanger || Have Fun!!
   ''')
print('''                                       
       [1] Change mac address to random. (macchanger -r eth0)
       [2] Show us to our status of Mac Address. (macchanger -s eth0)
       [3] Change the mac address to one company address. (macchanger -a eth0)
       [4] Return our original mac address. (macchanger -p eth0)
       [5] Set a specific Mac Address. (macchanger -m XX:XX:XX:XX:XX:XX eth0)
       [6] Find a MAC address prefix. (macchanger -l)
       #########################################################################
       [7] Interface Down. (ifconfig eth0 down)
       [8] Interface Up. (ifconfig eth0 up)
   ''')

Mac_input = int(input("Type what command you want to execute: "))


def macchanger_random():
    if Mac_input == 1:
        try:
            for mac in os.popen("macchanger \t" + "-r" "\t" "eth0"):
                print(f"{mac}")

            print(f"This works!, New MAC Address is {mac}")

        except:
            print("Someting wrong with Macchanger!! check this:)")


print("\n")


def macchanger_status():
    if Mac_input == 2:
        try:
            for mac in os.popen("macchanger \t" + "-s" "\t" "eth0"):
                print(f"{mac}")

            print(f"This works!, The {mac}")

        except:
            print("Someting wrong with Macchanger!! check this:)")

def macchanger_company():
    if Mac_input == 3:
        try:
            for mac in os.popen("macchanger \t" + "-a" "\t" "eth0"):
                print(f"{mac}")

            print(f"This works!, The {mac}")

        except:
            print("Someting wrong with Macchanger!! check this:)")

def macchanger_original():
    if Mac_input == 4:
        try:
            for mac in os.popen("macchanger \t" + "-p" "\t" "eth0"):
                print(f"{mac}")

            print(f"This works!, The {mac}")

        except:
            print("Someting wrong with Macchanger!! check this:)")

def macchanger_specific():
    if Mac_input == 5:
        mac_m = input("Enter your Mac Addres u want: ")
        try:
            for mac in os.popen("macchanger \t" + "-m" "\t" + mac_m + "\t" + "eth0"):
                print(f"{mac}")

            print(f"This works!, The {mac}")

        except:
            print("Someting wrong with Macchanger!! check this:)")

def macchanger_list_of_prefix():
    if Mac_input == 6:
        try:
            for mac in os.popen("macchanger \t" + "-l" "\t" "eth0"):
                print(f"{mac}")

            print(f"This works!, The {mac}")

        except:
            print("Someting wrong with Macchanger!! check this:)")

def Inteface_Down():
    if Mac_input == 7:
        try:
            for mac in os.popen("ifconfig" "\t" + "eth0" "\t" "down"):
                print(f"{mac}")

            print(f"This works!, The {mac}")

        except:
            print("Someting wrong with Macchanger!! check this:)")

def Interface_Up():
    if Mac_input == 8:
        try:
            for mac in os.popen("ifconfig" "\t" + "eth0" "\t" "up"):
                print(f"{mac}")

            print(f"This works!, The {mac}")

        except:
            print("Someting wrong with Macchanger!! check this:)")

macchanger_random()
macchanger_status()
macchanger_company()
macchanger_original()
macchanger_specific()
macchanger_list_of_prefix()
Inteface_Down()
Interface_Up()