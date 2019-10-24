# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 15:08:08 2019

@author: ayuwoki
"""
import json
from generate_graph import generate_graph
def main():
    #oveja = {}
    #gr=generate_graph(oveja)
    #gr.generate_sheep()
    sapo = {}
    
    gr = generate_graph(sapo)
 
    gr.generate_frog()
    

if __name__== "__main__":
    main()