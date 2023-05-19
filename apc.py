#!/usr/bin/env python3
#
# v20230517-1 hasherati
# This will prevent an APC UPS battery backup system that has an Emergency
# Power Off (EPO) port from discharging below a set threshold.
# It leverages a Raspberry Pi to 1) monitor the Battery Charge of the UPS
# and 2) trigger a relay to close via signel to GPIO pin.
# Assumes apcupsd has already been setup and that you're ok with completely
# powering down at set threshold.  This preserves life span of lead acid
# batteries by limiting the DoD (Depth of Discharge)

import os
import RPi.GPIO as GPIO
import time
import subprocess

#
# The relay that triggers the Emergency Power Off is on GPIO pin 21
#
relay = 21
#
# The relay will be off (open) in normal operation so set pin to low
#
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(relay, GPIO.OUT)
GPIO.output(relay, GPIO.LOW)
#
# Set threshold of how far to drain the battery prior to EPO shutdown
#
threshold = 85.0
#
# Query the APC UPS for it's battery charge %
#
cmd=['/usr/sbin/apcaccess -p BCHARGE | awk \'{print $1}\'']
bcharge = subprocess.check_output(cmd, shell=True)
bcharge = float(bcharge)
print("Charge state = ",bcharge,"| Threshold = ",threshold)

#
# Check the battery charge every time.sleep() until threshold is met
# and close then relay to setting GPIO pin to high.
#

while bcharge > threshold:
        time.sleep(5)
        bcharge = subprocess.check_output(cmd, shell=True)
        bcharge = float(bcharge)
        print("Charge state = ",bcharge,"| Threshold = ",threshold)
else:
        print("Charge state = ",bcharge,"| Threshold = ",threshold)
        GPIO.output(relay, GPIO.HIGH)
        print("EPO SHUTDOWN")

