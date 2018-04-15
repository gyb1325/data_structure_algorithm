#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 14:24:57 2018

@author: yongbingu
"""

class EmptyQueueError(Exception):
    pass
class Queue:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def size(self):
        return len(self.items)
    def enqueue(self,data):
        self.items.append(data)
    def dequeue(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is empty")
        return self.items.pop(0)
    def peek(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is empty")
        return self.items[0]
    def display(self):
        print(self.items)

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