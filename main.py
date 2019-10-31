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
    gr.generate_knight()
    
    with open('knight.json') as file:
        data =json.load(file)
        
    t=data['graph']
    g=graph(t)
    print('ijole ',g)
    gui=GUI(g)

    
    gui.window()
    

if __name__== "__main__":
    main()