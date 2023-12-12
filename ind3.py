#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == "__main__":
    a = { 'c', 'm', 'n', 'o', 'g' }
    b = { 'c', 'g', 'p', 'q' }
    c = { 'f', 'g', 's', 'x', 'y', 'z' }
    d = { 'a', 'c', 'd', 'g', 'u', 'v', 'z' }
    all_ = a.union(b).union(c).union(d)
    
    x = (a.union(b)).intersection(c)
    y = (all_.difference(a).intersection(d)).union(c.difference(d))
    
    print(f"x = {x}")
    print(f"y = {y}")