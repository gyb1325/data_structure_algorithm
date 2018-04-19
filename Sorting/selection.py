# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 11:52:40 2018

@author: guyo
"""

#def selection_sort(a):
#    for i in range(len(a)-1):
#        minIndex = i
#        for j in range(i+1, len(a)):
#            if a[j]< a[minIndex]:
#                minIndex =j
#        if i != minIndex:
#            a[i],a[minIndex]= a[minIndex],a[i]

def selection_sort(a):
    for i in range(len(a)-1):
        min_index = i
        for j in range(i+1,len(a)):
            if a[j]<a[min_index]:
                min_index = j
        if min_index != i:
            a[min_index],a[i] =a[i] ,a[min_index]

list1 = [6,3,1,5,9,8]
list2 = [4]
selection_sort(list1)
selection_sort(list2)
print(list1)
print(list2)
