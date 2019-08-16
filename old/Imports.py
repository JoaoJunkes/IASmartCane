# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 02:10:34 2018

@author: Joao Junkes
"""

def ImportarModulos():
    from pybrain.tools.shortcuts import buildNetwork
    from pybrain.datasets import SupervisedDataSet
    from pybrain.supervised.trainers import BackpropTrainer

    from pybrain.tools.customxml.networkwriter import NetworkWriter
    from pybrain.tools.customxml.networkreader import NetworkReader