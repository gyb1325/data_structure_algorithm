# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 22:07:11 2018

@author: guyo
"""

class Node(object):
    def __init__(self,data):
        self.info = data
        self.link = None
        
class CircularLinkList(object):
    def __init__(self):
        self.last = None
    def display_list(self):
        if self.last == None:
            print("List is empty\n")
            return
        p = self.last.link
        while True:
            print(p.info, "  ", end=' ')
            p = p.link
            if p == self.last.link:
                break
        print()
    def insert_in_beginning(self,data):
        temp = Node(data)
        temp.link = self.last.link
        self.last.link = temp
    def insert_in_empty_list(self,data):
        temp = Node(data)
        self.last = temp
        self.last.link = self.last
    def insert_at_end(self,data):
        temp = Node(data)
        temp.link = self.last.link
        self.last.link = temp
        self.last = temp
    def create_list(self):
        n = int(input("Enter the numbers of Node to be created "))
        if n == 0:
            return  
        data = int(input("Enter the element to be inserted "))
        self.insert_in_empty_list(data)
        for i in range(n-1):
            data = int(input("Enter the element to be inserted "))
            self.insert_at_end(data)
    def insert_after(self,data,x):
        p = self.last.link
        while True:
            if p.info == x:
                break
            p = p.link
            if p.link == self.last.link:
                break
        if p == self.last.link and p.info != x:
            print(x, " is not in the list")
        else:
            temp = Node(data)
            temp.link = p.link
            p.link = temp
            if p == self.last:
                self.last = temp
    def delete_first_node(self):
        if self.last == None:
            return 
        if self.last == self.last.link:
            self.last = None
            return
        self.last.link = self.last.link.link
    def delete_last_node(self):
        if self.last == None:
            return
        if self.last == self.last.link:
            self.last = None
            return
        p = self.last.link
        while True:
            if p.link == self.last:
                break
            p = p.link
        p.link = self.last.link
        self.last = p
    def delete_node(self,x):
        if self.last == None:
            return
        if self.last.link == self.last and self.last.info == x:
            self.last = None
            return
        if self.last.link.info == x:
            self.last.link = self.last.link.link
        p = self.last.link
        while p.link != self.last.link:
            if p.link.info == x:
                break
            p  = p.link
            if p.link == self.last.link:
                print (x, " is not in the list")
            else:
                p.link = p.link.link
                if self.last.info == x:
                    self.last = p 
        
        
        
list = CircularLinkList()
list.create_list()


while True:
    option = int(input("Enter your choice :"))
    if option == 1:
        list.display_list()
    elif option == 2:
        data = int(input("Enter the element to be inserted : "))
        list.insert_in_empty_list(data)        
    elif option == 3:
        data = int(input("Enter the element to be inserted : "))
        list.insert_in_beginning(data)
    elif option == 4:
        data = int(input("Enter the element to be inserted : "))
        list.insert_at_end(data)        
    elif option == 5:
        data = int(input("enter the element to be inserted : "))
        x = int(input("enter the position at wich to insert"))
        list.insert_after(data,x)
    elif option == 6:
        list.delete_first_node()
    elif option == 7:
        list.delete_last_node()
    elif option == 8:
        x = int(input("enter the element to be deleted "))
        list.delete_node(x)