# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 15:46:58 2018

@author: guyo
"""

#def merge(a1,a2, temp):
#    i = 0
#    j = 0
#    k = 0
#    n1 = len(a1)
#    n2 = len(a2)
#    while i <=n1-1 and j <= n2-1:
#        if a1[i] > a2[j]:
#            temp[k] = a2[j]
#            j +=1
#        else:
#            temp[k] = a1[i]
#            i +=1
#        k += 1
#        
#    while i <= n1-1:
#        temp[k] = a1[i]
#        i +=1
#        k += 1
#    while j <= n2-1:
#        temp[k] = a2[j]
#        j +=1
#        k += 1        
def merge_sort(a):
    n = len(a)
    temp = [None]*n
    sort(a, temp, 0, n-1)

def sort(a, temp, low, up):
    if low == up:
        return
    mid = (low+up)//2
    sort(a, temp, low, mid)
    sort(a, temp, mid+1, up)
    merge(a,temp, low, mid, mid+1, up)
    copy(a,temp, low, up)

    
def merge(a, temp, low1, up1, low2,up2):
    i = low1
    j = low2
    k = low1
    while i <=up1 and j <= up2:
        if a[i] > a[j]:
            temp[k] = a[j]
            j +=1
        else:
            temp[k] = a[i]
            i +=1
        k += 1
        
    while i <=up1:
        temp[k] = a[i]
        i +=1
        k += 1
    while j <= up2:
        temp[k] = a[j]
        j +=1
        k += 1    
def copy(a, temp, low, up):
    for i in range(low,up+1):
        a[i] = temp[i]

list1 = [2,11,15, 19, 5,6,7,8]
list2 = [6,3,1,5,9,8]

merge_sort(list2)
print(list2)