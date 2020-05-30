#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 23:43:53 2020

@author: jiangwenjie
"""

def inferred_conditions(pos_examples, neg_examples):
    rule=[]
    for i in range(2,len(pos_examples[0])):
        a=[]
        b=[]
        print("i: " +str(i))
        for j in pos_examples:
            a.append(j[i])
        pos_cond=[i,max(a),min(a)]
        for j in neg_examples:
            b.append(j[i])
        neg_cond=[i,max(b),min(b)]
        print("pos_cond: "+ str(pos_cond))
        print("neg_cond: "+ str(neg_cond))
        if neg_cond[1]>=pos_cond[1]:
            rule.append([i,'<=',pos_cond[1]])
        if neg_cond[2]<=pos_cond[2]:
            rule.append([i,'>=',pos_cond[2]])
    return rule