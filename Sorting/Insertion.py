# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 13:24:21 2018

@author: guyo
"""

def insertion_sort(a):
    for i in range(1,len(a)):
        temp= a[i]
        j = i-1
        while j>=0 and a[j]>temp:
            a[j+1] = a[j]
            j = j-1
        a[j+1] = temp
list1 = [6,3,1,5,9,8]
list2 = [4]
list3= [10,9,8,7,6,5,4,3,2,1,0]
insertion_sort(list1)
insertion_sort(list2)
insertion_sort(list3)
print(list1)
print(list2)
print(list3)