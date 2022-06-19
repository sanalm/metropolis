from time import sleep
from machine import Pin
import ujson
import machine
import ubinascii
import urandom as random
import ntptime 
import time
from machine import RTC

class Webhook:
    def __init__(self):
        ntptime.settime()  # Synchronise the system time using NTP
        self.blueLed = machine.Pin(2, machine.Pin.OUT)
        self.ledInterval = 0.01
        self.readingInterval = 0.5

    def wait_twitter(self):
        # wait for webhook
        self.blueLed.value(1)
        sleep(self.ledInterval)
        self.blueLed.value(0)
        


