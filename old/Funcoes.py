# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 02:45:31 2018

@author: Joao Junkes
"""

from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer

from pybrain.tools.customxml.networkwriter import NetworkWriter
from pybrain.tools.customxml.networkreader import NetworkReader

def Importar(caminho):
    rede = NetworkReader.readFrom(caminho)