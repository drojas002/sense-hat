from sense_hat import SenseHat

sense = SenseHat()

while True:
    temp = sense.get_temperature()
    temp = round(temp, 2)
    msg = "Temperatura =%s" %(temp)
    sense.show_message(msg)