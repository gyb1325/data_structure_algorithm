# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 18:56:21 2018

@author: guyo
"""

def quick_sort(a):
    sort(a,0,len(a)-1)
    
def sort(a, low, up):
    if low >= up:
        return
    p = partition(a,low, up)
    sort(a, low, p-1)
    sort(a, p+1, up)
    
def partition(a,low,up):
    pivot = a[low]
    i = low+1
    j = up
    
    while i<=j:
        while a[i] < pivot and i<up:
            i +=1
        while a[j]>pivot:
            j -= 1
        if i<j:
            temp= a[i]
            a[i] = a[j]
            a[j] = temp
            i+= 1
            j-=1
        else:
            break
    a[low] = a[j]
    a[j] = pivot
    return j
            
list2 = [6,3,1,5,9,8]

quick_sort(list2)
print(list2)