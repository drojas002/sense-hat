import paho.mqtt.client as mqtt

import time

from sense_hat import SenseHat

sense = SenseHat()

# set up mqtt client

client = mqtt.Client("python_pub")

#set mqtt username/pw

client.username_pw_set(username="pi", password="raspberry")

#set server to publish to

client.connect("192.168.1.93", 1883)

client.loop_start()

try:
    while True:
        #publish temp to topic
        client.publish("sense/temp", sense.get_temperature())
        #publish humidity
        client.publish("sense/humid", sense.get_humidity())
        #pause for 10 seconds
        time.sleep(10)
        #deal nicely with ^C
except KeyboardInterrupt:
        print("interrupted!")
        client.loop_stop()