import RPi.GPIO as GPIO
import time
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BOARD)
 
#set GPIO Pins
TRIG = 8
ECHO = 10
LED = 12
LED2 = 16
#set GPIO direction (IN / OUT)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED2, GPIO.OUT, initial=GPIO.LOW)

def distance():
    # set Trigger to HIGH
    GPIO.output(TRIG, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(ECHO) == 1:
        StopTime = time.time()
 
    
    Time = StopTime - StartTime
    # distance = (Time * 34300) / 2
    distance = Time * 17150
    distance = round(distance, 2)
    return distance
 
try:
    while True:
        dist = distance()
        if (dist <= 20):
            GPIO.output(LED, GPIO.HIGH)
        if (dist <= 10):
            GPIO.output(LED2, GPIO.HIGH)
        if (dist > 10):
            GPIO.output(LED2, GPIO.LOW)
        if (dist > 20):
            GPIO.output(LED, GPIO.LOW)
        print "Distance : ", dist, "cm"
        time.sleep(2)
 
except KeyboardInterrupt:
    print("Stopped by User")
    GPIO.cleanup()
