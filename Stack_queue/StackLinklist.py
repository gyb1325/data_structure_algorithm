#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 14:13:28 2018

@author: yongbingu
"""

class EmptyStackError(Exception):
    pass
class Node(object):
    def __init__(self,data):
        self.link = None
        self.info = data
        
class Stack:
    def __init__(self):
        self.top = None
    def is_empty(self):
        return self.top == None
    def size(self):
        if self.is_empty():
            return 0
        count = 0 
        p = self.top
        while p is not None:
            count += 1
            p = p.link
        return count
    def push(self,data):
        temp = Node(data)
        temp.link = self.top
        self.top = temp
    def pop(self):
        if self.is_empty():
            raise EmptyStackError("Stack is empty")
        data = self.top.info
        self.top = self.top.link
        return data
    def peek(self):
        if self.is_empty():
            raise EmptyStackError("Stack is empty")
        data = self.top.info
        return data
    def display(self):
        if self.is_empty():
            print("Stack is empty")
            return
        p = self.top
        while p is not None:
            print(p.info, " ")
            p = p.link
            

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


        