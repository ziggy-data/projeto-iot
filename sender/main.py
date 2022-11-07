import network
from machine import Pin
import time
from umqtt.simple import MQTTClient

MQTT_ID_CLIENT = 'micropython-presence-demo'
MQTT_BROKER    = 'broker.mqttdashboard.com'
MQTT_USUARIO   = ''
MQTT_SENHA     = ''
MQTT_TOPICO    = 'presenca'

# Configura a pinagem dos itens utilizados no código
sensor = Pin(4, Pin.IN) 
led = Pin(13, Pin.OUT)

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

print("Conectado ao servidor")

while True:
    # Vai verificar se o sensor de presença 'percebeu' alguém no ambiente e
    # imprime uma mensagem e envia a mensagem para acender um led (com o dispositivo 'receiver')
    if sensor.value() == 1:
        print("Welcome home, Master!")
        led.on()
        #Envia em bytes a mensagem "on" para o dispositivo "receiver" receber a informação para alterar 
        cliente.publish(MQTT_TOPICO, b'on') 
        time.sleep(3)
        led.off()
        cliente.publish(MQTT_TOPICO, b'off')
