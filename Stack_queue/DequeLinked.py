# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 21:08:29 2018

@author: guyo
"""
class Node(object):
    def __init__(self,data):
        self.info = data
        self.prev = None
        self.next = None

class EmptyQueueError(Exception):
    pass

class Deque:
    def __init__(self):
        self.front = None
        self.rear = None
    def is_empty(self):
        return self.front == None
    def size(self):
        if self.is_empty():
            return 0
        p = self.front
        count = 0
        while p is not None:
            count +=1
            p = p.next
        return count
    
    def insert_front (self,data):
        temp = Node(data)
        if self.is_empty():
            self.front = temp
            self.rear = temp
        else:
            temp.next = self.front
            self.front.prev = temp
            self.front =temp
            
    def insert_rear (self,data):
        temp = Node(data) 
        if self.is_empty():
            self.front = temp
            self.rear = temp
        else:
            self.rear.next = temp
            temp.prev = self.rear
            self.rear = temp
    def delete_front(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is empty") 
        x = self.front.info
        if self.front.next == None:
            self.front = None
            self.rear = None
        else:
           self.front = self.front.next
           self.front.prev = None
        return x
    def delete_rear(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is empty") 
        x = self.rear.info
        if self.front.next == None:
            self.front = None
            self.rear = None
        else:
            self.rear = self.rear.prev
            self.rear.next = None
        return x
    def first(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is empty") 
        return self.front.info 
    def last(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is empty") 
        return self.rear.info 
    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        p = self.front
        while p is not None:
            print(p.info)
            p = p.next

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