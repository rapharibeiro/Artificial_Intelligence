#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 22:59:17 2018

@author: raphael.ribeiro

BreadthFirstSearch
- Without information
- Data Structure - Queue(FIFO)
"""
from collections import deque

class BreadthFirst(object):
    def __init__(self, start, goal):
        self.start = start
        self.start.visited = True
        self.goal = goal
        self.frontier = deque()
        self.frontier.append(start)
        self.success = False
        self.iterations = 0

    def search(self):#No Information / Blind or random search
        top = self.frontier[0]
        print("\nTop: {}".format(top.name))
        if top == self.goal: # find the goal
            self.success = True
            print("Iterations: {}".format(self.iterations))
        else:
            self.iterations += 1
            temp = self.frontier.popleft()#dequeue
            print("Dequeue: {}".format(temp.name))
            for adj in top.adjacents:
                if adj.visited == False:
                    adj.visited = True
                    self.frontier.append(adj)#add all adjs(queue)
                    print("Adjacent: {}".format(adj.name))
            BreadthFirst.search(self)#recursion