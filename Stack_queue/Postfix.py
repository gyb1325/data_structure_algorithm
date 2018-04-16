# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 23:03:38 2018

@author: guyo
"""

from StackArray import Stack

def infix_to_postfix(infix):
    postfix = ""
    st = Stack()
    for symbol in infix:
        if symbol == ' ' or symbol == '\t':
            continue
        if symbol =='(':
            st.push(symbol)
        elif symbol ==')':
            next = st.pop()
            while next!='(':
                postfix = postfix+next
                next = st.pop()
        elif symbol in "+-*/%^":
            while not st.is_empty() and precedence(st.peak())>=precedence(symbol):
                next = st.pop()
                postfix = postfix + next
            st.push(symbol)
        else:
            postfix = postfix + symbol
    while not st.is_empty():
        postfix = postfix + st.pop()
    return postfix
def precedence(symbol):
    if symbol == '(':
        return 0
    elif symbol in '+-':
        return 1
    elif symbol in '*/%':
        return 2
    elif symbol in '^':
        return 3
    
    
    
    
while True:
    print("Enter the infix expression (q to quit) : ", end = '' )
    expression = input()
    if expression == 'q':
        break
    postfix = infix_to_postfix(expression)
    print("Postfix expression is ", postfix)
            