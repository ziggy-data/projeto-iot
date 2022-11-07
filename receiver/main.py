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

# Recebe as mensagens do topico que esta inscrito e vai retornar nesse callback
def sub_cb(topic, msg):
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
print('Conectado!')    

print("Conectando ao servidor MQTT... ")
cliente = MQTTClient(MQTT_ID_CLIENT,
                        MQTT_BROKER,
                        user = MQTT_USUARIO,
                        password=MQTT_SENHA)

cliente.connect() # Realiza a conexão com serviço de mensageria
cliente.set_callback(sub_cb) #Configura o metodo de callback para assim que receber as mensagem realizar o método
cliente.subscribe(MQTT_TOPICO)  #Realiza a inscrição do tópico para receber as mensagens
print("Conectado ao servidor")

while True:
    print("Esperando uma nova mensagem...")
    cliente.wait_msg() #Fica aguardando as mensagens do serviço de mensageria


     
     
        

