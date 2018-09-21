#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 19:20:41 2018

@author: raphael.ribeiro

Class of the type of data that we will perform the search.
"""

class City(object):
    def __init__(self,name):
        self.name = name #nome of the city
        self.visited = False #boolean to determine if node has already been visited
        self.adjacents = [] #adjacents list

    #add adjacent in the list
    def addCityAdjacent(self, city):
        self.adjacents.append(city)