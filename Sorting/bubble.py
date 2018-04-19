# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 12:14:17 2018

@author: guyo
"""

def Bubble_sort(a):
    for x in range(len(a)-1, 0 , -1):
        swaps = 0
        for j in range(x):
            if a[j]> a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
                swaps +=1
        if swaps == 0:
            break
list1 = [6,3,1,5,9,8]
list2 = [4]
list3= [10,9,8,7,6,5,4,3,2,1,0]
Bubble_sort(list1)
Bubble_sort(list2)
Bubble_sort(list3)
print(list1)
print(list2)
print(list3)