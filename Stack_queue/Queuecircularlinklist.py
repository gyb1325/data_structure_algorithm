# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 20:07:23 2018

@author: guyo
"""

class EmptyQueueError(Exception):
    pass
class Node(object):
    def __init__(self,data):
        self.link = None
        self.info = data
        
class Queue:
    def __init__(self):
        self.rear = None
    def is_empty(self):
        return self.rear == None
    def size(self):
        if self.rear == None:
            return 0
        n = 1
        p = self.rear.link
        while p != self.rear:
            n += 1
            p = p.link
        return n
    def enqueue(self,data):
        temp = Node(data)
        if self.rear == None:
            self.rear = temp
            self.rear.link = temp
        else:
            temp.link = self.rear.link
            self.rear.link = temp
            self.rear = temp
            
    def dequeue(self):
        if self.rear == None:
            raise EmptyQueueError("Queue is empty")
        if self.rear.link == self.rear:
            temp = self.rear
            self.rear = None
        else:
            temp = self.rear.link
            self.rear.link = temp.link
        return temp.info
    def peek(self):
        if self.front == None:
            raise EmptyQueueError("Queue is empty")
        data = self.rear.link.info
        return data
    def display(self):
        if self.rear== None:
            print("Queue is empty")
            return
        p = self.rear.link
        while True:
            print(p.info, " ")
            p = p.link
            if p == self.rear.link:
                break
        print()
            

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


        