# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 18:56:15 2019

@author: ayuwoki
"""
import json
class generate_graph:
    
    def __init__(self,ov):
        self.oveja=ov
        self.frog = ov
        
    def in_graph(self,x):
        for h in self.oveja['graph']:
            if x==h['label']:
                return True
        return False
    def in_graph_sapo(self,x):
        for h in self.frog['graph']:
            if x==h['label']:
                return True
        return False
    
    def generate_frog(self):
            self.frog['estado_inicial'] =[]
            self.frog['estado_aceptacion'] =[]
            self.frog['graph']=[]
            self.frog['transiciones'] = []
            self.frog['estado_inicial'].append([1,1,1,0,2,2,2])
            self.frog['estado_aceptacion'].append([2,2,2,0,1,1,1])
            self.frog['graph'].append({'label':[1,1,1,0,2,2,2],'FIN':False,
                                   'adyacentes':[], 'done':True})
            
            self.generate_frog_r(self.frog['graph'][0])
    
            with open('rana.json', 'a') as outfile:
                json.dump(self.frog, outfile)
            
            
    def generate_frog_r(self,h):
            print('what?', h,'\n')
            #condicion de escape
            for k in  self.frog['graph']:
                if k['label']==[2,2,2,0,1,1,1]:
                    return
              
            #mover la piedra una casilla a la izquierda
            for k in self.frog['graph']:
                for i in range(len(k['label'])):
                    if k['label'][i] == 0:
                        if h['label'][i-1]==1 and (0 <= i-1 <= len(h['label'])):
                            aux=h['label'][:]
                            aux[i]=1
                            aux[i-1]=0
                            if h['label'][i] == 0 and h['label'][i-1] == 2 and h['label'][i+1] == 1:
                                h['adyacentes'].append({'label':aux , 'FIN':True})
                            else:
                                h['adyacentes'].append({'label':aux , 'FIN':False})
            #mover la piedra una casilla a la derecha
                        if h['label'][i+1]==2 and (0 <= i+1 <= len(h['label'])):
                            aux=h['label'][:]
                            aux[i]=2
                            aux[i+1]=0
                            if h['label'][i] == 0 and h['label'][i+1] == 1 and h['label'][i-1] == 2:
                                h['adyacentes'].append({'label':aux , 'FIN':True})
                            else:
                                h['adyacentes'].append({'label':aux , 'FIN':False})
            
            #mover piedra dos casillas a la izquierda
                        if h['label'][i-2]==1 and h['label'][i-1] == 2 and (0 <= i-2 <= len(h['label'])):
                            aux=h['label'][:]
                            aux[i]=1
                            aux[i-2]=0
                            h['adyacentes'].append({'label':aux , 'FIN':False})
                        print("lfjekhfij",i)    
            #mover piedra dos casillas a la derecha
                        if h['label'][i+2]==2 and h['label'][i+1] == 1 and (0 <= i+2 <= len(h['label'])):
                            aux=h['label'][:]
                            aux[i]=2
                            aux[i+2]=0
                            h['adyacentes'].append({'label':aux , 'FIN':False})
            
            
            for j in h['adyacentes']:
                if self.in_graph_sapo(j['label']):
                    continue
                else:
                    self.frog['graph'].append({'label':j['label'],'FIN':j['FIN'],
                                   'adyacentes':[], 'done': False})
    

            for i in self.frog['graph']:
                if not i['done']:
                    i['done']=True
                    if not i['FIN']:
                        self.generate_frog_r(i)
                
    
                            
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
                if self.in_graph(j['label']):
                    continue
                else:
                    self.oveja['graph'].append({'label':j['label'],'FIN':j['FIN'],
                                   'adyacentes':[], 'done': False})

            for i in self.oveja['graph']:
                if not i['done']:
                    i['done']=True
                    if not i['FIN']:
                        self.generate_sheep_r(i)
                
                
        
