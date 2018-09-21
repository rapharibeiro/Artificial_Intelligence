#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 16:37:31 2018

@author: raphael.ribeiro
Map of cities with value in straight line.
Adjacent with real distance value.
"""

import sys
sys.path.append("../Data")
from City import City
from AdjacentDistance import AdjacentDistance

class Map(object):
    # vértices
    portoUniao = City('Porto União', 203)
    pauloFrontin = City('Paulo Frontin', 172)
    canoinhas = City('Canoinhas', 141)
    irati = City('Irati', 139)
    palmeira = City('Palmeira', 59)
    campoLargo = City('Campo Largo', 27)
    curitiba = City('Curitiba', 0)
    balsaNova = City('Balsa Nova', 41)
    araucaria = City('Auracaria', 23)
    saoJose = City('São Jośe', 13)
    contenda = City('Contenda', 39)
    mafra = City('Mafra', 94)
    tijucas = City('Tijucas do Sul',56)
    lapa = City('Lapa', 74)
    saoMateus = City('São Mateus do Sul', 123)
    tresBarras = City('Três Barras', 131)

    portoUniao.addCityAdjacent(AdjacentDistance(pauloFrontin, 46))
    portoUniao.addCityAdjacent(AdjacentDistance(canoinhas, 78))
    portoUniao.addCityAdjacent(AdjacentDistance(saoMateus,87))

    pauloFrontin.addCityAdjacent(AdjacentDistance(portoUniao, 46))
    pauloFrontin.addCityAdjacent(AdjacentDistance(irati, 75))

    canoinhas.addCityAdjacent(AdjacentDistance(portoUniao, 78))
    canoinhas.addCityAdjacent(AdjacentDistance(tresBarras,12))
    canoinhas.addCityAdjacent(AdjacentDistance(mafra,66))

    irati.addCityAdjacent(AdjacentDistance(pauloFrontin, 75))
    irati.addCityAdjacent(AdjacentDistance(palmeira, 75))
    irati.addCityAdjacent(AdjacentDistance(saoMateus, 57))

    palmeira.addCityAdjacent(AdjacentDistance(irati, 75))
    palmeira.addCityAdjacent(AdjacentDistance(saoMateus, 77))
    palmeira.addCityAdjacent(AdjacentDistance(campoLargo, 55))

    campoLargo.addCityAdjacent(AdjacentDistance(palmeira, 55))
    campoLargo.addCityAdjacent(AdjacentDistance(balsaNova, 22))
    campoLargo.addCityAdjacent(AdjacentDistance(curitiba, 29))

    curitiba.addCityAdjacent(AdjacentDistance(campoLargo, 29))
    curitiba.addCityAdjacent(AdjacentDistance(balsaNova, 51))
    curitiba.addCityAdjacent(AdjacentDistance(araucaria, 37))
    curitiba.addCityAdjacent(AdjacentDistance(saoJose, 15))

    balsaNova.addCityAdjacent(AdjacentDistance(curitiba, 51))
    balsaNova.addCityAdjacent(AdjacentDistance(campoLargo, 22))
    balsaNova.addCityAdjacent(AdjacentDistance(contenda, 19))

    araucaria.addCityAdjacent(AdjacentDistance(curitiba, 37))
    araucaria.addCityAdjacent(AdjacentDistance(contenda, 18))

    saoJose.addCityAdjacent(AdjacentDistance(curitiba, 15))
    saoJose.addCityAdjacent(AdjacentDistance(tijucas, 49))

    contenda.addCityAdjacent(AdjacentDistance(balsaNova, 19))
    contenda.addCityAdjacent(AdjacentDistance(araucaria, 18))
    contenda.addCityAdjacent(AdjacentDistance(lapa, 26))

    mafra.addCityAdjacent(AdjacentDistance(tijucas, 99))
    mafra.addCityAdjacent(AdjacentDistance(lapa, 57))
    mafra.addCityAdjacent(AdjacentDistance(canoinhas, 66))

    tijucas.addCityAdjacent(AdjacentDistance(mafra, 99))
    tijucas.addCityAdjacent(AdjacentDistance(saoJose, 49))

    lapa.addCityAdjacent(AdjacentDistance(contenda, 26))
    lapa.addCityAdjacent(AdjacentDistance(saoMateus, 60))
    lapa.addCityAdjacent(AdjacentDistance(mafra, 57))

    saoMateus.addCityAdjacent(AdjacentDistance(palmeira, 77))
    saoMateus.addCityAdjacent(AdjacentDistance(irati, 57))
    saoMateus.addCityAdjacent(AdjacentDistance(lapa, 60))
    saoMateus.addCityAdjacent(AdjacentDistance(tresBarras, 43))
    saoMateus.addCityAdjacent(AdjacentDistance(portoUniao, 87))

    tresBarras.addCityAdjacent(AdjacentDistance(saoMateus, 43))
    tresBarras.addCityAdjacent(AdjacentDistance(canoinhas, 12))