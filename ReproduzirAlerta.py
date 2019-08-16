# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 02:16:52 2018

@author: Joao Junkes
"""

import pygame
import threading

class ThreadReproduzir(threading.Thread):
    def __init__(self,Alerta):
       threading.Thread.__init__(self)
       self.Alerta = Alerta
       
    def run(self):
       Reproduzir(self.Alerta)
       #self._stop()

def Reproduzir(Alerta):
    
    mp3 = str(Alerta)+".mp3"
    
    pygame.init()
    pygame.mixer.music.load(mp3)
    pygame.mixer.music.play()
    print("Reproduzindo audio: "+str(mp3))