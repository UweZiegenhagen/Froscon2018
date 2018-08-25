# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 07:47:30 2018

@author: Uwe Ziegenhagen
"""

def fakulty(n):
    if n == 0:
        return 1
    else:
        return n * fakulty(n-1)

