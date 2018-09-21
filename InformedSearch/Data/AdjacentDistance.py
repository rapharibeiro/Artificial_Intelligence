#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 16:26:02 2018

@author: raphael.ribeiro

Class used to connect one city to another using the value of the distance in a straight line by the actual distance of each city
"""
#classe para ligar uma cidade a outra
class AdjacentDistance(object):
    def __init__(self, city, distanceReal):
        self.city = city
        self.distanceReal = distanceReal
        self.distanceHeuristic = self.city.distanceTarget + self.distanceReal
