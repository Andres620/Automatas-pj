# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 12:49:31 2019

@author: ayuwoki
"""

from heapq import heappop, heappush

class graph:
    def __init__(self,gr):
        self.graph=gr

    def returnPosAdy(self,aux): 
        for h in self.graph:
            if h['label']==aux['label']:
                return h['x'],h['y']