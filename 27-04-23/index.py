tempo = 2
pino = 12 # Pino do Raspberry

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pino, GPIO.OUT)

def acendeLed(pino_led):
    GPIO.output(pino_led, 1)
    return

def apagaLed(pino_led):
    GPIO.output(pino_led, 0)
    return

while(1):
    acendeLed(pino)
    time.sleep(tempo)

    apagaLed(pino)
    time.sleep(tempo)
