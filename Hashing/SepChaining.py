# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 00:23:27 2018

@author: guyo
"""

class StudentRecords:
    def __init__(self, i, name):
        self.id = i
        self.name = name
        
    def get_student_id(self):
        return self.id
    def set_student_id(self,i):
        self.id = i
    def __str__(self):
        return str(self.id) + " " + self.name
class Node:
    def __init__(self,data):
        self.info = data
        self.link = None
class SingleLinkedList:
    def __init__(self):
        self.start = None
    def display_list(self):
        if self.start is None:
            print("______")
        else:
            p = self.start
            while p is not None:
                print(p.info , " ", end = ' '  )
                p = p.link
            print()
        
    
    def search(self,x):
        p = self.start
        while p is not None:
            if p.info.get_student_id() == x:
                return p.info
            p = p.link
        return None    
    def insert_in_beginning(self, data):
        temp = Node(data)
        temp.link = self.start
        self.start = temp
    def delete_node(self,x):
        if self.start is None:
            print("The link list is empty")
            return
        
        if self.start.info.get_student_id() == x:
            self.start =self.start.link
            return
        
        p = self.start
        while p.link is not None:
            if p.link.info.get_student_id() == x:
                break
            p = p.link
        if p.link is None:
            print("Element ", x ," is not in the list")
        else:
            p.link = p.link.link
            

            
class HashTable:
    def __init__(self,table_size):
        self.m = table_size
        self.array = [None]*self.m
        self.n = 0
    def hash(self,key):
        return (key%self.m)
    def display_table(self):
        for i in range(self.m):
            print("[ ",i, " ]  -->  ", end ="")
            if self.array[i] != None:
                self.array[i].display_list()
            else:
                print("____")
    def search(self, key):
        h = self.hash(key)
        if self.array[h] is not None:
            return self.array[h].search(key)
        return None
    def insert(self,newRecord):
        key = newRecord.get_student_id()
        h = self.hash(key)
        if self.array[h] is None: 
            self.array[h] = SingleLinkedList()
        self.array[h].insert_in_beginning(newRecord)
        self.n += 1
    def delete(self,key):
        h = self.hash(key)
        if self.array[h] is not None: 
            self.array[h].delete_node(key)
            self.n -= 1
        else:
            print("Value ", key , "is not present")
            
            
size = int(input("Enter the size of the table: "))
table = HashTable(size)
while True:
    option =int(input("Enter your option: "))
    if option ==1:
        id = int(input("Student id is: "))
        name = input("Student name is: ")
        aRecord = StudentRecords(id,name)
        table.insert(aRecord)
    elif option ==2:
        id = int(input("Student id to be search is: "))
        aRecord = table.search(id)
        if aRecord is not None:
            print(aRecord)
        else:
            print("Key is not found")
    elif option ==3:
        id = int(input("Student id to be deleted is: "))
        table.delete(id)
    elif option ==4:
        table.display_table()
    elif option ==5:
        break
    print()   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    