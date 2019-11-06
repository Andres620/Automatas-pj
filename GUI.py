# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 18:30:54 2019

@author: ayuwoki
"""

import pygame
from pygame.locals import RESIZABLE
import sys

class GUI:
    
    def __init__(self,graph):
        self.graph=graph
        self.sWIDTH = 1180    #screen width
        self.sHEIGHT = 600    #screen height
        self.font=None
        self.screen=None
    
    def window(self):
        pygame.init()
        pygame.display.set_caption("Automaton")
        self.screen=pygame.display.set_mode((self.sWIDTH, self.sHEIGHT),RESIZABLE)
        self.screen.fill((211, 200, 227))
        self.font = pygame.font.SysFont("Arial", 12)
        self.paintLines()
        x=0
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit() 
            if x==0:
               self.paint(self.graph)
               x=x+1
            
            pygame.display.update()
        
            
    def paint(self,graph):
        if not graph is None:
            for h in graph.graph:
                pygame.draw.circle(self.screen, (238, 241, 9),(h['x'],h['y']), 10)
                textID = self.font.render("{}".format(h['label']), 0, (0, 0, 0))
                self.screen.blit(textID, (h['x']-20,h['y']-10))
                pygame.display.flip()
                
    def paintLines(self):
         for h in self.graph.graph:
            x1=h['x']
            y1=h['y']
            for j in h['adyacentes']:
                x2,y2=self.graph.returnPosAdy(j)
                pygame.draw.line(self.screen,(241, 129, 9),(x1,y1),(x2,y2),2)
                pygame.display.flip()
         pygame.display.flip()
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                