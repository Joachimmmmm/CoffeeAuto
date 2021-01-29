import RPi.GPIO as GPIO

def stopcoffee():
    relay_pin = 26 # defines the gpio pin for relay
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(relay_pin, GPIO.OUT) # sets relay pin as output
    GPIO.output(relay_pin, 0) # the 0 turns off the coffee machine
    print("Stopping machine")
    GPIO.cleanup() # clears all gpio pins used by program

stopcoffee() # calling function
