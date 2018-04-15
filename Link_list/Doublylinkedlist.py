# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 14:05:42 2018

@author: guyo
"""

class Node:
    def __init__(self,value):
        self.info = value
        self.prev = None
        self.next = None

class DoubleLinkList:
    def __init__(self):
        self.start = None
    def display_list(self):
        if self.start is None:
            print("List is empty")
            return
        p = self.start
        print("List is ")
        while p is not None:
            print(p.info, "  ", end=' ')
            p = p.next
        print()
    def insert_in_beginning(self,data):
        temp = Node(data)
        temp.next = self.start
        self.start.prev = temp
        self.start =temp
    def insert_in_empty_list(self,data):
        temp = Node(data)
        self.start = temp
    def insert_at_end(self,data):
        temp = Node(data)
        p = self.start
        while p.next is not None:
            p = p.next
        p.next = temp
        temp.prev = p
    def create_list(self):
        n = int(input("Enter the numbers of Node to be created"))
        if n == 0:
            return 
        data = int(input("Enter the first element to be inserted"))
        self.insert_in_empty_list(data)
        for i in range(n-1):
            data = int(input("Enter the elements to be inserted"))
            self.insert_at_end(data)

    def insert_after(self,data,x):
        temp = Node(data)
        p = self.start
        while p is not None:
            if p.info == x :
                break
            p = p.next 
        if p is None:
            print ("The element is not in the list")
            return
        else:            
            temp.next = p.next
            temp.prev = p
            if p.next is not None:
                p.next.prev = temp # when p is not in the last node
            p.next = temp
    def insert_before(self,data,x):
        if self.start is None:
            print ("the list is empty")
            return
        if self.start.info == x:
            self.insert_in_beginning(data)
        p = self.start
        while p is not None:
            if p.info == x :
                break
            p = p.next 
        if p is None:
            print ("The element is not in the list")
            return
        else:
            temp = Node(data)
            temp.next = p
            temp.prev = p.prev
            p.prev.next = temp
            p.prev = temp
    def delete_first_node(self):
        if self.start is None:
            return
        if self.start.next is None:
            self.start = None
            return
        self.start = self.start.next
        self.start.prev = None
    def delete_last_node(self):
        if self.start is None:
            return
        if self.start.next is None:
            self.start = None
            return
        p = self.start 
        while p.next is not None:
            p = p.next
        p.prev.next = None
    def delete_node(self,x):
        if self.start is None:
            return
        if self.start.next is None:
            if self.start.info == x:
                self.start = None
                return
            else :
                print(x, " is not found")
        #delete of first node   
        if self.start.info == x :
            self.start = self.start.next
            self.start.prev = None
            return
        p = self.start.next
        while p.next is not None :
            if p.info == x:
                break
            p = p.next
        if p.next is not None:
            p.prev.next = p.next
            p.next.prev = p.prev
        else:
            if p.info == x:
                p.prev.next = None
            else:
                print(x, "not found")

    def reverse_list(self):
        if self.start is None:
            return
        p1 = self.start
        p2 = self.start.next 
        p1.next = None
        p1.prev = p2
        while p2 is not None:
            p2.prev = p2.next
            p2.next = p1
            p1 = p2 
            p2 = p2.prev
        self.start = p1
        
    
    
list = DoubleLinkList()
list.create_list()
while True:
    option = int(input("Enter your choice :"))
    if option == 1:
        list.display_list()
    elif option == 2:
        data = int(input("Enter the element to be inserted : "))
        list.insert_in_beginning(data)
    elif option == 3:
        data = int(input("Enter the element to be inserted : "))
        list.insert_at_end(data)
    elif option == 4:
        data = int(input("enter the element to be inserted : "))
        x = int(input("enter the position at wich to insert"))
        list.insert_after(data,x)
    elif option == 5:
        data = int(input("enter the element to be inserted : "))
        x = int(input("enter the position at wich to insert"))
        list.insert_before(data,x)
    elif option == 6:
        list.delete_first_node()
    elif option == 7:
        list.delete_last_node()
    elif option == 8:
        x = int(input("enter the element to be deleted "))
        list.delete_node(x)
    elif option == 9:
        list.reverse_list()


