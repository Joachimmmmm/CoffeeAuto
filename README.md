# CoffeeAuto
Using a relay and raspberry pi in order to turn a coffee machine off and on at given times

file 'buttoncoffeestart.py' is responsible for activating the coffee machine through a relay which turns on when a button is pressed, then automatically turns off in 1000 seconds - an infinite program  that runs in the background so can be turned on at any time in day.

file 'startcoffee.py' is responsible for starting the coffee machine at any specified time in works with crontab.

file 'stopcoffee.py' is responsiblie for stopping the coffee machine at any specified time in works with crontab.
