#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 13:32:05 2018

@author: yongbingu
"""

class EmptyStackError(Exception):
    pass
class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def size(self):
        return len(self.items)
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if self.is_empty():
            raise EmptyStackError("Stack is empty")
        return self.items.pop()
    def peek(self):
        if self.is_empty():
            raise EmptyStackError("Stack is empty")
        return self.items[-1]
    def display(self):
        print(self.items)
if __name__ == "__main__":
    st = Stack()
    while True:
        choice = int(input("Enter your choice "))
        if choice == 1:
            x = int(input("Enter the element to be pushed "))
            st.push(x)
        elif choice == 2:
            x= st.pop()
            print("The popped element is ", x)
        elif choice == 3:
            print("element in the top is ", st.peek())
        elif choice == 4:
            print("Size of the stack is ",st.size())
        elif choice == 5:
            st.display()
        elif choice == 6:
            break
        
        