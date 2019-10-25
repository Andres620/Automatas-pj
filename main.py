# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 15:08:08 2019

@author: ayuwoki
"""
import json
from GUI import GUI
from generate_graph import generate_graph
def main():

    oveja = {}
    gr=generate_graph(oveja)
    gr.generate_cannibal()
    #gr.generate_sheep()
    
    with open('cannibal.json') as file:
        data =json.load(file)
        
    graph=data['graph']
    
    print('ijole ',graph)
    gui=GUI(graph)

    
    gui.window()
    

if __name__== "__main__":
    main()