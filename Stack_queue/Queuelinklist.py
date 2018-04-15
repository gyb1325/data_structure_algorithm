#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 15:15:39 2018

@author: yongbingu
"""

class EmptyQueueError(Exception):
    pass
class Node(object):
    def __init__(self,data):
        self.link = None
        self.info = data
        
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size_queue = 0
    def is_empty(self):
        return self.front == None
    def size(self):
        return self.size_queue
    def enqueue(self,data):
        temp = Node(data)
        if self.front == None:
            self.front = temp
        else:
            self.rear.link = temp
        self.rear = temp
        self.size_queue += 1
    def dequeue(self):
        if self.front == None:
            raise EmptyQueueError("Queue is empty")
        x = self.front.info
        self.front = self.front.link
        self.size_queue -= 1
        return x
    def peek(self):
        if self.front == None:
            raise EmptyQueueError("Queue is empty")
        data = self.front.info
        return data
    def display(self):
        if self.front== None:
            print("Queue is empty")
            return
        p = self.front
        while p is not None:
            print(p.info, " ")
            p = p.link
            

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


        