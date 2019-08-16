# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 01:45:17 2018

@author: Joao Junkes
"""

from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer

from pybrain.tools.customxml.networkwriter import NetworkWriter

def CriarObjTreinamento():
    rede = buildNetwork(3, 4, 1)
    base = SupervisedDataSet(3, 1)

def PrimeiraCarga():
    base.addSample((0, 0, 0), (1))
    base.addSample((0, 0, 1), (2))
    base.addSample((0, 1, 0), (3))
    base.addSample((0, 1, 1), (4))
    base.addSample((1, 0, 0), (5))
    base.addSample((1, 0, 1), (6))
    base.addSample((1, 1, 0), (7))
    base.addSample((1, 1, 1), (8))

def Treinar(rede,base):
    treinamento = BackpropTrainer(rede, dataset = base, learningrate = 0.01,
                                  momentum = 0.06)
    for i in range(1, 10000):
        erro = treinamento.train()
    
    NetworkWriter.writeToFile(rede, 'filename.xml')