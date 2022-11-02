import network
from machine import Pin
import time
from umqtt.simple import MQTTClient

MQTT_ID_CLIENT = 'micropython-presence-demo2'
MQTT_BROKER    = 'broker.mqttdashboard.com'
MQTT_USUARIO   = ''
MQTT_SENHA     = ''
MQTT_TOPICO    = 'presenca'

led = Pin(13, Pin.OUT)

def sub_cb(topic, msg):
    print(msg)
    if msg == b'on':
        led.on()
    else:
        led.off()
    

print("conectando ao WIFI", end="")
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect("Wokwi-GUEST",'')
while not sta_if.isconnected():
    print(".", end='')
    time.sleep(0.1)
print('conectado!')    

print("Conectando ao servidor MQTT... ")
cliente = MQTTClient(MQTT_ID_CLIENT,
                        MQTT_BROKER,
                        user = MQTT_USUARIO,
                        password=MQTT_SENHA)

cliente.connect()  
cliente.set_callback(sub_cb)
cliente.subscribe(MQTT_TOPICO)
print("Conectado ao servidor")

while True:
    print("checando")
    cliente.wait_msg()


     
     
        

