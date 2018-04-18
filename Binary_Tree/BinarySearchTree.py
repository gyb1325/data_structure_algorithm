# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 20:27:06 2018

@author: guyo
"""
from collections import deque



class TreeEmptyError(Exception):
    pass
class Node:
    def __init__(self,value):
        self.info = value
        self.lchild = None
        self.rchild = None
class BinarySearchTree:
    def __init__(self):
        self.root = None
    def is_empty(self):
        return self.root == None
    def insert(self,x):
        self.root = self._insert(self.root,x)
    def _insert(self,p,x):
        if p is None:
            p = Node(x)
        elif x <p.info:
            p.lchild = self._insert(p.lchild,x)
        elif x > p.info:
            p.rchild = self._insert(p.rchild,x)   
        else:
            print(x," is alreay is the tree")
        return p
    def insert1(self,x):
        p = self.root
        par = None
        while p is not None:
            par = p
            if x < p.info:
                p = p.lchild
            elif x >p.info:
                p = p.rchild
            else:
                print(x," is alreay is the tree")
                return
        temp = Node(x)
        if par == None:
            self.root = temp
        elif par.info <x:
            par.rchild = temp
        else:
            par.lchild = temp
    def delete(self,x):
        self.root = self._delete(self.root, x)
    def _delete(self,p,x):
        if p is None:
            print(x, " is not Found")
            return p 
        if p.info < x :
            p.rchild = self._delete(p.rchild,x)
        elif p.info >x:
            p.lchild = self._delete(p.lchild,x)
        else:
            if p.lchild != None and p.rchild != None:
                s = p.rchild
                while s.lchild is not None:
                    s = s.lchild
                p.info = s.info
                p.rchild = self._delete(p.rchild,s.info)
            else:
                if p.lchild is not None:
                    ch = p.lchild
                else:
                    ch = p.rchild
                p = ch
        return p
                
    def delete1(self,x):
        p = self.root
        par = None
        while p is not None:
            if x == p.info:
                break
            par = p
            if x <p.info:
                p = p.lchild
            else: 
                p = p.rchild
        if p is None:
            print(x, " is not Found")
            return
        
        #Case C : 2 children
        #Find inorder successor and its parents
        if p.lchild != None and p.rchild != None:
            ps = p
            s = p.rchild
            while s.lchild is not None:
                ps = s
                s = s.lchild
            p.info = s.info
            par = ps
            p = s 
        if p.lchild is not None:
            ch = p.lchild
        else:
            ch = p.rchild
        if par == None:
            self.root = ch
        elif p == par.lchild:
            par.lchild = ch
        else:
            par.rchild = ch
       
    def search(self,x):
        return self._search(self.root,x)
    def _search(self, p ,x):
        if p is None:
            return False
        if p.info > x:
            return self._search(p.lchild,x)
        elif p.info < x:
            return self._search(p.rchild,x)
        else:
            return True
    
    def search1(self,x):
        p = self.root
        while p is not None:
            if x < p.info:
                p = p.lchild
            elif x > p.info:
                p = p.rchild
            else:
                return True
        return False
    def min1(self):
        if self.root == None:
            raise TreeEmptyError("Tree is empty")
        p = self.root
        while p.lchild is not None:
            p = p.lchild
        return p
    def max1(self):
        if self.root == None:
            raise TreeEmptyError("Tree is empty")
        p = self.root
        while p.rchild is not None:
            p = p.rchild
        return p
    def max2(self):
        if self.root == None:
            raise TreeEmptyError("Tree is empty")        
        return self._max(self.root)
    def _max(self, p ):
        if p.rchild == None:
            return p
        return self._max(self.rchild)
    def min2(self):
        if self.root == None:
            raise TreeEmptyError("Tree is empty")        
        return self._min(self.root)
    def _min(self, p ):
        if p.rchild == None:
            return p
        return self._min(self.lchild)    
    def preorder(self):
        self._preorder(self.root)
    def _preorder(self,p):
        if p is None:
            return
        print(p.info," ", end = ' ')
        self.preorder(p.lchild)
        self._preorder(p.rchild)
    def inorder(self):
        self._inorder(self.root)
    def _inorder(self,p):
        if p is None:
            return
        self.preorder(p.lchild)
        print(p.info," ", end = ' ')
        self._preorder(p.rchild)        
    def postorder(self):
        self._inorder(self.root)
    def _postorder(self,p):
        if p is None:
            return
        self.preorder(p.lchild)
        self._preorder(p.rchild)   
        print(p.info," ", end = ' ')
    def levelorder(self):
        if self.is_empty():
            print("The tree is empty")
            return
        dq = deque()
        dq.append(self.root)
        while len(dq) != 0:
            p = dq.popleft()
            print(p.info," ", end = ' ')
            if p.lchild is not None:
                dq.append(p.lchild)
            if p.rchild is not None:
                dq.append(p.rchild)    
    
    def height(self):
        return self._height(self.root)
    def _height(self, p):
        if p is None:
            return 0
        hL = self._height(p.lchild)
        hR = self._height(p.rchild)
        if hL > hR:
            return hL+1
        else:
            return hR+1
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        