import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

GPIO.cleanup()

GPIO.setmode(GPIO.BCM)

TRIG = 4

ECHO = 18

GREEN = 17

GPIO.setup(TRIG,GPIO.OUT)

GPIO.setup(ECHO,GPIO.IN)

GPIO.setup(GREEN,GPIO.OUT)

def green_light():
    
    GPIO.output(GREEN, GPIO.HIGH)


def get_distance():

    GPIO.output(TRIG, True)

time.sleep(0.00001)

GPIO.output(TRIG, False)

while GPIO.input(ECHO) == False: start = time.time()

while GPIO.input(ECHO) == True: end = time.time()

signal_time = end-start

distance = signal_time / 0.000058

print(distance)

    

while True:
    

    distance = get_distance()
    


    time.sleep(0.05)

print(distance)

if distance >= 25:
    

    green_light()

elif 25 > distance > 10:
    

    green_light()

elif distance <= 5:

    green_light()