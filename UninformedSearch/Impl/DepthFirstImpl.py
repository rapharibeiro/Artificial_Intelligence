#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 22:15:12 2018

@author: raphael.ribeiro
"""
import sys
sys.path.append("../Maps")
sys.path.append("../Search")
from Map import Map
from DepthFirst import DepthFirst

map = Map()
dfs = DepthFirst(map.portoUniao, map.curitiba)
dfs.search()
