#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 18:18:17 2018

@author: raphael.ribeiro

DepthFirstSearch
- Without information
- Data Structure - Stack(LIFO)
"""

class DepthFirst(object):
    def __init__(self, start, goal):
        self.start = start
        self.start.visited = True
        self.goal = goal
        self.frontier = []
        self.frontier.append(start)
        self.success = False
        self.iterations = 0
        
    def search(self): #No Information / Blind or random search
        topo = self.frontier[-1]
        print('\nTop: {}'.format(topo.name))

        if topo == self.goal:
            self.success = True
            print('Iterations: {}'.format(self.iterations))
        else:
            self.iterations += 1
            for adj in topo.adjacents:
                if self.success == False:
                    if adj.visited == False:
                        adj.visited = True
                        self.frontier.append(adj)#add all adj(stack)
                        print("Adjacent: {}".format(adj.name))
                        DepthFirst.search(self)#recursion
        print('Unstack: {}'.format(self.frontier.pop().name))
