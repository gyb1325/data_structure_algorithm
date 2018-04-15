# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 23:26:48 2018

@author: guyo
"""

class Node(object):
    def __init__(self,value):
        self.info = value
        self.link = None
class SortedLinkedList(object):
    def __init__(self):
        self.start = None
    def insert_in_order(self, data):
        temp = Node(data)
        if self.start == None or data < self.start.info:
            temp.link= self.start
            self.start = temp
            return
        p = self.start
        while p.link is not None and p.link.info < data:
            p = p.link
        temp.link = p.link
        p.link = temp
        
    def create_list(self):
        n = int(input("Enter the node you want to create "))
        if n == 0:
            return
        for i in range(n):
            data = int(input("Please enter the data "))
            self.insert_in_order(data)            
    def search(self,x):
        if self.start == None:
            print("List is empty")
            return
        p = self.start
        position = 1
        while p is not None and p.info <= x:
            if p.info == x:
                break
            position += 1
            p = p.link
        if p is None or p.info != x:
            print(x, " is not in the List")    
        else: 
            print(x, " is at position ", position)
    def display_list(self):
        if self.start is None:
            print("List is empty")
        else:
            print("List is : ")
            p = self.start
            while p is not None:
                print(p.info , " ", end = ' '  )
                p = p.link
            print()

list = SortedLinkedList()
list.create_list()


while True:
    option = int(input("Enter your choice :"))
    if option == 1:
        list.display_list()
    elif option == 2:
        list.create_list
    elif option == 3:
        data = int(input("Enter the element to be searched : "))
        list.search(data)