"""
Name: Program_01_OneLEDBlink.py
Purpose: Turn On and Off one LED in a loop 

Requirements: Micropython and ESP32 board

"""

from machine import Pin
from time import sleep_ms

p32 = Pin(16, Pin.OUT)

print("Starting loop, use Ctrl-C to break out.")
while(True):
    try:
        p32.on()
        sleep_ms(500)  # Sleep for 500 milliseconds
        p32.off()
        sleep_ms(500)
    except KeyboardInterrupt: # Ctrl-C to come out of loop
        print("User Interruption, exiting loop")
        break
    
