#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 06:42:30 2018
@author: pc
"""

import os
from pyecharts.charts import Bar
import os.path
import xml.dom.minidom
import xml.etree.cElementTree as et
from scipy.ndimage import measurements




res = [23754, 69366, 41535, 25162, 14533, 6391, 3366, 2128, 1598, 1394, 1198, 803, 506, 313, 186, 87, 50, 31, 11, 12]
data = []
for i in range(0, 20, 2):
    t = res[i] + res[i + 1]
    data.append(t)
print(data)

total = 0
ii = 2
for i in data:
    total += i
print(total)





