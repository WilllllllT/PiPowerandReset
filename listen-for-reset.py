#!/usr/bin/env python

import RPi.GPIO as GPIO
import subprocess
from evdev import UInput, ecodes

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    # Wait for button press
    GPIO.wait_for_edge(4, GPIO.FALLING)
    
    # Create a virtual keyboard device
    with UInput() as ui:
        # Simulate pressing and releasing ESC key
        ui.write(ecodes.EV_KEY, ecodes.KEY_ESC, 1)  # Press ESC
        ui.write(ecodes.EV_KEY, ecodes.KEY_ESC, 0)  # Release ESC
        ui.syn()
    
finally:
    # Clean up GPIO on exit
    GPIO.cleanup()
