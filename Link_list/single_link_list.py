#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 23:32:09 2018

@author: yongbingu
"""

class Node:
    def __init__(self,value):
        self.info = value
        self.link = None
        
        
        
        
class SingleLinkedList:
    def __init__(self):
        self.start = None
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
        
    def count_nodes(self):
        p = self.start
        n = 0
        while p is not None:
            n += 1
            p = p.link
        print("Number of nodes is in the list - ", n)
    
    def search(self,x):
        p = self.start
        position = 1
        while p is not None:
            if p.info == x:
                print(x, " is at position ", position)
                return True
            position += 1
            p = p.link
        print(x, " is not in the List")    
        return False    
    def insert_in_beginning(self, data):
        temp = Node(data)
        temp.link = self.start
        self.start = temp
    def insert_at_end(self, data):
        temp = Node(data)
        if self.start is None:
            self.start = temp
            return
        
        p = self.start
        while p.link is not None:
            p = p.link
        p.link = temp
    def create_list(self):
        n = int(input("Enter the node you want to create "))
        if n == 0:
            return
        for i in range(n):
            data = int(input("Please enter the data "))
            self.insert_at_end(data)
    def insert_after(self,data,x):
        p = self.start
        while p is not None:
            if p.info == x:
                break
            p = p.link
        if p is None:
            print(x," is not present in the list")
            return
        temp = Node(data)
        temp.link = p.link
        p.link = temp
    def insert_before(self,data,x):
        if self.start is None:
            print("List is empty")
            return
        if self.start.info == x:
            temp = Node(data)
            temp.link = self.start
            self.start = temp
            return
        
        p = self.start
        while p.link is not None:
            if p.link.info == x:
                break
            p = p.link
        if p.link is None:
            print(x, " is not present in the list")
        else:
            temp = Node(data)
            temp.link = p.link
            p.link = temp
    def insert_at_position(self, data, k):
        if k == 1:
           temp = Node(data)
           temp.link = self.start
           self.start = temp
           return      
        p = self.start
        i = 1
        while i < k-1 and p is not None:
            p = p.link
            i += 1
        if p is None:
            print ("You can only insert upto postion", i)
        else:
            temp = Node(data)
            temp.link = p.link
            p.link = temp
    def delete_node(self,x):
        if self.start is None:
            print("The link list is empty")
            return
        if self.start.info == x:
            self.start = self.start.link
            return
        p = self.start
        while p.link is not None:
            if p.link.info == x:
                break
            p = p.link
        if p.link is None:
            print("Element ", x ," is not in the list")
        else:
            p.link = p.link.link
            
    def delete_first_node(self):
        if self.start is None: 
            print("The link list is empty")
            return
        self.start = self.start.link
    def delete_last_node(self):
        if self.start is None: 
            print("The link list is empty")
            return
        if self.start.link is None:
            self.start = None
        p = self.start
        while p.link.link is not None:
            p = p.link
        p.link = None
            
    def reverse_list(self):
        prev = None
        p = self.start
        while p is not None:
            next = p.link
            p.link = prev
            prev = p
            p = next
        self.start = prev
    def bubble_sort_exdata(self):
        end = None
        while end != self.start.link:
            p = self.start
            while p.link != end:
                q = p.link
                if p.info > q.info:
                    temp = p.info
                    p.info = q.info
                    q.info = temp
                p = p.link
            end = p
            
    def bubble_sort_exlinks(self):
        end =None
        while end != self.start.link:
            r= p = self.start
            while p.link != end:
                q = p.link
                if p.info > q.info:
                    p.link = q.link
                    q.link = p
                    if p !=self.start:
                        r.link = q
                    else:
                        self.start = q
                    p,q = q,p
                r= p 
                p = p.link
            end = p
                    
                    
    def has_cycle(self):
        pass
    def find_cycle(self):
        pass
    def remove_cycle(self):
        pass
    def insert_cycle(self):
        pass
    def merge1(self,list2):
        mergelist = SingleLinkedList()
        mergelist.start = self._merge1(self.start, list2.start)
        return mergelist
    def _merge1(self, p1, p2):
        if p1.info > p2.info:
            startM = Node(p2.info)
            p2 = p2.link
        else:
            startM = Node(p1.info)
            p1 = p1.link
        pM = startM
        while p1 is not None and p2 is not None:
            if p1.info > p2.info:
                pM.link = Node(p2.info)
                p2 = p2.link
            else:
                pM.link = Node(p1.info)
                p1 = p1.link
            pM = pM.link
        while p1 is not None:
            pM.link = Node(p1.info)
            p1 = p1.link
            pM = pM.link
        while p2 is not None:
            pM.link = Node(p2.info)
            p2 = p2.link
            pM = pM.link 
        return startM
        
                    
    def merge2(self,list2):
        mergelist = SingleLinkedList()
        mergelist.start = self._merge2(self.start, list2.start)
        return mergelist
    def _merge2(self,p1,p2):
        if p1.info > p2.info:
            startM = p2
            p2 = p2.link
        else:
            startM = p1
            p1 = p1.link
        pM = startM
        while p1 is not None and p2 is not None:
            if p1.info > p2.info:
                pM.link = p2
                pM = pM.link
                p2 = p2.link
            else:
                pM.link = p1
                pM = pM.link
                p1 = p1.link
        if p1 is not None:
            pM.link = p1
        else:
            pM.link = p2
        return startM
    def merge_sort(self):
        pass
    def _merge_sort_rec(self, listStart):
        pass
    def _divide_list(self, p):
        pass
    ########################Construction Part#########################3
#list = SingleLinkedList()
#list.create_list()


#while True:
#    option = int(input("Enter your choice :"))
#    if option == 1:
#        list.display_list()
#    elif option == 2:
#        list.count_nodes()
#    elif option == 3:
#        data = int(input("Enter the element to be searched : "))
#        list.search(data)
#    elif option == 4:
#        data = int(input("Enter the element to be inserted : "))
#        list.insert_in_beginning(data)
#    elif option == 5:
#        data = int(input("Enter the element to be inserted : "))
#        list.insert_at_end(data)
#    elif option == 6:
#        data = int(input("enter the element to be inserted : "))
#        x = int(input("enter the position at wich to insert"))
#        list.insert_after(data,x)
#    elif option == 7:
#        data = int(input("enter the element to be inserted : "))
#        x = int(input("enter the position at wich to insert"))
#        list.insert_before(data,x)
#    elif option == 8:
#        data = int(input("enter the element to be inserted : "))
#        k = int(input("enter the position at wich to insert"))
#        list.insert_at_position(data,k)
#    elif option == 9:
#        list.delete_first_node()
#    elif option == 10:
#        list.delete_last_node()
#    elif option == 11:
#        x = int(input("enter the element to be deleted "))
#        list.delete_node(x)
#    elif option ==12:
#        list.reverse_list()
#    elif option == 13:
#        list.bubble_sort_exdata()
#    elif option == 14:
#        list.bubble_sort_exlinks()
    
list1 = SingleLinkedList()
list2 = SingleLinkedList()
list1.create_list()
list2.create_list()

list1.bubble_sort_exdata()
list2.bubble_sort_exdata()

list1.display_list()
list2.display_list()


list3 = list1.merge1(list2)
list1.display_list()
list2.display_list()
list3.display_list()



list4 = list1.merge2(list2)
list1.display_list()
list2.display_list()  
list4.display_list()   
    
    
    
    