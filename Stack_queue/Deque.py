# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 20:23:37 2018

@author: guyo
"""

class EmptyQueueError(Exception):
    pass
class Deque:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def size(self):
        return len(self.items)
    def insert_front (self,data):
        self.items.insert(0,data)
    def insert_rear (self,data):
        self.items.append(data)
    def delete_front(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is empty")
        return self.items.pop(0)
    def delete_rear(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is empty")
        return self.items.pop()
    def first(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is empty")
        return self.items[0]
    def last(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is empty")       
        return self.items[-1]
    def display(self):
        print(self.items)


if __name__ == "__main__":
    q = Deque()
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
    