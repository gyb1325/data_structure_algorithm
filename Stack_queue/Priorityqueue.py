# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 21:33:44 2018

@author: guyo
"""

class Node(object):
    def __init__(self,data,pr):
        self.info = data
        self.priority = pr
        self.link = None 

class EmptyQueueError(Exception):
    pass

class PriorityQueue(object):
    def __init__(self):
        self.front = None
    def enqueue(self, data, data_prio):
        temp = Node(data, data_prio)
        if self.is_empty() or data_prio < self.front.priority:
            temp.link = self.front
            self.front = temp
        else:
            p = self.front
            while p.link != None and p.link.priority <= data_prio:
                p = p.link
            temp.link = p.link
            p.link = temp
    def dequeue(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is empty")
        x = self.front.info
        self.front = self.front.link
        return x
    def is_empty(self):
        return self.front == None
    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        p = self.front
        while p is not None:
            print(p.info)
            p = p.link
    def size(self):
        n = 0
        p= self.front
        while p is not None:
            p = p.link
            n += 1
        return n
    
    
    
if __name__ == "__main__":
    q = PriorityQueue()
    while True:
        choice = int(input("Enter your choice "))
        if choice == 1:
            x = int(input("Enter the element to be pushed "))
            pr = int(input("Enter the priority to be pushed "))
            q.enqueue(x,pr)
        elif choice == 2:
            x= q.dequeue()
            print("The popped element is ", x)
#        elif choice == 3:
#            print("element in the top is ", q.peek())
        elif choice == 4:
            print("Size of the stack is ",q.size())
        elif choice == 5:
            q.display()
        elif choice == 6:
            break
            