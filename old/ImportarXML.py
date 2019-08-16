# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 01:45:17 2018

@author: Joao Junkes
"""

from pybrain.tools.customxml.networkreader import NetworkReader

import TreinarRNA

def Importar(caminho):

    TreinarRNA.CriarObjTreinamento()

    TreinarRNA.rede = NetworkReader.readFrom(caminho)