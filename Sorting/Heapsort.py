# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 19:41:29 2018

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
#        
#
def heap_sort(a):
    n = len(a)-1
    #temp = [0]
    #a = temp+a
    build_heap_bottom_up(a,n)
    while n > 1:
        max_value = a[1]
        a[1] = a[n]
        a[n] = max_value
        n = n-1
        restore_down(1,a,n)
         

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
#hp = Heap()
list = [999,6,3,1,5,9,8]
heap_sort(list)
print(list)
#new_list = [None]*len(list)
#for i in range(len(list)):
#    hp.insert(list[i])
#for i in range(len(list),0,-1):
#    new_list[i-1] = hp.delete_root()
#print(new_list)