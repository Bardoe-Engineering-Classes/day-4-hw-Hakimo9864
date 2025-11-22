1. Explain in writing why pull-up resistors are needed to power an LED.


Background: A pull-up resistor is a resistor in which connects a microcontroller input pin to a 3.3 V or 5 V so that the pin has a high value if nothing is connected (Like a default value)


Why We need them:

    
Micro-controller input pins are sensitive (Raspberry Pi Pico) thus if an input pin has nothing connected it will randomize whether it will read High/Low voltage and randomize values if the button isn’t even Pressed.

 -  This causes unpredictable behaviour.


Pull-up resistors fix this by giving the pin a stable default state of HIGH voltage. 


People call this floating if the pin doesn’t have a default state thus the pull up resistor is needed.
