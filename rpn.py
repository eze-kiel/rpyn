# !/usr/bin/env python3

import operator

def get_number(num):
    return float(num)

def get_operator(op):
	return { '+': operator.add,'-': operator.sub, '/': operator.truediv, '*': operator.mul, '%': operator.mod, '**': operator.pow }[op]

l = []


while True:
    a = input()
    try:
        l.append(get_number(a))
        print(l)
    except:
        ope = get_operator(a)
        z = ope(l.pop(0),l.pop(0))
        l.insert(0, z)
        print(l)
