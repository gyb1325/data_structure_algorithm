#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 14:36:45 2018

@author: yongbingu
"""

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
        self.front = 0
    def is_empty(self):
        #return self.items == []
        return self.front == len(self.items)
    def size(self):
        return len(self.items)-self.front
    def enqueue(self,data):
        self.items.append(data)
    def dequeue(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is empty")
        x = self.items[self.front]
        self.items[self.front] = None
        self.front += 1
        return x
    def peek(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is empty")
        return self.items[self.front]
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