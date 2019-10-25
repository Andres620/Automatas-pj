# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 18:56:15 2019

@author: ayuwoki
"""
import json
import random
class generate_graph:
    
    def __init__(self,ov):
        self.oveja=ov
        self.cannibal=ov
        
    def in_graph_sheep(self,x):
        for h in self.oveja['graph']:
            if x==h['label']:
                return True
        return False
    
    def in_graph_cannibal(self,x):
        for h in self.cannibal['graph']:
            if x==h['label']:
                return True
        return False
    
    def generate_sheep(self):
            self.oveja['estado_inicial'] =[]
            self.oveja['estado_aceptacion'] =[]
            self.oveja['graph']=[]
            self.oveja['transiciones'] = []
            self.oveja['estado_inicial'].append([0,0,0,0])
            self.oveja['estado_aceptacion'].append([1,1,1,1])
        
            self.oveja['graph'].append({'label':[0,0,0,0],'FIN':False,
                                   'adyacentes':[], 'done':True,'x':random.randint(10, 1100),'y':random.randint(10, 500)})
            
            self.generate_sheep_r(self.oveja['graph'][0])
    
            with open('oveja.json', 'w') as outfile:
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
                if self.in_graph_sheep(j['label']):
                    continue
                else:
                    self.oveja['graph'].append({'label':j['label'],'FIN':j['FIN'],
                                   'adyacentes':[], 'done': False , 'x':random.randint(10, 1100),'y':random.randint(10, 500)})

            for i in self.oveja['graph']:
                if not i['done']:
                    i['done']=True
                    if not i['FIN']:
                        self.generate_sheep_r(i)
                        
    def generate_cannibal(self):
            self.cannibal['estado_inicial'] =[]
            self.cannibal['estado_aceptacion'] =[]
            self.cannibal['graph']=[]
            self.cannibal['transiciones'] = []
            self.cannibal['estado_inicial'].append([0,0,'D'])
            self.cannibal['estado_aceptacion'].append([3,3,'I'])
        
            self.cannibal['graph'].append({'label':[0,0,'D'],'FIN':False,
                                   'adyacentes':[], 'done':True,'x':random.randint(10, 1100),'y':random.randint(10, 500)})
            
            self.generate_cannibal_r(self.cannibal['graph'][0])
            
            for h in self.cannibal['graph']:
                print('Label: ', h['label'], h['FIN'])
                for i in h['adyacentes']:
                    print('          adyacentes: ', i['label'] ,i['FIN'])
    
            with open('cannibal.json', 'w') as outfile:
                json.dump(self.cannibal, outfile)
                
                
    def generate_cannibal_r(self,h):
            print('what?', h,'\n')
            
            #condicion de escape
            for k in  self.cannibal['graph']:
                if k['label']==[3,3,'I']:
                    return
        
            #pasar un canibal
            if h['label'][1]<3 and h['label'][2]=='D':
                aux=h['label'][:]
                aux[1]=aux[1]+1
                aux[2]="I"
                if h['label'][0]==0 or h['label'][0]==3:
                    h['adyacentes'].append({'label':aux , 'FIN':False})
                else:
                    h['adyacentes'].append({'label':aux , 'FIN':True})
                    
            #devolver un canibal
            if h['label'][1]>0 and h['label'][2]=='I':
                aux=h['label'][:]
                aux[1]=aux[1]-1
                aux[2]="D"
                if h['label'][0]==0 or h['label'][0]==3:
                    h['adyacentes'].append({'label':aux , 'FIN':False})
                else:
                    h['adyacentes'].append({'label':aux , 'FIN':True})
                    
            #pasar dos canibal
            if h['label'][1]<=1 and h['label'][2]=='D':
                aux=h['label'][:]
                aux[1]=aux[1]+2
                aux[2]='I'
                if h['label'][0]==0 or h['label'][0]==3:
                    h['adyacentes'].append({'label':aux , 'FIN':False})
                else:
                    h['adyacentes'].append({'label':aux , 'FIN':True})
                    
            #devolver dos canibal
            if h['label'][1]>=2 and h['label'][2]=='I':
                aux=h['label'][:]
                aux[1]=aux[1]-2
                aux[2]='D'
                if h['label'][0]==0 or h['label'][0]==3:
                    h['adyacentes'].append({'label':aux , 'FIN':False})
                else:
                    h['adyacentes'].append({'label':aux , 'FIN':True})
                              
            #pasar un misionero
            if h['label'][0]<3 and h['label'][2]=='D':
                aux=h['label'][:]
                aux[0]=aux[0]+1
                aux[2]='I'
                if (aux[0]!=0 and aux[0]< aux[1]) or (aux[0]!=3 and aux[0]> aux[1]):
                    h['adyacentes'].append({'label':aux , 'FIN':True})
                else:
                    h['adyacentes'].append({'label':aux , 'FIN':False})
                    
            #devolver un misionero
            if h['label'][0]>0 and h['label'][2]=='I':
                aux=h['label'][:]
                aux[0]=aux[0]-1
                aux[2]='D'
                if (aux[0]!=0 and aux[0]< aux[1]) or (aux[0]!=3 and aux[0]> aux[1]):
                    h['adyacentes'].append({'label':aux , 'FIN':True})
                else:
                    h['adyacentes'].append({'label':aux , 'FIN':False})
            
            #pasar dos misionero
            if h['label'][0]<=1 and h['label'][2]=='D':
                aux=h['label'][:]
                aux[0]=aux[0]+2
                aux[2]='I'
                if (aux[0]!=0 and aux[0]< aux[1]) or (aux[0]!=3 and aux[0]> aux[1]):
                    h['adyacentes'].append({'label':aux , 'FIN':True})
                else:
                    h['adyacentes'].append({'label':aux , 'FIN':False})

                    
            #devolver dos misionero
            if h['label'][0]>=2 and h['label'][2]=='I':
                aux=h['label'][:]
                aux[0]=aux[0]-2
                aux[2]='D'
                if (aux[0]!=0 and aux[0]< aux[1]) or (aux[0]!=3 and aux[0]> aux[1]):
                    h['adyacentes'].append({'label':aux , 'FIN':True})
                else:
                    h['adyacentes'].append({'label':aux , 'FIN':False})
            
            #pasar un misionero y un canibal
            if h['label'][0]<3 and h['label'][1]<3 and h['label'][2]=='D':
                aux=h['label'][:]
                aux[0]=aux[0]+1
                aux[1]=aux[1]+1
                aux[2]='I'
                if (aux[0]!=0 and aux[0]< aux[1]) or (aux[0]!=3 and aux[0]> aux[1]):
                    h['adyacentes'].append({'label':aux , 'FIN':True})
                else:
                    h['adyacentes'].append({'label':aux , 'FIN':False})

            #devolver un misionero y un canibal
            if h['label'][0]>0 and h['label'][1]>0 and h['label'][2]=='I':
                
                aux=h['label'][:]
                aux[0]=aux[0]-1
                aux[1]=aux[1]-1
                aux[2]='D'
                if (aux[0]!=0 and aux[0]< aux[1]) or (aux[0]!=3 and aux[0]> aux[1]):
                    h['adyacentes'].append({'label':aux , 'FIN':True})
                else:
                    h['adyacentes'].append({'label':aux , 'FIN':False})
            
            
                        
        
            for j in h['adyacentes']:
                if self.in_graph_cannibal(j['label']):
                    continue
                else:
                    self.cannibal['graph'].append({'label':j['label'],'FIN':j['FIN'],
                                   'adyacentes':[], 'done': False,'x':random.randint(10, 1100),'y':random.randint(10, 500)})

            for i in self.cannibal['graph']:
                if not i['done']:
                    i['done']=True
                    if not i['FIN']:
                        self.generate_cannibal_r(i)    
