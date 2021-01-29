import RPi.GPIO as GPIO

def startcoffee():
    relay_pin = 26 # defines gpio pin for relay
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(relay_pin, GPIO.OUT) # sets pin as output
    GPIO.output(relay_pin, 1) # the 1 starts coffee machine
    print("Starting machine")

startcoffee() # calling function
