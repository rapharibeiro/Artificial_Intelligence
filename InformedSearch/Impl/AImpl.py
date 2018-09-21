#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 16:59:51 2018

@author: raphael.ribeiro
"""

import sys
sys.path.append("../Maps")
sys.path.append("../Search")
from AStar import AStar
from Map import Map

map = Map()
astar = AStar(map.curitiba)
astar.search(map.portoUniao)