# coding:utf-8

'''import sys
import time
import signal
import RPi.GPIO as GPIO'''
'''import threading

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
            sensor1 = 1#Sensor.PegaDistancia(1)
            time.sleep(2)
            
            sensor2 = 2#Sensor.PegaDistancia(2)
            time.sleep(2)
            
            sensor3 = 3#Sensor.PegaDistancia(3)
            time.sleep(2)
            
    '''def PegaDistancia(sensor):
        if sensor == 1:
            return 1
        elif sensor == 2:
            return 2        
        else:
            return 3
   ''' def PegaDistancia(sensor):
        # Define a numeração dos pinos de acordo com a placa
        GPIO.setmode(GPIO.BOARD)
         
        # Função para finalizar o acesso à GPIO do Raspberry de forma segura
        def clean():
            GPIO.cleanup()
         
        # Função para finalizar o programa de forma segura com CTRL-C
        def sigint_handler(signum, instant):
            clean()
            sys.exit()
         
        # Ativar a captura do sinal SIGINT (Ctrl-C)
        signal.signal(signal.SIGINT, sigint_handler)
         
        if sensor == 1:
            # TRIG será conectado ao pino 18. ECHO ao pino 16.
            TRIG = 11
            ECHO = 33
        elif sensor == 2:
            # TRIG será conectado ao pino 18. ECHO ao pino 16.TROCAR OS VALORES
            TRIG = 13
            ECHO = 35        
        else:
            # TRIG será conectado ao pino 18. ECHO ao pino 16. TROCAR OS VALORES
            TRIG = 15
            ECHO = 37
            
        # Variáveis para auxiliar no controle do loop principal
        # sampling_rate: taxa de amostragem em Hz, isto é, em média,
        #   quantas leituras do sonar serão feitas por segundo
        # speed_of_sound: velocidade do som no ar a 30ºC em m/s
        # max_distance: máxima distância permitida para medição
        # max_delta_t: um valor máximo para a variável delta_t,
        #   baseado na distância máxima max_distance
        sampling_rate = 20.0
        speed_of_sound = 349.10
        max_distance = 4.0
        max_delta_t = max_distance / speed_of_sound
         
        # Define TRIG como saída digital
        # Define ECHO como entrada digital
        GPIO.setup(TRIG, GPIO.OUT)
        GPIO.setup(ECHO, GPIO.IN)
         
        # Inicializa TRIG em nível lógico baixo
        GPIO.output(TRIG, False)
        time.sleep(1)
         
        #print ("Sampling Rate:", sampling_rate, "Hz")
        #print ("Distances (cm)")
         
        # Loop principal. Será executado até que que seja pressionado CTRL-C
        #while True:
         
        # Gera um pulso de 10ms em TRIG.
        # Essa ação vai resultar na transmissão de ondas ultrassônicas pelo
        # transmissor do módulo sonar.
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)
     
        # Atualiza a variável start_t enquanto ECHO está em nível lógico baixo.
        # Quando ECHO trocar de estado, start_t manterá seu valor, marcando
        # o momento da borda de subida de ECHO. Este é o momento em que as ondas
        # sonoras acabaram de ser enviadas pelo transmissor.
        while GPIO.input(ECHO) == 0:
          start_t = time.time()
     
        # Atualiza a variável end_t enquando ECHO está em alto. Quando ECHO
        # voltar ao nível baixo, end_t vai manter seu valor, marcando o tempo
        # da borda de descida de ECHO, ou o momento em que as ondas refletidas
        # por um objeto foram captadas pelo receptor. Caso o intervalo de tempo
        # seja maior que max_delta_t, o loop de espera também será interrompido.
        while GPIO.input(ECHO) == 1 and time.time() - start_t < max_delta_t:
          end_t = time.time()
     
        # Se a diferença entre end_t e start_t estiver dentro dos limites impostos,
        # atualizamos a variável delta_t e calculamos a distância até um obstáculo.
        # Caso o valor de delta_t não esteja nos limites determinados definimos a
        # distância como -1, sinalizando uma medida mal-sucedida.
        if end_t - start_t < max_delta_t:
            delta_t = end_t - start_t
            distance = 100*(0.5 * delta_t * speed_of_sound)
        else:
            distance = -1
     
        # Imprime o valor da distância arredondado para duas casas decimais
        #print (round(distance, 2))
        
        return round(distance, 2)
     
        # Um pequeno delay para manter a média da taxa de amostragem
        #time.sleep(1/sampling_rate)
            '''