#!/usr/bin/env python

import RPi.GPIO as GPIO
import subprocess

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.wait_for_edge(4, GPIO.FALLING)

# Simulate ESC key press using keyboard events
try:
    # Write ESC key code directly to input device
    with open('/dev/input/event0', 'wb') as f:
        # ESC key code is 1
        f.write(bytes([0x01, 0x00, 0x00, 0x00])) 
except PermissionError:
    print("Error: Need root permissions to simulate keyboard events")


