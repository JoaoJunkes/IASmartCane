# coding:utf-8
 
import threading

#variaveis globais
sensor1 = 0
sensor2 = 0
sensor3 = 0

class ThreadSensor(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
      
    def run(self):
        Sensor.AtualizaDistancia()
             
class Sensor:    
    def PegaDistanciaSensor(sensor):
        global sensor1
        global sensor2
        global sensor3    
    
        if sensor == 1:
            return sensor1
        elif sensor == 2:
            return sensor2
        else:
            return sensor3
    
    
    def AtualizaDistancia():
        global sensor1
        global sensor2
        global sensor3
    
        while True:
            sensor1 = Sensor.PegaDistancia(1)
            sensor2 = Sensor.PegaDistancia(2)
            sensor3 = Sensor.PegaDistancia(3)
            
    def PegaDistancia(sensor):
        if sensor == 1:
            return 1
        elif sensor == 2:
            return 2
        elif sensor == 3:
            return 3