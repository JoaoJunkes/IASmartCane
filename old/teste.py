# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 02:41:00 2018

@author: Joao Junkes
"""

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
from pybrain.tools.customxml.networkreader import NetworkReader

#rede = buildNetwork(3, 4, 1)
base = SupervisedDataSet(3, 1)

rede = NetworkReader.readFrom('filename.xml')
   
treinamento = BackpropTrainer(rede, dataset = base, learningrate = 0.01,
                              momentum = 0.06)
for i in range(1, 10000):
    erro = treinamento.train()

print(rede.activate([0.8, 0.3, 0.3]))