#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 13:55:59 2018

@author: yongbingu
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 13:32:05 2018

@author: yongbingu
"""

class EmptyStackError(Exception):
    pass
class FullStackError(Exception):
    pass
class Stack:
    def __init__(self,max_size =10):
        self.items = [None]*max_size
        self.count =0
    def is_empty(self):
        return self.count == 0
    def is_full(self):
        return self.count == len(self.items)
    def size(self):
        return self.count
    def push(self, item):
        if self.is_full():
            raise FullStackError()
        self.items[self.count] = item
        self.count += 1
    def pop(self):
        if self.is_empty():
            raise EmptyStackError("Stack is empty")
        x = self.items[self.count -1]
        self.items[self.count -1] = None
        self.count -= 1
        return x
    def peek(self):
        if self.is_empty():
            raise EmptyStackError("Stack is empty")
        return self.items[self.count -1]
    def display(self):
        print(self.items)
if __name__ == "__main__":
    st = Stack(8)
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
        
        