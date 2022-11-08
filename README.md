# Projeto IOT 

## Visão geral

Nesse projeto foi programado 2 sistemas IOT se comunicando por mensageria e alterando dispositivos, como uma prova de conceito (os arquivos diagram.json são utilizados apenas no Wokwi, são dispensáveis para o uso do projeto). O ESP32 foi escolhido por ser uma ferramenta com melhor custo-benefício e o site Wokwi foi utilizado para simular o projeto final.

## Componentes
<ul>
    <li> 
         1 ESP32: é um pequeno microcontrolador desenvolvido com a capacidade de
         proporcionar comunicação sem fio através do wifi e através do próprio sistema
         Bluetooth;
    </li>
    <li>
         1 resistor de 1k Ohms;
    </li> 
    <li>
         1 LED;
    </li> 
    <li> 
         1 PIR Motion Sensor (HC-SR501): possui um sensor piroelétrico de alta sensibilidade
         que consegue detectar a radiação infravermelha emitida pelos corpos. Quanto mais
         quente está um corpo, maior será a radiação infravermelha emitida;
    </li> 
</ul>

## Funcionamento

O sensor PIR Motion Sensor, ao detectar movimento, envia uma mensagem para o ESP32, que
ao receber, envia a mensagem ao tópico da mensageria, que é recebida pelo “receiver” que
está esperando uma mensagem pelo tópico e que, ao receber cada mensagem, verificará o
conteúdo e executará o método de call-back e caso o caso do conteúdo seja o esperado,
acenderá o LED.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Sender layout:  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Receiver layout:  <br>
![Sender!](/sender/sender.png "Sender")
![Receiver!](/receiver/receiver.png "Receiver")


## Considerações Finais

Mensageria foi escolhida principalmente pelo fato de ser uma forma simples de implementar, MicroPython que possui uma implementação para iot mais eficiente e enxuta que o Python completo, e também permite que escale o tamanho do produto final da forma como desejar. Pode-se também modificar os terminais, trocando o led por um relé, que acionaria um ventilador (ou qualquer outro dispositivo) e o sensor por um programa no celular que seria como se fosse o botão “LIGAR/DESLIGAR”.















