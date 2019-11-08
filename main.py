# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 15:08:08 2019

@author: ayuwoki
"""
import json
from GUI import GUI
from graph import graph
from generate_graph import generate_graph
def main():

    oveja = {}
    gr=generate_graph(oveja)
    #gr.generate_cannibal()
    #gr.generate_sheep()
    gr.generate_sheep()
    
    with open('oveja.json') as file:
        data =json.load(file)
        
    t=data['graph']
    s=data['estado_inicial']
    u=data['estado_aceptacion']
    g=graph(t,s,u)
    
    copyg=g
    aux=gr.call_return_path(copyg,copyg.graph[0])
    print('CAMINOOOO -----', aux)
    for h in gr.path:
        print('--',h,'\n')
    aux=gr.return_path_pos(copyg)
    print(aux)
    print(aux[0][1])
    
    gui=GUI(g,gr)
    

    
    gui.window()
    

if __name__== "__main__":
    main()