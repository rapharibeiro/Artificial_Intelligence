#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 16:52:01 2018

@author: raphael.ribeiro
Greedy Search
- With Information
- Heuristic: value of the distance in a straight line
"""

class Greedy(object):
    def __init__(self, goal):
        self.goal = goal
        self.find = False
        self.iterations = 0
        self.finalDistance = 0

    def search(self, current):
        print("\ncurrent: {}".format(current.name))
        current.visited = True
        if current == self.goal:
            self.find = True
            print("Iterations: {}".format(self.iterations))
            print("Value Distance: {}".format(self.finalDistance))
        else:
            self.iterations += 1
            self.frontier = [] #heuristic
            for adj in current.adjacents:
                if adj.city.visited == False:
                    print("Adj: {}".format(adj.city.name))
                    adj.city.visited = True
                    self.frontier.append(adj) #add adj
                    self.frontier.sort(key=lambda x: x.city.distanceTarget)# value of the distance in a straight line
            self.__show(self.frontier)
            if self.frontier[0].city != None:
                self.finalDistance += self.frontier[0].distanceReal
                Greedy.search(self, self.frontier[0].city)#recursion: shorter distance

    def __show(self, data):
        for d in data:
            print("{} - {}".format(d.city.name, d.city.distanceTarget))