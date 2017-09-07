import smtplib
from email.mime.text import MIMEText

import RPi.GPIO as GPIO
import time
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BOARD)
 
#set GPIO Pins
TRIG = 8
ECHO = 10

#set GPIO direction (IN / OUT)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

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
 
dist = distance()
text = "hc_sr04_Detected " + str(dist) + "cm"
print "Distance : ", dist, "cm"
if(dist > 10):
    smtp = smtplib.SMTP('smtp.gmail.com',587)
    smtp.ehlo()
    smtp.starttls()
            
    smtp.login('jung10531@gmail.com','tnghk1548')
    
    msg = MIMEText(text)
    msg['Subject'] = 'Hey, you must notify this situation'
    msg['To'] = 'jung10531@naver.com'
    smtp.sendmail('jung10531@gmail.com', 'jung10531@naver.com',msg.as_string())
    smtp.quit()
    print('send email')

GPIO.cleanup()
