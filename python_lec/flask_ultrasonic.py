from flask import Flask
import os
import time
import RPi.GPIO as GPIO

app = Flask(__name__)

GPIO.setmode(GPIO.BOARD)

trig = 12
echo = 16

GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

def distance():
	GPIO.output(trig, True)

	time.sleep(0.00001)
	GPIO.output(trig, False)

	start = time.time()
	stop = time.time()

	while GPIO.input(echo) == 0:
		start = time.time()
	while GPIO.input(echo) == 1:
		stop = time.time()

	Time = stop - start
	distance = Time * 17150
	distance = round(distance, 2)
	return distance

@app.route('/SONIC')
def sonic():
	dist = distance()
	if (dist > 10):
		os.system("curl http://192.168.0.121:8888/LED/on")
		return 'LED ON'
	else:
		os.system("curl http://192.168.0.121:8888/LED/off")
		return 'LED OFF'

if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0', port=12312)
