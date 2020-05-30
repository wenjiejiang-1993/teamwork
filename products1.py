#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 20:07:32 2020

@author: jiangwenjie
"""

def relevant(products, preferences):
    checklist=products.copy()

    for i in range(0,len(products)):
        p1 = products[i]
        plist2 = products.copy()
        plist2.remove(p1)
        poutput=[]
        for p2 in plist2:
            output=[]
            
            for rule in preferences:
                if rule[1] == 1:
                    op = p1[rule[0]] < p2[rule[0]]
                elif rule[1] == -1:
                    op = p1[rule[0]] > p2[rule[0]]
                else:
                    print ("Your preferences list is wrong.") 
                output.append(op)

            if False in output:
                poutput.append(False)
            else:
                poutput.append(True)
                
        if True in poutput:
            checklist.remove(p1)        
    return checklist