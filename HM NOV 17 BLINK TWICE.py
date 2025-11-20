from machine import Pin
import time

led = Pin(15, Pin.OUT)

button = Pin(14, Pin.IN, Pin.PULL_UP) # declaring button to be a pin
# attached to pin 14 an input and a pull up resistor. dont want a floating wire

while True:
    if button.value() == 0: # Notice that this is double = this means =? instead of assignment
        print("button pressed")
        led.value(1)
        time.sleep(0.5)
        led.value(0)
        time.sleep(0.5)
        
        led.value(1)
        time.sleep(0.5)
        led.value(0)
        time.sleep(0.5)
       
