#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 14:53:17 2018

@author: yongbingu
"""

class EmptyQueueError(Exception):
    pass
class Queue:
    def __init__(self,default_size = 10):
        self.items = [None]*default_size
        self.front = 0
        self.count = 0
    def is_empty(self):
        #return self.items == []
        return self.count == 0
    def size(self):
        return self.count
    def enqueue(self,data):
        if self.count == len(self.items):
            self.resize(2*len(self.items))
        i = (self.count+self.front)%len(self.items)
        self.items[i] = data
        self.count+=1
    def dequeue(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is empty")
        x = self.items[self.front]
        self.items[self.front] = None
        self.front = (self.front+1) % len(self.items)
        self.count -=1
        return x
    def peek(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is empty")
        return self.items[self.front]
    def display(self):
        print(self.items)
    def resize(self, newsize):
        old_list = self.items
        self.items = [None]*newsize
        i = self.front
        for j in range(self.count):
            self.items[j] = old_list[i]
            i = (i+1)% len(old_list)
        self.front = 0

if __name__ == "__main__":
    q = Queue()
    while True:
        choice = int(input("Enter your choice "))
        if choice == 1:
            x = int(input("Enter the element to be pushed "))
            q.enqueue(x)
        elif choice == 2:
            x= q.dequeue()
            print("The popped element is ", x)
        elif choice == 3:
            print("element in the top is ", q.peek())
        elif choice == 4:
            print("Size of the stack is ",q.size())
        elif choice == 5:
            q.display()
        elif choice == 6:
            break