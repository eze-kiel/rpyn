# !/usr/bin/env python3

import operator, sys

def get_number(num):
    return float(num)

def do_clear(stack):
    return []

def do_drop(stack):
    stack.pop(0)
    return stack

def do_exit(stack):
    exit()

def do_sum(stack):
    return [sum(stack)]

def do_tva(stack):
    stack.insert(0, stack[0]*0.20)
    return stack

def do_plus(stack):
     stack.insert(0, stack.pop(0) + stack.pop(0))
     return stack

def do_minus(stack):
     stack.insert(0, stack.pop(0) - stack.pop(0))
     return stack

def do_multi(stack):
    stack.insert(0, stack.pop(0) * stack.pop(0))
    return stack

def do_power(stack):
    stack.insert(0, stack.pop(0) ** stack.pop(0))
    return stack

def do_modulo(stack):
    stack.insert(0, stack.pop(0) % stack.pop(0))
    return stack

def do_divi(stack):
    if stack[1] == 0:
        print("impossible")
    else:
        stack.insert(0, stack.pop(0) / stack.pop(0))
    return stack

def do_swap(stack):
    stack.insert(0, stack.pop(1))
    return stack

def do_help(stack):
    for k,v in FUNCTIONS.iteritems():
        print(" {}   : {}".format(k,v["description"]))
    return stack


FUNCTIONS = {
    '+': {"card": 2, "func": do_plus, "description": "add the last two numbers of the list"},
    '-': {"card": 2, "func": do_minus, "description": "substract the last two numbers of the list"},
    '*': {"card": 2, "func": do_multi, "description": "multiply the last two numbers of the list"},
    '/': {"card": 2, "func": do_divi, "description": "divise the last two numbers of the list"},
    '**': {"card": 2, "func": do_power, "description": "power tool"},
    '%': {"card": 2, "func": do_modulo, "description": "modulo tool"},
    'clear': {"card": 0, "func": do_clear, "description": "clear the list"},
    'sum': {"card": 2, "func": do_sum, "description": "add all the numbers of the list"},
    'exit': {"card": 0, "func": do_exit, "description": "exit the calculator"},
    'swap': {"card": 2, "func": do_swap, "description": "swap the last two numbers of the list"},
    'drop': {"card": 1, "func": do_drop, "description": "drop the last number of the list"},
    'help': {"card": 0, "func": do_help, "description": "print the 'help' informations"},
    'tva': {"card": 1, "func": do_tva, "description": "calculate the tva of the last number of the list"}
}

def rpn_loop():
    l = []

    while True:
        a = raw_input()
        try:
            l.insert(0, get_number(a))
        except:
            if len(l) >= FUNCTIONS[a]["card"]:
                l = FUNCTIONS[a]["func"](l)
            else:
                print("not enough elements")

        print(l)

if __name__ == '__main__':
    print("**/RPyN\**")
    print("")
    rpn_loop()