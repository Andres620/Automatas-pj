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
        
            self.oveja['graph'].append({'label':[0,0,0,0],'FIN':False,
                                   'adyacentes':[], 'done':True})
            
            self.generate_sheep_r(self.oveja['graph'][0])
    
            with open('oveja.json', 'a') as outfile:
                json.dump(self.oveja, outfile)
                
    def generate_sheep_r(self,h):
            print('what?', h,'\n')
            
            #condicion de escape
            for k in  self.oveja['graph']:
                if k['label']==[1,1,1,1]:
                    return
        
            #pasar repollo
            if h['label'][0]==0 and h['label'][3]==0:
                aux=h['label'][:]
                aux[0]=1
                aux[3]=1
                if h['label'][1]==h['label'][2]:
                    h['adyacentes'].append({'label':aux , 'FIN':True})
                else:
                    h['adyacentes'].append({'label':aux , 'FIN':False})
            #pasar oveja
            if h['label'][1]==0 and h['label'][3]==0:
                aux=h['label'][:]
                aux[1]=1
                aux[3]=1
                h['adyacentes'].append({'label':aux , 'FIN':False})
            
            #pasar lobo
            if h['label'][2]==0 and h['label'][3]==0:
                aux=h['label'][:]
                aux[2]=1
                aux[3]=1
                if h['label'][0]==h['label'][1]:
                    h['adyacentes'].append({'label':aux , 'FIN':True})
                else:
                    h['adyacentes'].append({'label':aux , 'FIN':False})
            #pasar solo barco
            if h['label'][3]==0:
                aux=h['label'][:]
                aux[3]=1
                if h['label'][0]==h['label'][1] or h['label'][1]==h['label'][2]:
                    h['adyacentes'].append({'label':aux , 'FIN':True})
                else:
                    h['adyacentes'].append({'label':aux , 'FIN':False})
            
            #devolver repollo
            if h['label'][0]==1 and h['label'][3]==1:
                aux=h['label'][:]
                aux[0]=0
                aux[3]=0
                if h['label'][1]==h['label'][2]:
                    h['adyacentes'].append({'label':aux , 'FIN':True})
                else:
                    h['adyacentes'].append({'label':aux , 'FIN':False})
            
            #devolver oveja
            if h['label'][1]==1 and h['label'][3]==1:
                aux=h['label'][:]
                aux[1]=0
                aux[3]=0
                h['adyacentes'].append({'label':aux , 'FIN':False})
            
            #devolver lobo
            if h['label'][2]==1 and h['label'][3]==1:
                aux=h['label'][:]
                aux[2]=0
                aux[3]=0
                if h['label'][0]==h['label'][1]:
                    h['adyacentes'].append({'label':aux , 'FIN':True})
                else:
                    h['adyacentes'].append({'label':aux , 'FIN':False})
                
            #pasar solo barco
            if h['label'][3]==1:
                aux=h['label'][:]
                aux[3]=0
                if h['label'][0]==h['label'][1] or h['label'][1]==h['label'][2]:
                    h['adyacentes'].append({'label':aux , 'FIN':True})
                else:
                    h['adyacentes'].append({'label':aux , 'FIN':False})
            
            
                        
        
            for j in h['adyacentes']:
                self.oveja['graph'].append({'label':j['label'],'FIN':j['FIN'],
                                   'adyacentes':[], 'done': False})

            for i in self.oveja['graph']:
                if not i['done']:
                    i['done']=True
                    if not i['FIN']:
                        self.generate_sheep_r(i)
                
                
        
