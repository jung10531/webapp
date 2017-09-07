from flask import Flask 
import RPi.GPIO as GPIO

app = Flask(__name__) #make instance

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT, initial = GPIO.LOW)

@app.route('/LED/<val>')
def led(val):
	val = val.upper()
	if (val == 'ON'):
		GPIO.output(8, GPIO.HIGH)
		return 'LED ON'
	if (val == 'OFF'):
		GPIO.output(8, GPIO.LOW)
		return 'LED OFF'
	else:
		return 'Not val'

if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0', port=8888)
