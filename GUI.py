# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 18:30:54 2019

@author: ayuwoki
"""

import pygame
from pygame.locals import RESIZABLE
import sys
from time import sleep
from pygame.locals import K_1, K_2, K_3,K_4,K_5,K_6,K_r,K_a,K_b,K_x,K_y,K_z,K_p,K_q

class GUI:
    
    def __init__(self,graph,gr):
        self.graph=graph
        self.generate_graph=gr
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
        
        
        
        x=0
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit() 
                if event.type == pygame.KEYDOWN:
                    if event.key == K_1:  #llamar paso a paso
                        self.paintPathNodes()
                        self.paintPath()
                    if event.key == K_2:  #limpiar pantalla
                        x=0
                        
            if x==0:
               self.paint(self.graph)
               self.paintLines()
               x=x+1
            
            pygame.display.update()
        
        
            
    def paint(self,graph):
        if not graph is None:
            for h in graph.graph:
                pygame.draw.circle(self.screen, (238, 241, 9),(h['x'],h['y']), 10)
                if h['label']==graph.estado_inicial[0]:
                    pygame.draw.circle(self.screen, (9, 241, 27),(h['x'],h['y']), 10)
                if h['label']==graph.estado_aceptacion[0]:
                    pygame.draw.circle(self.screen, (241, 9, 9),(h['x'],h['y']), 10)
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
                pygame.draw.circle(self.screen, (241, 9, 9),(x2,y2-10), 3)
                pygame.display.flip()
            
         pygame.display.flip()
        
    def paintPath(self):
        aux=self.generate_graph.return_path_pos(self.graph)
        for h in range(1,len(aux)):
           pygame.draw.line(self.screen,(23, 48, 235),(aux[h-1][0],aux[h-1][1]),(aux[h][0],aux[h][1]),2)
           
            
    def paintPathNodes(self):
        aux=self.generate_graph.return_path_pos(self.graph)
        for h in aux:
            pygame.draw.circle(self.screen, (50, 168, 82),(h[0],h[1]), 10)
            pygame.display.flip()
            sleep(0.5) 
        
        
            
            
            
            
            
            
            
            
            
            
            
            
            
            