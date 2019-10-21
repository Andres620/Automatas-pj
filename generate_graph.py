# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 18:56:15 2019

@author: ayuwoki
"""
import json
class generate_graph:
    
    def __init__(self,ov):
        self.oveja=ov
    
    def generate_sheep(self):
            self.oveja['estado_inicial'] =[]
            self.oveja['estado_aceptacion'] =[]
            self.oveja['graph']=[]
            self.oveja['transiciones'] = []
            self.oveja['estado_inicial'].append([0,0,0,0])
            self.oveja['estado_aceptacion'].append([1,1,1,1])
            self.oveja['graph'].append({'label':self.oveja['estado_inicial'],
                                   'adyacentes':[]})
            
            self.generate_sheep_r(self.oveja)
    
            with open('oveja.json', 'a') as outfile:
                json.dump(self.oveja, outfile)
                
    def generate_sheep_r(self,oveja):
        
        for h in oveja['graph']:
            #pasar obeja
            if h['label'][0][1]==0 and h['label'][0][3]==0:
                aux=h['label'][0]
                aux[1]=1
                aux[3]=1
                h['adyacentes'].append({'label':aux})
                
        
