# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 20:36:43 2018

@author: guyo
"""

class EmptyQueueError(Exception):
    pass
class Deque:
    def __init__(self, default_size):
        self.items = [None]* default_size
        self.front = 0
        self.count = 0
    def is_empty(self):
        return self.count == 0
    def size(self):
        return self.count
    def insert_front (self,data):
        if self.count == len(self.items):
            self.resize(2*len(self.items))
        self.front = (self.front-1) % len(self.items)
        self.items[self.front] = data
        self.count += 1
    def insert_rear (self,data):
        if self.count == len(self.items):
            self.resize(2*len(self.items))
        i = (self.front + self.count) % len(self.items)
        self.items[i] = data
        self.count += 1
    def delete_front(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is empty")
        data = self.items[self.front]
        self.items[self.front] = None
        self.front = (self.front + 1) % len(self.items)
        self.count -= 1
        return data
    def delete_rear(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is empty")
        rear = (self.front + self.count - 1) % len(self.items)
        data = self.items[rear]
        self.items[rear] = None  
        self.count -= 1
        return data
    def first(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is empty")
        return self.items[self.front]
    def last(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is empty")  
        rear = (self.front + self.count - 1) % len(self.items)            
        return self.items[rear]
    def display(self):
        print(self.items)
    def resize(self,newsize):
        oldlist = self.items
        self.items = [None]*newsize
        i= self.front
        for j in range(len(oldlist)):
            self.items[j] = oldlist[i]
            i = (i+1)% len(oldlist)
        self.front = 0


if __name__ == "__main__":
    q = Deque(3)
    while True:
        choice = int(input("Enter your choice "))
        if choice == 1:
            x = int(input("Enter the element to be pushed "))
            q.insert_front(x)
        elif choice == 2:
            x = int(input("Enter the element to be pushed "))
            q.insert_rear(x)            
        elif choice == 3:                        
            x= q.delete_front()
            print("The popped element is ", x)
        elif choice == 4:
            x= q.delete_rear()
            print("The popped element is ", x)
        elif choice == 5:
            print("element in the top is ", q.first())
        elif choice == 6:
            print("element in the rear is ", q.last())
        elif choice == 7:
            print("Size of the stack is ",q.size())
        elif choice == 8:
            q.display()
        elif choice == 9:
            break