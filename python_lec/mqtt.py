import paho.mqtt.client as mqtt

#클라이언트가 서버에게서 응답을 받을 때 호출되는 콜백
def on_connect(client, userdata, flags, rc):
	print("Connected with result code " + str(rc))
	client.subscribe("test")

#서버에게서 PUBLISH 메시지를 받을 때 호출되는 콜백
def on_message(client, userdata, msg):
	print(msg.topic +": "+ str(msg.payload))

client = mqtt.Client() # MQTT Client 오브젝트 생성
client.on_connect = on_connect # on_connect callback설정
client.on_message = on_message # on_message callback설정

client.connect("192.168.0.121", 1883, 60)
client.loop_forever()
