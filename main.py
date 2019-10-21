# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 15:08:08 2019

@author: ayuwoki
"""
import json
from generate_graph import generate_graph
def main():

  #  with open('oveja.json','r') as file:
       # data =json.load(file)
        #aux=data['dominio'].append({'nombre':'jose jose'})
        #print(aux)
    oveja = {}
    gr=generate_graph(oveja)
    gr.generate_sheep()
    

if __name__== "__main__":
    main()