# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 18:56:15 2019

@author: ayuwoki
"""
import json
class generate_graph:
    
    def generate_sheep():
            oveja = {}
            oveja['estado_inicial'] =[]
            oveja['estado_aceptacion'] =[]
            oveja['graph']=[]
            oveja['transiciones'] = []
            oveja['estado_inicial'].append([0,0,0,0])
            oveja['estado_aceptacion'].append([1,1,1,1])
            oveja['graph'].append({'label':oveja['estado_inicial'],
                                   'adyacentes':[]})
    
            with open('oveja.json', 'a') as outfile:
                json.dump(oveja, outfile)
