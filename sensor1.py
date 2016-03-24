#!/usr/bin/env python

#####################################################################
#   code developed by: austinmeier
#   developed on: 03/24/16
#   contact:austinmeier on github
#####################################################################
#                       Imports here
#####################################################################
import time
import os
from time import sleep
import RPi.GPIO as GPIO




"""
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)
GPIO.setup(25, GPIO.IN)

while True:
    if (GPIO.input(23) == False):
        os.system('mpg123 -q binary-language-moisture-evaporators.mp3 &amp;')

    if (GPIO.input(24) == False):
        os.system('mpg123 -q power-converters.mp3 &amp;')

    if (GPIO.input(25)== False):
        os.system('mpg123 -q vader.mp3 &amp;')

    sleep(0.1);
"""







#####################################################################
#                       Define functions
#####################################################################

def main():
    todaysdate = time.strftime('%m%d%Y')
    todaystime = time.strftime('%H%M')
    print("today is: %s")%todaysdate
    print("And the time is ",todaystime)









#####################################################################
#                     Put code below this
#####################################################################
#print the date (code to use for specific date return items)
print(time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime()))


main()


