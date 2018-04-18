# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 22:13:55 2018

@author: guyo
"""

#class HeapEmptyError(Exception):
#    pass
#class Heap:
#    def __init__(self, default_size = 10):
#        self.a = [None]*default_size
#        self.n = 0
#        self.a[0] = 99999
#    def insert(self,data):
#        self.n = self.n + 1
#        self.a[self.n] = data
#        self.restore_up(self.n)
#    def restore_up(self,x):
#        k = self.a[x]
#        parent = x // 2
#        while self.a[parent] < k:
#            self.a[x] = self.a[parent]
#            x = parent
#            parent = x //2
#        self.a[x] = k
#    def delete_root(self):
#        if self.n == 0:
#            raise HeapEmptyError("Heap is empty")
#        maxValue = self.a[1]
#        self.a[1] = self.a[self.n]
#        self.n -= 1
#        self.restore_down(1)
#        return maxValue 
#    def restore_down(self, i):
#        k = self.a[i]
#        lchild = 2*i
#        rchild = 2*i +1
#        while rchild <= self.n:
#            if k >= self.a[lchild] and k >=self.a[rchild]:
#                self.a[i] = k
#                return
#            else:
#                if self.a[lchild] > self.a[rchild]:
#                    self.a[i] = self.a[lchild]
#                    i = lchild
#                else:
#                    self.a[i] = self.a[rchild]
#                    i = rchild
#            lchild = i *2
#            rchild = i*2 +1
#        if lchild == self.n and k < self.a[lchild]:
#            self.a[i] = self.a[lchild]
#            i = lchild
#        self.a[i] = k
#    def display(self):
#        if self.n == 0:
#            print("Heap is empty")
#            return
#        print("Heap size is ", self.n)
#        for i in range (1, self.n+1):
#            print (self.a[i], " ", end = ' ')
#        print()

    
    
#h = Heap()
#while True:
#    choice = int(input("The choice is "))
#    if choice ==1:
#        value = int(input("Enter the value  "))
#        h.insert(value)
#    elif choice == 2:
#        print("Maximum value is ", h.delete_root())
#    elif choice == 3:
#        h.display()
#    elif choice == 4:
#        break

def build_heap_top_down(a, n):
    for i in range (2,n+1):
        restore_up(i,a)
def restore_up(i, a):
    k = a[i]
    parent = i // 2
    while a[parent] < k:
        a[i] = a[parent]
        i = parent
        parent = i //2
    a[i] = k
def build_heap_bottom_up(a,n):
    i = n//2
    while i >=1:
        restore_down(i, a, n)
        i -= 1
def restore_down(i, a, n):
    k = a[i]
    lchild = 2* i
    rchild = 2*i +1
    while rchild <= n:
        if a[rchild] <= k and a[lchild] <= k:
            a[i] = k
            return
        else:
            if a[lchild] > a[rchild]:
                a[i] = a[lchild]
                i = lchild
            else:
                a[i] = a[rchild]
                i = rchild
        lchild = 2* i
        rchild = 2*i +1
    if lchild == n and a[lchild]>k:
        a[i] = a[lchild]
        i = lchild
    a[i] = k
                
                
    


      
a1 = [999999, 20 ,33,15,6,40,60,45,16,75,10,80,12]
n1 = len(a1)-1
build_heap_bottom_up(a1,n1)
for i in range (1, n1+1): 
    print (a1[i], " ", end = ' ')
print()
a2 = [999999, 20 ,33,15,6,40,60,45,16,75,10,80,12]
n2 = len(a2)-1
build_heap_top_down(a2,n2)
for i in range (1, n2+1): 
    print (a2[i], " ", end = ' ')
print()    