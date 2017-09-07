import Adafruit_DHT
import httplib, urllib
import time

KEY = 'J2909WAYE0NOY12I'
headers = {"Content-type":"application/x-www-form-urlencoded","Accept":"text/plain"}

sensor = Adafruit_DHT.DHT11
pin = 14

def dht11_read():
	humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
	return temperature

while True:
	temp = dht11_read()
	params = urllib.urlencode({'field1': temp, 'key': KEY})
	conn = httplib.HTTPConnection("api.thingspeak.com:80")
	try:
		conn.request("POST", "/update", params, headers)
		response = conn.getresponse()
		print response.status, response.reason
		print temp
	except:
		print "Connection failed"
	time.sleep(5)
