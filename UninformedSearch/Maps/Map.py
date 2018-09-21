#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 19:29:51 2018

@author: raphael.ribeiro

Map of cities.
"""
import sys
sys.path.append("../Data")
from City import City

class Map(object):
    #vertixs
    portoUniao = City('Porto União')
    pauloFrontin = City('Paulo Frontin')
    canoinhas = City('Canoinhas')
    irati = City('Irati')
    palmeira = City('Palmeira')
    campoLargo = City('Campo Largo')
    curitiba = City('Curitiba')
    balsaNova = City('Balsa Nova')
    araucaria = City('Auracaria')
    saoJose = City('São Jośe')
    contenda = City('Contenda')
    mafra = City('Mafra')
    tijucas = City('Tijucas do Sul')
    lapa = City('Lapa')
    saoMateus = City('São Mateus do Sul')
    tresBarras = City('Três Barras')
    
    portoUniao.addCityAdjacent(pauloFrontin)
    portoUniao.addCityAdjacent(canoinhas)
    portoUniao.addCityAdjacent(saoMateus)
    
    pauloFrontin.addCityAdjacent(irati)
    pauloFrontin.addCityAdjacent(portoUniao)

    canoinhas.addCityAdjacent(tresBarras)
    canoinhas.addCityAdjacent(mafra)
    canoinhas.addCityAdjacent(portoUniao)
    
    irati.addCityAdjacent(pauloFrontin)
    irati.addCityAdjacent(palmeira)
    irati.addCityAdjacent(saoMateus)
    
    palmeira.addCityAdjacent(irati)
    palmeira.addCityAdjacent(saoMateus)
    palmeira.addCityAdjacent(campoLargo)
    
    campoLargo.addCityAdjacent(palmeira)
    campoLargo.addCityAdjacent(balsaNova)
    campoLargo.addCityAdjacent(curitiba)
    
    curitiba.addCityAdjacent(campoLargo)
    curitiba.addCityAdjacent(balsaNova)
    curitiba.addCityAdjacent(araucaria)
    curitiba.addCityAdjacent(saoJose)
    
    balsaNova.addCityAdjacent(curitiba)
    balsaNova.addCityAdjacent(campoLargo)
    balsaNova.addCityAdjacent(contenda)
    
    araucaria.addCityAdjacent(curitiba)
    araucaria.addCityAdjacent(contenda)

    saoJose.addCityAdjacent(curitiba)
    saoJose.addCityAdjacent(tijucas)
    
    contenda.addCityAdjacent(balsaNova)
    contenda.addCityAdjacent(araucaria)
    contenda.addCityAdjacent(lapa)
    
    mafra.addCityAdjacent(tijucas)
    mafra.addCityAdjacent(lapa)
    mafra.addCityAdjacent(canoinhas)
    
    tijucas.addCityAdjacent(mafra)
    tijucas.addCityAdjacent(saoJose)
    
    lapa.addCityAdjacent(contenda)
    lapa.addCityAdjacent(saoMateus)
    lapa.addCityAdjacent(mafra)
    
    saoMateus.addCityAdjacent(palmeira)
    saoMateus.addCityAdjacent(irati)
    saoMateus.addCityAdjacent(lapa)
    saoMateus.addCityAdjacent(tresBarras)
    saoMateus.addCityAdjacent(portoUniao)
    
    tresBarras.addCityAdjacent(saoMateus)
    tresBarras.addCityAdjacent(canoinhas)