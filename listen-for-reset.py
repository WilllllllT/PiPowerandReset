#!/usr/bin/env python

import RPi.GPIO as GPIO
import subprocess

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.wait_for_edge(4, GPIO.FALLING)

# Simulate ESC key press using uinput
try:
    # Use xdotool to simulate ESC key press
    subprocess.call(['xdotool', 'key', 'Escape'])
except FileNotFoundError:
    print("Please install xdotool: sudo apt-get install xdotool")


