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
        self.knight=ov
        self.family=ov
        self.horse=ov
        self.boy=ov
        
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
    
    def in_graph_knight(self,x):
        for h in self.knight['graph']:
            if x==h['label']:
                return True
        return False
    
    def in_graph_boy(self,x):
        for h in self.boy['graph']:
            if x==h['label']:
                return True
        return False
    def in_graph_horse(self,x):
        for h in self.horse['graph']:
            if x==h['label']:
                return True
        return False

    def in_graph_family(self,x):
        for h in self.family['graph']:
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
                        
        
    def generate_knight(self):
            self.knight['estado_inicial'] =[]
            self.knight['estado_aceptacion'] =[]
            self.knight['graph']=[]
            self.knight['transiciones'] = []
            self.knight['estado_inicial'].append([0,0,0,0])
            self.knight['estado_aceptacion'].append([1,1,1,1])
        
            self.knight['graph'].append({'label':[0,0,0,0],'FIN':False,
                                   'adyacentes':[], 'done':True,'x':random.randint(10, 1100),'y':random.randint(10, 500)})
            
            self.generate_knight_r(self.knight['graph'][0])
    
            with open('knight.json', 'w') as outfile:
                json.dump(self.knight, outfile)
                
    def generate_knight_r(self,h):
            print('what?', h,'\n')
            
            #condicion de escape
            for k in  self.knight['graph']:
                if k['label']==[1,1,1,1]:
                    return
        
            #pasar arrogante
            if h['label'][0]==0:
                if h['label'][1]==h['label'][2] or h['label'][1]==h['label'][3]:
                    aux=h['label'][:]
                    aux[0]=1
                    h['adyacentes'].append({'label':aux , 'FIN':False})
            #pasar un valiente C
            if h['label'][2]==0:
                if h['label'][1]==h['label'][0] or h['label'][1]==h['label'][3]:
                    aux=h['label'][:]
                    aux[2]=1
                    h['adyacentes'].append({'label':aux , 'FIN':False})
            
            #pasar otro valiente D
            if h['label'][3]==0:
                if h['label'][1]==h['label'][0] or h['label'][1]==h['label'][2]:
                    aux=h['label'][:]
                    aux[3]=1
                    h['adyacentes'].append({'label':aux , 'FIN':False})
 
           #pasar valiente C con vago
            if h['label'][1]==0 and h['label'][2]==0:
                aux=h['label'][:]
                aux[1]=1
                aux[2]=1
                h['adyacentes'].append({'label':aux , 'FIN':False})
            
            #pasar valiente D con vago
            if h['label'][0]==0 and h['label'][3]==0:
                aux=h['label'][:]
                aux[1]=1
                aux[3]=1
                h['adyacentes'].append({'label':aux , 'FIN':False})
            
            #pasar C con D
            if h['label'][2]==0 and h['label'][3]==0:
                if h['label'][1]==h['label'][0]:
                    aux=h['label'][:]
                    aux[2]=1
                    aux[3]=1
                    h['adyacentes'].append({'label':aux , 'FIN':False})
            
            #devolver arrogante
            if h['label'][0]==1:
                if h['label'][1]==h['label'][2] or h['label'][1]==h['label'][3]:
                    aux=h['label'][:]
                    aux[0]=0
                    h['adyacentes'].append({'label':aux , 'FIN':False})
                
            #devolver valiente C
            if h['label'][2]==1:
                if h['label'][1]==h['label'][0] or h['label'][1]==h['label'][3]:
                    aux=h['label'][:]
                    aux[2]=0
                    h['adyacentes'].append({'label':aux , 'FIN':False})
            
            #devolver valiente D
            if h['label'][3]==1:
                if h['label'][1]==h['label'][0] or h['label'][1]==h['label'][2]:
                    aux=h['label'][:]
                    aux[3]=0
                    h['adyacentes'].append({'label':aux , 'FIN':False}) 
                    
            #devolver valiente C con vago
            if h['label'][1]==1 and h['label'][2]==1:
                aux=h['label'][:]
                aux[1]=0
                aux[2]=0
                h['adyacentes'].append({'label':aux , 'FIN':False})
            
            #devolver valiente D con vago
            if h['label'][1]==1 and h['label'][3]==1:
                aux=h['label'][:]
                aux[1]=0
                aux[3]=0
                h['adyacentes'].append({'label':aux , 'FIN':False})
                
            #devolver C con D
            if h['label'][2]==1 and h['label'][3]==1:
                if h['label'][1]==h['label'][0]:
                    aux=h['label'][:]
                    aux[2]=0
                    aux[3]=0
                    h['adyacentes'].append({'label':aux , 'FIN':False})
        
            for j in h['adyacentes']:
                if self.in_graph_knight(j['label']):
                    continue
                else:
                    self.knight['graph'].append({'label':j['label'],'FIN':j['FIN'],
                                   'adyacentes':[], 'done': False , 'x':random.randint(10, 1100),'y':random.randint(10, 500)})

            for i in self.knight['graph']:
                if not i['done']:
                    i['done']=True
                    if not i['FIN']:
                        self.generate_knight_r(i)
                        
    def generate_boy(self):
            self.boy['estado_inicial'] =[]
            self.boy['estado_aceptacion'] =[]
            self.boy['graph']=[]
            self.boy['transiciones'] = []
            self.boy['estado_inicial'].append([0,0,0,0])
            self.boy['estado_aceptacion'].append([1,1,1,1])
        
            self.boy['graph'].append({'label':[0,0,0,0],'FIN':False,
                                   'adyacentes':[], 'done':True,'x':random.randint(10, 1100),'y':random.randint(10, 500)})
            
            self.generate_boy_r(self.boy['graph'][0])
    
            with open('boy.json', 'w') as outfile:
                json.dump(self.boy, outfile)
                
    def generate_boy_r(self,h):
            print('what?', h,'\n')
            
            #condicion de escape
            for k in  self.boy['graph']:
                if k['label']==[1,1,1,1]:
                    return
        
            #pasar A
            if h['label'][0]==0:
                aux=h['label'][:]
                aux[0]=1
                h['adyacentes'].append({'label':aux , 'FIN':False})
            #pasar B
            if h['label'][1]==0:
                aux=h['label'][:]
                aux[1]=1
                h['adyacentes'].append({'label':aux , 'FIN':False})
            
            #pasar C
            if h['label'][2]==0:
                aux=h['label'][:]
                aux[2]=1
                h['adyacentes'].append({'label':aux , 'FIN':False})
        
            #pasar D
            if h['label'][3]==0:
                aux=h['label'][:]
                aux[3]=1
                h['adyacentes'].append({'label':aux , 'FIN':False})
 
           #pasar AB
            if h['label'][0]==0 and h['label'][1]==0:
                aux=h['label'][:]
                aux[0]=1
                aux[1]=1
                h['adyacentes'].append({'label':aux , 'FIN':False})
                
            #devolver A
            if h['label'][0]==1:
                aux=h['label'][:]
                aux[0]=0
                h['adyacentes'].append({'label':aux , 'FIN':False})
            #devolver B
            if h['label'][1]==1:
                aux=h['label'][:]
                aux[1]=0
                h['adyacentes'].append({'label':aux , 'FIN':False})
            
            #devolver C
            if h['label'][2]==1:
                aux=h['label'][:]
                aux[2]=0
                h['adyacentes'].append({'label':aux , 'FIN':False})
        
            #devolver D
            if h['label'][3]==1:
                aux=h['label'][:]
                aux[3]=0
                h['adyacentes'].append({'label':aux , 'FIN':False})
 
           #devolver AB
            if h['label'][0]==1 and h['label'][1]==1:
                aux=h['label'][:]
                aux[0]=0
                aux[1]=0
                h['adyacentes'].append({'label':aux , 'FIN':False})
            
        
            for j in h['adyacentes']:
                if self.in_graph_boy(j['label']):
                    continue
                else:
                    self.boy['graph'].append({'label':j['label'],'FIN':j['FIN'],
                                   'adyacentes':[], 'done': False , 'x':random.randint(10, 1100),'y':random.randint(10, 500)})

            for i in self.boy['graph']:
                if not i['done']:
                    i['done']=True
                    if not i['FIN']:
                        self.generate_boy_r(i)
            
    def generate_family(self):
            self.family['estado_inicial'] =[]
            self.family['estado_aceptacion'] =[]
            self.family['graph']=[]
            self.family['transiciones'] = []
            self.family['estado_inicial'].append([0,0,0,0,0])
            self.family['estado_aceptacion'].append([1,1,1,1,1])
        
            self.family['graph'].append({'label':[0,0,0,0,0],'FIN':False,
                                   'adyacentes':[], 'done':True,'x':random.randint(10, 1100),'y':random.randint(10, 500)})
            
            self.generate_family_r(self.family['graph'][0])
    
            with open('family.json', 'w') as outfile:
                json.dump(self.family, outfile)
                
    def generate_family_r(self,h):
            print('what?', h,'\n')
            
            #condicion de escape
            for k in  self.family['graph']:
                if k['label']==[1,1,1,1]:
                    return
        
            #pasar A
            if h['label'][0]==0:
                aux=h['label'][:]
                aux[0]=1
                h['adyacentes'].append({'label':aux , 'FIN':False})
            #pasar B
            if h['label'][1]==0:
                aux=h['label'][:]
                aux[1]=1
                h['adyacentes'].append({'label':aux , 'FIN':False})
            
            #pasar C
            if h['label'][2]==0:
                aux=h['label'][:]
                aux[2]=1
                h['adyacentes'].append({'label':aux , 'FIN':False})
        
            #pasar D
            if h['label'][3]==0:
                aux=h['label'][:]
                aux[3]=1
                h['adyacentes'].append({'label':aux , 'FIN':False})
 
           #pasar AB
            if h['label'][0]==0 and h['label'][1]==0:
                aux=h['label'][:]
                aux[0]=1
                aux[1]=1
                h['adyacentes'].append({'label':aux , 'FIN':False})
                
            #devolver A
            if h['label'][0]==1:
                aux=h['label'][:]
                aux[0]=0
                h['adyacentes'].append({'label':aux , 'FIN':False})
            #devolver B
            if h['label'][1]==1:
                aux=h['label'][:]
                aux[1]=0
                h['adyacentes'].append({'label':aux , 'FIN':False})
            
            #devolver C
            if h['label'][2]==1:
                aux=h['label'][:]
                aux[2]=0
                h['adyacentes'].append({'label':aux , 'FIN':False})
        
            #devolver D
            if h['label'][3]==1:
                aux=h['label'][:]
                aux[3]=0
                h['adyacentes'].append({'label':aux , 'FIN':False})
 
           #devolver AB
            if h['label'][0]==1 and h['label'][1]==1:
                aux=h['label'][:]
                aux[0]=0
                aux[1]=0
                h['adyacentes'].append({'label':aux , 'FIN':False})
            
        
            for j in h['adyacentes']:
                if self.in_graph_boy(j['label']):
                    continue
                else:
                    self.boy['graph'].append({'label':j['label'],'FIN':j['FIN'],
                                   'adyacentes':[], 'done': False , 'x':random.randint(10, 1100),'y':random.randint(10, 500)})

            for i in self.boy['graph']:
                if not i['done']:
                    i['done']=True
                    if not i['FIN']:
                        self.generate_boy_r(i)
                        
                        
                        
                        
                        
        
    '''def generate_horse(self):
            self.horse['estado_inicial'] =[]
            self.horse['estado_aceptacion'] =[]
            self.horse['graph']=[]
            self.horse['transiciones'] = []
            self.horse['estado_inicial'].append([[0,0,0,0],[0,0,0,0],[0,0,0,0],[-1,0,0,-1],[-1,1,3,-1]])
            self.horse['estado_aceptacion'].append([[1,1,1,1],[1,1,1,1],[1,1,1,1],[-1,1,1,-1]])
        
            self.horse['graph'].append({'label':[[0,0,0,0],[0,0,0,0],[0,0,0,0],[-1,0,0,-1],[-1,1,3,-1]] ,'FIN':False,
                                   'adyacentes':[], 'done':True,'x':random.randint(10, 1100),'y':random.randint(10, 500)})
            
            self.generate_horse_r(self.horse['graph'][0])
    
            with open('horse.json', 'w') as outfile:
                json.dump(self.horse, outfile)
                        
    def generate_horse_r(self,h):
            
            #condicion de escape
            for k in  self.horse['graph']:
                if k['label'][0]==[1,1,1,1] and k['label'][1]==[1,1,1,1] and k['label'][2]==[1,1,1,1] and k['label'][3]==[-1,1,1,-1]:
                    return
        
            i=h['label'][4][1]
            j=h['label'][4][2]
            #izquierda arriba
            if i>=1 and j>=2 and h['label'][i-1][j-2]!=-1:
                aux=h['label'][:]
                aux[i][j]=1
                aux[4][1]=aux[4][1]-1
                aux[4][2]=aux[4][2]-2
                i=i-1
                j=j-2
                aux[i][j]=1
                if h['label'][i][j]==0:
                    h['adyacentes'].append({'label':aux , 'FIN':False})
                if h['label'][i][j]==1:
                    h['adyacentes'].append({'label':aux , 'FIN':True})
                    
            #izquierda abajo
            if i<=2 and j>=2 and h['label'][i+1][j-2]!=-1:
                aux=h['label'][:]
                aux[i][j]=1
                aux[4][1]=aux[4][1]+1
                aux[4][2]=aux[4][2]-2
                i=i+1
                j=j-2
                aux[i][j]=1
                if h['label'][i][j]==0:
                    h['adyacentes'].append({'label':aux , 'FIN':False})
                if h['label'][i][j]==1:
                    h['adyacentes'].append({'label':aux , 'FIN':True})
                    
            #erecha arriba
            if i>=1 and j<=1 and h['label'][i-1][j+2]!=-1:
                aux=h['label'][:]
                aux[i][j]=1
                aux[4][1]=aux[4][1]-1
                aux[4][2]=aux[4][2]+2
                i=i-1
                j=j+2
                aux[i][j]=1
                if h['label'][i][j]==0:
                    h['adyacentes'].append({'label':aux , 'FIN':False})
                if h['label'][i][j]==1:
                    h['adyacentes'].append({'label':aux , 'FIN':True})
                    
            #derecha abajo
            if i<=2 and j<=1 and h['label'][i+1][j+2]!=-1:
                aux=h['label'][:]
                aux[i][j]=1
                aux[4][1]=aux[4][1]+1
                aux[4][2]=aux[4][2]+2
                i=i+1
                j=j+2
                aux[i][j]=1
                if h['label'][i][j]==0:
                    h['adyacentes'].append({'label':aux , 'FIN':False})
                if h['label'][i][j]==1:
                    h['adyacentes'].append({'label':aux , 'FIN':True})
                    
            #abajo derecha 1
            if i==0 and j<=2 and h['label'][i+2][j+1]!=-1:
                aux=h['label'][:]
                aux[i][j]=1
                aux[4][1]=aux[4][1]+2
                aux[4][2]=aux[4][2]+1
                i=i+2
                j=j+1
                aux[i][j]=1
                if h['label'][i][j]==0:
                    h['adyacentes'].append({'label':aux , 'FIN':False})
                if h['label'][i][j]==1:
                    h['adyacentes'].append({'label':aux , 'FIN':True})
            
            #abajo derecha 2
            if i==1 and j==1 and h['label'][i+2][j+1]!=-1:
                aux=h['label'][:]
                aux[i][j]=1
                aux[4][1]=aux[4][1]+2
                aux[4][2]=aux[4][2]+1
                i=i+2
                j=j+1
                aux[i][j]=1
                if h['label'][i][j]==0:
                    h['adyacentes'].append({'label':aux , 'FIN':False})
                if h['label'][i][j]==1:
                    h['adyacentes'].append({'label':aux , 'FIN':True})
            
            #abajo izquierda 1
            if i==0 and (j>=1 and j<=3) and h['label'][i+2][j-1]!=-1:
                aux=h['label'][:]
                aux[i][j]=1
                aux[4][1]=aux[4][1]+2
                aux[4][2]=aux[4][2]-1
                i=i+2
                j=j-1
                aux[i][j]=1
                if h['label'][i][j]==0:
                    h['adyacentes'].append({'label':aux , 'FIN':False})
                if h['label'][i][j]==1:
                    h['adyacentes'].append({'label':aux , 'FIN':True})
            
            #abajo izquierda 2
            if i==1 and j==2 and h['label'][i+2][j-1]!=-1:
                aux=h['label'][:]
                aux[i][j]=1
                aux[4][1]=aux[4][1]+2
                aux[4][2]=aux[4][2]-1
                i=i+2
                j=j-1
                aux[i][j]=1
                if h['label'][i][j]==0:
                    h['adyacentes'].append({'label':aux , 'FIN':False})
                if h['label'][i][j]==1:
                    h['adyacentes'].append({'label':aux , 'FIN':True})
                    
            #arriba derecha 1
            if i==2 and j<=2 and h['label'][i-2][j+1]!=-1:
                aux=h['label'][:]
                aux[i][j]=1
                aux[4][1]=aux[4][1]-2
                aux[4][2]=aux[4][2]+1
                i=i-2
                j=j+1
                aux[i][j]=1
                if h['label'][i][j]==0:
                    h['adyacentes'].append({'label':aux , 'FIN':False})
                if h['label'][i][j]==1:
                    h['adyacentes'].append({'label':aux , 'FIN':True})
            
            #arriba derecha 2
            if i==3 and (j==1 or j==2) and h['label'][-+2][j+1]!=-1:
                aux=h['label'][:]
                aux[i][j]=1
                aux[4][1]=aux[4][1]-2
                aux[4][2]=aux[4][2]+1
                i=i-2
                j=j+1
                aux[i][j]=1
                if h['label'][i][j]==0:
                    h['adyacentes'].append({'label':aux , 'FIN':False})
                if h['label'][i][j]==1:
                    h['adyacentes'].append({'label':aux , 'FIN':True})
                    
            #arriba izquierda 1
            if i==2 and (j>=1 and j<=3) and h['label'][i-2][j-1]!=-1:
                aux=h['label'][:]
                aux[i][j]=1
                aux[4][1]=aux[4][1]-2
                aux[4][2]=aux[4][2]-1
                i=i-2
                j=j-1
                aux[i][j]=1
                if h['label'][i][j]==0:
                    h['adyacentes'].append({'label':aux , 'FIN':False})
                if h['label'][i][j]==1:
                    h['adyacentes'].append({'label':aux , 'FIN':True})
            
            #arriba izquierda 2
            if i==3 and (j==1 or j==2) and h['label'][i-2][j-1]!=-1:
                aux=h['label'][:]
                aux[i][j]=1
                aux[4][1]=aux[4][1]-2
                aux[4][2]=aux[4][2]-1
                i=i-2
                j=j-1
                aux[i][j]=1
                if h['label'][i][j]==0:
                    h['adyacentes'].append({'label':aux , 'FIN':False})
                if h['label'][i][j]==1:
                    h['adyacentes'].append({'label':aux , 'FIN':True})
                    
 
        
            for j in h['adyacentes']:
                if self.in_graph_horse(j['label']):
                    print('entrada 1')
                    continue
                else:
                    print('entrada 2')
                    self.horse['graph'].append({'label':j['label'],'FIN':j['FIN'],
                                   'adyacentes':[], 'done': False , 'x':random.randint(10, 1100),'y':random.randint(10, 500)})

            for i in self.horse['graph']:
                print('entrada 3')
                if not i['done']:
                    i['done']=True
                    if not i['FIN']:
                        print('entrada 4')
                        self.generate_horse_r(i)'''
                        
                        
    '''def generate_family(self):
            self.tiempo = 30
            self.family['estado_inicial'] =[]
            self.family['estado_aceptacion'] =[]
            self.family['graph']=[]
            self.family['transiciones'] = []
            self.family['estado_inicial'].append([30,'D','D','D','D','D','D'])
            self.family['estado_aceptacion'].append(['x','I','I','I','I','I','I'])
        
            self.family['graph'].append({'label':[30,'D','D','D','D','D','D'],'FIN':False,
                                   'adyacentes':[], 'done':True,'x':random.randint(10, 1100),'y':random.randint(10, 500)})
            
            self.generate_family_r(self.family['graph'][0])
            
            for h in self.family['graph']:
                print('Label: ', h['label'], h['FIN'])
                for i in h['adyacentes']:
                    print('          adyacentes: ', i['label'] ,i['FIN'])
    
            with open('family.json', 'w') as outfile:
                json.dump(self.family, outfile)
                
                
                
    def generate_family_r(self,h):
            print('what?', h,'\n')
            aux=[]
            p=0    
            #condicion de escape
            for k in  self.family['graph']:
                for l in k['label']:
                    if p>0:
                        aux.append(l)
                    p+=1
                if aux==['I','I','I','I','I','I']:
                    return
        
            #pasar A
            if (h['label'][1]=='D' and h['label'][6]=='D') or (h['label'][1]=='I' and h['label'][6] == 'I'):
                aux=h['label'][:]
                aux[0]=aux[0]-1
                if h['label'][5] == 'D':
                    aux[6] = 'I'
                    aux[1] = 'I'
                else:
                    aux[6] = 'D'
                    aux[1] = 'D'
                    
                if aux[0] > 0 :
                     h['adyacentes'].append({'label':aux , 'FIN':False})
                
                else:
                     h['adyacentes'].append({'label':aux , 'FIN':True})
                    
            #pasar B
            if (h['label'][2]=='D' and h['label'][6]=='D') or (h['label'][2]=='I' and h['label'][6] == 'I'):
                aux=h['label'][:]
                aux[0]=aux[0]-3
                if h['label'][6] == 'D':
                    aux[6] = 'I'
                    aux[2] = 'I'
                else:
                    aux[6] = 'D'
                    aux[2] = 'D'
                    
                if aux[0] > 0 :
                     h['adyacentes'].append({'label':aux , 'FIN':False})
                
                else:
                     h['adyacentes'].append({'label':aux , 'FIN':True})
                    
            #pasar c
            if (h['label'][3]=='D' and h['label'][6]=='D') or (h['label'][3]=='I' and h['label'][6] == 'I'):
                aux=h['label'][:]
                aux[0]=aux[0]-6
                if h['label'][6] == 'D':
                    aux[6] = 'I'
                    aux[3] = 'I'
                else:
                    aux[6] = 'D'
                    aux[3] = 'D'
                    
                if aux[0] > 0 :
                     h['adyacentes'].append({'label':aux , 'FIN':False})
                
                else:
                     h['adyacentes'].append({'label':aux , 'FIN':True})
                    
                
            #pasar D
            if (h['label'][4]=='D' and h['label'][6]=='D') or (h['label'][4]=='I' and h['label'][6] == 'I'):
                aux=h['label'][:]
                aux[0]=aux[0]-8
                if h['label'][6] == 'D':
                    aux[6] = 'I'
                    aux[4] = 'I'
                else:
                    aux[6] = 'D'
                    aux[4] = 'D'
                    
                if aux[0] > 0 :
                     h['adyacentes'].append({'label':aux , 'FIN':False})
                
                else:
                     h['adyacentes'].append({'label':aux , 'FIN':True})
                    
            
            #pasar E
            if (h['label'][5]=='D' and h['label'][6]=='D') or (h['label'][5]=='I' and h['label'][6] == 'I'):
                aux=h['label'][:]
                aux[0]-12
                if h['label'][6] == 'D':
                    aux[6] = 'I'
                    aux[5] = 'I'
                else:
                    aux[6] = 'D'
                    aux[5] = 'D'
                    
                if aux[0] > 0 :
                     h['adyacentes'].append({'label':aux , 'FIN':False})
                
                else:
                     h['adyacentes'].append({'label':aux , 'FIN':True})
                    
            
            #pasar AB
            if (h['label'][1]=='D' and h['label'][2]=='D' and h['label'][6]=='D') or (h['label'][1]=='I' and h['label'][2]=='I' and h['label'][6] == 'I'):
                aux=h['label'][:]
                aux[0]=aux[0]-3
                if h['label'][6] == 'D':
                    aux[6] = 'I'
                    aux[1] = 'I'
                    aux[2] = 'I'
                else:
                    aux[6] = 'D'
                    aux[1] = 'D'
                    aux[2] = 'D'
                    
                if aux[0] > 0 :
                     h['adyacentes'].append({'label':aux , 'FIN':False})
                
                else:
                     h['adyacentes'].append({'label':aux , 'FIN':True})
                     
             #pasar AC
            if (h['label'][1]=='D' and h['label'][3]=='D' and h['label'][6]=='D') or (h['label'][1]=='I' and h['label'][3]=='I' and h['label'][6] == 'I'):
                aux=h['label'][:]
                aux[0]=aux[0]-6
                if h['label'][6] == 'D':
                    aux[6] = 'I'
                    aux[1] = 'I'
                    aux[3] = 'I'
                else:
                    aux[6] = 'D'
                    aux[1] = 'D'
                    aux[3] = 'D'
                    
                if aux[0] > 0 :
                     h['adyacentes'].append({'label':aux , 'FIN':False})
                
                else:
                     h['adyacentes'].append({'label':aux , 'FIN':True})

            #pasar AD
            if (h['label'][1]=='D' and h['label'][4]=='D' and h['label'][6]=='D') or (h['label'][1]=='I' and h['label'][5]=='I' and h['label'][6] == 'I'):
                aux=h['label'][:]
                aux[0]=aux[0]-8
                if h['label'][6] == 'D':
                    aux[6] = 'I'
                    aux[1] = 'I'
                    aux[4] = 'I'
                else:
                    aux[6] = 'D'
                    aux[1] = 'D'
                    aux[4] = 'D'
                    
                if aux[0] > 0 :
                     h['adyacentes'].append({'label':aux , 'FIN':False})
                
                else:
                     h['adyacentes'].append({'label':aux , 'FIN':True})
                     
            #pasar AE
            if (h['label'][1]=='D' and h['label'][5]=='D' and h['label'][6]=='D') or (h['label'][1]=='I' and h['label'][5]=='I' and h['label'][6] == 'I'):
                aux=h['label'][:]
                aux[0]=aux[0]-12
                if h['label'][6] == 'D':
                    aux[6] = 'I'
                    aux[1] = 'I'
                    aux[5] = 'I'
                else:
                    aux[6] = 'D'
                    aux[1] = 'D'
                    aux[5] = 'D'
                    
                if aux[0] > 0 :
                     h['adyacentes'].append({'label':aux , 'FIN':False})
                
                else:
                     h['adyacentes'].append({'label':aux , 'FIN':True})
                     
            #pasar BC
            if (h['label'][2]=='D' and h['label'][3]=='D' and h['label'][6]=='D') or (h['label'][2]=='I' and h['label'][3]=='I' and h['label'][6] == 'I'):
                aux=h['label'][:]
                aux[0]=aux[0]-6
                if h['label'][6] == 'D':
                    aux[6] = 'I'
                    aux[1] = 'I'
                    aux[3] = 'I'
                else:
                    aux[6] = 'D'
                    aux[1] = 'D'
                    aux[3] = 'D'
                    
                if aux[0] > 0 :
                     h['adyacentes'].append({'label':aux , 'FIN':False})
                
                else:
                     h['adyacentes'].append({'label':aux , 'FIN':True})
                     
            #pasar BD
            if (h['label'][2]=='D' and h['label'][4]=='D' and h['label'][6]=='D') or (h['label'][2]=='I' and h['label'][4]=='I' and h['label'][6] == 'I'):
                aux=h['label'][:]
                aux[0]=aux[0]-8
                if h['label'][6] == 'D':
                    aux[6] = 'I'
                    aux[2] = 'I'
                    aux[4] = 'I'
                else:
                    aux[6] = 'D'
                    aux[2] = 'D'
                    aux[4] = 'D'
                    
                if aux[0] > 0 :
                     h['adyacentes'].append({'label':aux , 'FIN':False})
                
                else:
                     h['adyacentes'].append({'label':aux , 'FIN':True})
        
        
            #pasar BE
            if (h['label'][2]=='D' and h['label'][5]=='D' and h['label'][6]=='D') or (h['label'][2]=='I' and h['label'][5]=='I' and h['label'][6] == 'I'):
                aux=h['label'][:]
                aux[0]=aux[0]-12
                if h['label'][6] == 'D':
                    aux[6] = 'I'
                    aux[2] = 'I'
                    aux[5] = 'I'
                else:
                    aux[6] = 'D'
                    aux[2] = 'D'
                    aux[5] = 'D'
                    
                if aux[0] > 0 :
                     h['adyacentes'].append({'label':aux , 'FIN':False})
                
                else:
                     h['adyacentes'].append({'label':aux , 'FIN':True})
        
            #pasar CD
            if (h['label'][3]=='D' and h['label'][4]=='D' and h['label'][6]=='D') or (h['label'][3]=='I' and h['label'][4]=='I' and h['label'][6] == 'I'):
                aux=h['label'][:]
                aux[0]=aux[0]-8
                if h['label'][6] == 'D':
                    aux[6] = 'I'
                    aux[3] = 'I'
                    aux[4] = 'I'
                else:
                    aux[6] = 'D'
                    aux[3] = 'D'
                    aux[4] = 'D'
                    
                if aux[0] > 0 :
                     h['adyacentes'].append({'label':aux , 'FIN':False})
                
                else:
                     h['adyacentes'].append({'label':aux , 'FIN':True})
                     
            #pasar CE
            if (h['label'][3]=='D' and h['label'][5]=='D' and h['label'][6]=='D') or (h['label'][3]=='I' and h['label'][5]=='I' and h['label'][6] == 'I'):
                aux=h['label'][:]
                aux[0]=aux[0]-12
                if h['label'][6] == 'D':
                    aux[6] = 'I'
                    aux[3] = 'I'
                    aux[5] = 'I'
                else:
                    aux[6] = 'D'
                    aux[3] = 'D'
                    aux[5] = 'D'
                    
                if aux[0] < 12 :
                     h['adyacentes'].append({'label':aux , 'FIN':False})
                
                else:
                     h['adyacentes'].append({'label':aux , 'FIN':True})
                     
            #pasar DE
            if (h['label'][4]=='D' and h['label'][5]=='D' and h['label'][6]=='D') or (h['label'][4]=='I' and h['label'][5]=='I' and h['label'][6] == 'I'):
                aux=h['label'][:]
                aux[0]=aux[0]-12
                if h['label'][6] == 'D':
                    aux[6] = 'I'
                    aux[4] = 'I'
                    aux[5] = 'I'
                else:
                    aux[6] = 'D'
                    aux[4] = 'D'
                    aux[5] = 'D'
                    
                if aux[0] < 12 :
                     h['adyacentes'].append({'label':aux , 'FIN':False})
                
                else:
                     h['adyacentes'].append({'label':aux , 'FIN':True})
                     
                     
                     
                     
        
            for j in h['adyacentes']:
                if self.in_graph_family(j['label']):
                    continue
                else:
                    self.family['graph'].append({'label':j['label'],'FIN':j['FIN'],
                                   'adyacentes':[], 'done': False,'x':random.randint(10, 1100),'y':random.randint(10, 500)})

            for i in self.family['graph']:
                if not i['done']:
                    i['done']=True
                    if not i['FIN']:
                        self.generate_family_r(i)'''    
