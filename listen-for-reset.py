#!/usr/bin/env python

import RPi.GPIO as GPIO
import subprocess

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.wait_for_edge(4, GPIO.FALLING)

# Simulate ESC key press using uinput
try:
    import uinput
    
    # Create uinput device with ESC key capability
    device = uinput.Device([uinput.KEY_ESC])
    
    # Simulate ESC key press and release
    device.emit_click(uinput.KEY_ESC)
    
except ImportError:
    print("Please install python-uinput: sudo apt-get install python-uinput")
    print("And load the uinput kernel module: sudo modprobe uinput")


