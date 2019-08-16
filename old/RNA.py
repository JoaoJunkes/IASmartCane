# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 01:51:08 2018

@author: Joao Junkes
"""

#[0.8, 0.3, 0.3]
#print(rede.activate([0.8, 0.3, 0.3]))

import TreinarRNA
import ImportarXML
import AtivarRNA

ImportarXML.Importar('filename.xml')

TreinarRNA.Treinar(ImportarXML.TreinarRNA.rede,ImportarXML.TreinarRNA.base)

AtivarRNA.Ativar([0.8, 0.3, 0.3])