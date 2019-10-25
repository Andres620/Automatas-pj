# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 18:30:54 2019

@author: ayuwoki
"""

import pygame
import random
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
        pygame.display.set_caption("Soy el mapa")
        self.screen=pygame.display.set_mode((self.sWIDTH, self.sHEIGHT),RESIZABLE)
        self.screen.fill((211, 200, 227))
        self.font = pygame.font.SysFont("Arial", 12)
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
            x=0
            for h in graph:
                x=random.randint(10, 1100)
                y=random.randint(10, 500)
                pygame.draw.circle(self.screen, (238, 241, 9),(x,y), 10)
                textID = self.font.render("{}".format(h['label']), 0, (0, 0, 0))
                self.screen.blit(textID, (x-20,y-10))
                pygame.display.flip()
                
    def paintLines(self):
         for h in self.graph:
            for j in h['adyacentes']:
                x1=h['posX']+20
                y1=h['posY']+20
                x2=self.graph.returnPlace(j['label'])['posX']+20
                y2=self.graph.returnPlace(j['label'])['posY']+20
                if not j['obstruction']:
                    pygame.draw.line(self.screen,(26,8,242),(x1,y1),(x2,y2),5)
                else:
                    pygame.draw.line(self.screen,(200, 0, 0),(x1,y1),(x2,y2),5)
                    avgPosX,avgPosY=self.graph.midPoint(x1,y1,x2,y2)
                    self.screen.blit(self.deadDonkey,(avgPosX,avgPosY-30))
                    pygame.display.flip()
         pygame.display.flip()
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                