#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 16:55:31 2018

@author: raphael.ribeiro
"""

import sys
sys.path.append("../Maps")
sys.path.append("../Search")
from Greedy import Greedy
from Map import Map

map = Map()
greedy = Greedy(map.curitiba)
greedy.search(map.portoUniao)