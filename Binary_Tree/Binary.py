# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 13:28:30 2018

@author: guyo
"""
from collections import deque

class Node:
    def __init__(self,value):
        self.info = value
        self.lchild = None
        self.rchild = None
class BinaryTree:
    def __init__(self):
        self.root = None
    def is_empty(self):
        return self.root == None
    def display(self):
        pass
    def preorder(self):
        self._preorder(self.root)
        print()
    def _preorder(self,p):
        if p is None:
            return
        print(p.info," ", end = ' ')
        self._preorder(p.lchild)
        self._preorder(p.rchild)
        
    def inorder(self):
        self._inorder(self.root)
        print()        
    def _inorder(self,p):
        if p is None:
            return        
        self._inorder(p.lchild)
        print(p.info," ", end = ' ')
        self._inorder(p.rchild)    
    def postorder(self):
        self._postorder(self.root)
        print()
    def _postorder(self,p):
        if p is None:
            return        
        self._postorder(p.lchild)
        self._postorder(p.rchild)          
        print(p.info," ", end = ' ') 
    def levelorder(self):
        if self.is_empty():
            print("The tree is empty")
            return
        qu = deque()
        qu.append(self.root)
        while len(qu) != 0:
            p = qu.popleft()
            print(p.info," ", end = ' ')
            if p.lchild != None:
                qu.append(p.lchild)
            if p.rchild != None:
                qu.append(p.rchild)
    def findheight(self):
        return self._findheight(self.root)

    def _findheight(self, p):
        if p is None:
            return 0
        hL = self._findheight(p.lchild)
        hR = self._findheight(p.rchild)
        if hL > hR:
            return hL+1
        else:
            return hR+1
            
    def create_tree(self):
        self.root = Node('P')
        self.root.lchild = Node('Q')
        self.root.rchild = Node('R')        
        self.root.lchild.lchild = Node('A')
        self.root.lchild.rchild = Node('B')
        self.root.rchild.lchild = Node('X')
        
bt = BinaryTree()
bt.create_tree()
#bt.display()
bt.preorder()
bt.inorder()
bt.postorder()
bt.levelorder()