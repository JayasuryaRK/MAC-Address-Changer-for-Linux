#!/usr/bin/env python
import subprocess
interface = input("Enter your interface to change.. (eg.wlan0)= ")
newMAC = input("ENTER YOUR REQUESTED MAC ADDRESS >")

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether",newMAC])
subprocess.call(["ifconfig", interface, "up"])

print("=============================MAC ADDRESS CHANGED=============================")
print("If you enter valid one")