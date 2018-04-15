# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 23:04:19 2018

@author: guyo
"""

class Node(object):
    def __init__(self,value):
        self.info = value
        self.link = None
        
class HeaderLinkedList(object):
    def __init__(self):
        self.head = Node(0)
        
    def display_list(self):
        if self.head.link == None:
            print("This list is empty")
            return
        p = self.head.link
        print("List is : ")
        while p is not None:
            print(p.info , " ", end = ' '  )
            p = p.link
        print()
    def create_list(self):
        n = int(input("Enter the node you want to create "))
        for i in range(n):
            data = int(input("Please enter the data "))
            self.insert_at_end(data)
    def insert_at_end(self, data):
        temp = Node(data)
        p = self.head
        while p.link is not None:
            p = p.link
        p.link = temp
    def insert_before(self, data, x):
        p = self.head
        while p.link is not None:
            if p.link.info == x:
                break
            p = p.link
        if p.link == None:
            print("x is not present")
        else:
            temp = Node(data)
            temp.link = p.link
            p.link = temp
            
    def insert_at_position(self,data,k):
        p = self.head
        i = 1 
        while i <= k-1 and p is not None:
            p = p.link
            i = i+1
        if p is None: 
            print("Overflow")
        else:
            temp = Node(data)
            temp.link = p.link
            p.link =temp
    def delete_node(self,x):
        p = self.head
        while p.link is not None:
            if p.link.info == x:
                break
            p = p.link
        if p.link is None:
            print (x, " Not Found")
        else:
            p.link = p.link.link
    
        
        
        
        
        
        
        