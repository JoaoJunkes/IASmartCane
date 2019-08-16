
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 00:19:42 2018

@author: Joao Junkes
"""

from pathlib import Path
from pybrain.tools.customxml.networkreader import NetworkReader

import time

import Init
import AtivarRNA
import ReproduzirAlerta
import RetornaEntSensor

def ExecutaSistema():
    try:
        ReproduzirAlerta.Reproduzir('iniciando')
        time.sleep(3)
        
        pesosInit = Path("baseIA.xml")
        
        if not pesosInit.exists():
            ReproduzirAlerta.Reproduzir('treinamentoInit')
            time.sleep(3)
            Init.InicializarParamRNA()
         
        Init.rede = NetworkReader.readFrom('baseIA.xml')
    
        saida_old = 0
        dist1_old = 0
        dist2_old = 0
        dist3_old = 0
        seq_sensor= 0
        x = 0
        y = 0
        result = ''
        dif = 1
    
        threadSensor = RetornaEntSensor.ThreadSensor()
        threadSensor.start()
        
        ReproduzirAlerta.Reproduzir('vamosLa')
        time.sleep(5)
        while True:
            dist1 = (RetornaEntSensor.Sensor.PegaDistanciaSensor(1)) / 100
            
            dist1 = dist1 if dist1 > 0 else 0
            dist2 = (RetornaEntSensor.Sensor.PegaDistanciaSensor(2)) / 100
        
            dist2 = dist2 if dist2 > 0 else 0
            dist3 = (RetornaEntSensor.Sensor.PegaDistanciaSensor(3)) / 100
        
            dist3 = dist3 if dist3 > 0 else 0
          
            if ((dist1 + 0.5 > dist1_old) and (dist2 + 0.5 > dist2_old) and (dist3 + 0.5 > dist3_old) and
               (dist1 - 0.5 < dist1_old) and (dist2 - 0.5 < dist2_old) and (dist3 - 0.5 < dist3_old) and
               (dist3 <= 0.1)):
                seq_sensor += 1
            else:
                dist1_old = dist1
                dist2_old = dist2
                dist3_old = dist3
                
                seq_sensor = 0
            
            if seq_sensor < 2:
                continue
            
            seq_sensor = 0
            
            if x == 0:
                distanciaControle = []
            
            threadON = bool(Init.threadON)
            if threadON:
                print("Treinando rede")
            else:
                print("Colhendo dados para treinamento")
            
            if (x > 2) and (not threadON):
                x = 0
        
                dif = distanciaControle[2] - distanciaControle[0]
                
                if dif == 0:
                    dif = 1
                    
                bias = 1
                baseResult = Init.AdicionaBase(dist1*dif,dist2*dif,dist3*dif)
        
                Init.base.addSample((bias,dist1,dist2,dist3),(baseResult))
                 
                distanciaControle.clear()
                
                if y > 100:
                    y = 0
                    
                    treinarThread = Init.ThreadTreinar()
                    treinarThread.start()
                y += 1
                 
            x += 1
            
            distanciaControle.append(dist2)
            
            dist1 = dist1*dif
            dist2 = dist2*dif
            dist3 = dist3*dif
            
            saida = AtivarRNA.AtivarEntrada(NetworkReader,[1, dist1, dist2, dist3])
        
            result = ''
            for i in saida:
                result += '1' if i > 0.5 else '0'    
            
            if ((result != '0001') and 
               (result != '1111') and 
               (result != '1000') and 
               (result != '1100')):
                result = ''
                continue   
            
            if saida_old == result:
                result = ''
                continue
            try:
                threadReproduzir = ReproduzirAlerta.ThreadReproduzir(result)
                threadReproduzir.start()
                ReproduzirAlerta.Reproduzir(result)
                time.sleep(3)
            finally:
                saida_old = result
                result = ''
    except:
        print("Ocorreu Falha")

while True:
    ExecutaSistema()