#!/usr/bin/env python

import RPi.GPIO as GPIO
import subprocess

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.wait_for_edge(4, GPIO.FALLING)

# Simulate ESC key press using ASCII code 27
with open('/dev/tty', 'wb') as tty:
    tty.write(b'\x1b')  # Write ESC character (ASCII 27)
    tty.flush()
