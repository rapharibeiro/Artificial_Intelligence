#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 22:20:05 2018

@author: raphael.ribeiro
"""
import sys
sys.path.append("../Maps")
sys.path.append("../Search")
from BreadthFirst import BreadthFirst
from Map import Map

map = Map()
bfs = BreadthFirst(map.portoUniao, map.curitiba)
bfs.search()