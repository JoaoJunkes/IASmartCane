# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 01:51:08 2018

@author: Joao Junkes
"""

#[0.8, 0.3, 0.3]
#print(rede.activate([0.8, 0.3, 0.3]))

from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer

from pybrain.tools.customxml.networkwriter import NetworkWriter
import threading
#import os
#from pybrain.tools.customxml.networkreader import NetworkReader
#import AtivarRNA



def PrimeiraCarga(base):
    base.addSample((1,0,1,1),(0,0,0,1))
    base.addSample((1,0,0,0),(1,1,1,1))
    base.addSample((1,1,1,0.5),(1,0,0,0))
    base.addSample((1,1,1,0),(1,1,0,0))
  

def Treinar(rede,base):
    try:
        print("Iniciando treinamento")
        erro = 10
        erro_old = 0
        tentativas = 0
        tentativa_controle = 0
        
        '''xml = "D:\SmartCane"
        dir = os.listdir(xml)
        for file in dir:
            if file == "baseIA.xml":
                os.remove(file)'''
       
        treinamento = BackpropTrainer(rede, dataset = base, learningrate = 0.01,
                                      momentum = 0.06)
        #for i in range(1, 100):
        while (tentativas < 10000) and (round(erro,3) > 0.001):
            print("Preparando treinamento")
            erro = treinamento.train()
            
            if (erro < 0.001):
                print("Erro baixo")
            else:
                print(erro)
        
            if (tentativa_controle > 1000) and (erro_old > 0) and (erro_old <= erro):
                break
            
            if tentativa_controle > 1000:
                erro_old = erro
                tentativa_controle = 0
    
            tentativas += 1        
            tentativa_controle +=  1
        
        NetworkWriter.writeToFile(rede, 'baseIA.xml')
        print("Base gravada com sucesso")
    except:
        global threadON
        threadON = False

class ThreadTreinar(threading.Thread):
    def __init__(self):
       threading.Thread.__init__(self)
      
    def run(self):
        global threadON
        threadON = True
        #rede.reset()
        try:
            Treinar(rede,base)
        finally:
            threadON = False
       
       #self._stop()

def InicializarParamRNA():    
    PrimeiraCarga(base)
    Treinar(rede,base)
    
    #NetworkWriter.writeToFile(rede, 'baseIA.xml')
    
def AdicionaBase(dist1,dist2,dist3):
    if dist1 >= 1 and dist2 >= 1 and dist3 < 0.2:
        return '1100'
    elif dist1 >= 1 and dist2 >= 1 and dist3 > 0.2:
        return '1000'
    elif dist1 < 1 and dist2 < 1 and dist3 < 0.2:
        return '1111'
    elif dist1 < 1 and dist2 >= 1:
        return '0001'
    else:
        return '0000'

base = SupervisedDataSet(4, 4)
rede = buildNetwork(4, 15, 4)
threadON = False