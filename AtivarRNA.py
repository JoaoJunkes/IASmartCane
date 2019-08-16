# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 12:09:00 2018

@author: Joao Junkes
"""

#[0.8, 0.3, 0.3]
#print(rede.activate([0.8, 0.3, 0.3]))

def AtivarEntrada(NetWR,values):
    rede = NetWR.readFrom('baseIA.xml')
    return rede.activate(values)