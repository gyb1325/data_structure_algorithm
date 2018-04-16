# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 22:08:25 2018

@author: guyo
"""

from StackArray import Stack

def is_valid(expr):
    st = Stack()
    for ch in expr:
        if ch in '( [ {':
            st.push(ch)
        if ch in ') ] }':
            if st.is_empty():
                print("Right Parentheses are more than left Parentheses")
                return False
            else:
                temp = st.pop()
                if not_match(temp, ch):
                    print ("MisMatched left ", temp, " right ",ch )
                    return False
    if st.is_empty():
        print("Balanced Parentheses")
        return True
    else:
        print("Left Parentheses are more than right Parentheses")
        return False 
def not_match(left, right):
    if left =='{' and right == '}':
        return False
    if left =='[' and right == ']':
        return False
    if left =='(' and right == ')':
        return False       
    return True
    

while True:
    print ("Enter and expression with parentheses (q to quit): ", end = ' ')            
    expression = input()
    if expression == 'q':
        break
    if is_valid(expression):
        print("Valid Expression")
    else:
        print("Invalid Expression")        
        