#!/usr/bin/env python

import RPi.GPIO as GPIO
import subprocess

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.wait_for_edge(4, GPIO.FALLING)

# Simulate ESC key press using ASCII code 27
subprocess.call(['sudo', 'sh', '-c', 'echo -ne "\\033" > /dev/input/event0'])  # Send ESC keycode directly to input device
