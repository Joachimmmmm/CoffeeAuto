import RPi.GPIO as GPIO
from gpiozero import Button
from time import sleep

while True:
    button = Button(2) # assigns the gpio pin of the button
    button.wait_for_press()
    relay_pin = 26 # defines gpio pin for relay
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(relay_pin, GPIO.OUT)
    GPIO.output(relay_pin, 1) # the 1 starts coffee machine
    print("Starting coffee")
    sleep(1000) # waits 1000 seconds before stopping machine
    GPIO.output(relay_pin, 0)
    print("Stopping coffee")
    GPIO.cleanup() # clears the gpio
