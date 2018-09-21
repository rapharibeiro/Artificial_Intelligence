# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 16:44:43 2018

@author: raphael.ribeiro
AStar Search
- With Information
- Heuristic: value of the distance in a straight line by the actual distance of each city
"""

class AStar(object):
    def __init__(self, goal):
        self.goal = goal
        self.find = False
        self.iterations = 0
        self.finalDistance = 0

    def search(self, current):
        print('\nActual: {}'.format(current.name))
        current.visited = True

        if current == self.goal:
            self.find = True
            print("Iterations: {}".format(self.iterations))
            print("Value Distance: {}".format(self.finalDistance))
        else:
            self.iterations += 1
            self.frontier = [] #heuristic list
            for adj in current.adjacents:
                if adj.city.visited == False:
                    adj.city.visited = True
                    self.frontier.append(adj) #add all adjs(queue)
                    self.frontier.sort(key=lambda x: x.distanceHeuristic)  # heuristic: value of the distance in a straight line by the actual distance of each city
            self.__show(self.frontier)
            if self.frontier[0].city != None:
                self.finalDistance += self.frontier[0].distanceReal
                AStar.search(self, self.frontier[0].city)#recursion: shorter distance

    def __show(self, data):
        for d in data:
            print("{} - {}".format(d.city.name, d.distanceHeuristic))