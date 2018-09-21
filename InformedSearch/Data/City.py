#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 16:22:11 2018

@author: raphael.ribeiro

Class of the type of data that we will perform the search.
"""

class City(object):
    def __init__(self, name, distanceTarget):
        self.name = name  # name of the city
        self.visited = False  # boolean to determine if node has already been visited
        self.adjacents = []  # adjacent list
        self.distanceTarget = distanceTarget # value of distance to objective in straight line

    # add int adjacent list
    def addCityAdjacent(self, city):
        self.adjacents.append(city)