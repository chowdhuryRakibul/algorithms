# -*- coding: utf-8 -*-
"""
Created on Mon Mar  10 13:43:57 2020

@author: Shimanto
"""
#sort the list A in ascending order using bubble sort method
def bubbleSort(A):
    n = len(A)
    for i in range(n):
        for j in range(n-i-1):
            if A[j] > A[j+1]:
                A[j] , A[j+1] = A[j+1], A[j]
    return A
#sort the list A in ascending order using insertion sort method
def insertionSort(A):
    n = len(A)
    for i in range(1,n):
        for j in range(i,0,-1):
            if A[j-1] > A[j]:
                A[j-1] , A[j] = A[j], A[j-1]
                print(A)
            else:
                break
    return A

#sort the list A in ascending order using selection sort method
def selectionSort(A):
    n = len(A)
    for i in range(n):
        min_idx = i
        for j in range(i,n):
            if A[min_idx] > A[j]:
                min_idx = j
        A[min_idx] , A[i] = A[i],A[min_idx]
    return A

#sort the list A in ascending order using merge sort method
def mergeSort(A):
    if len(A) > 1:
        mid = int(len(A)/2)
        
        L = A[:mid]
        R = A[mid:]
        
        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
            k += 1
        #check if anything is left in L or R matrix
        while i < len(L):
            A[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            A[k] = R[j]
            j += 1
            k += 1
    return A


A = [6,4,9,5,1,2]
bubbleSort(A)
A = [6,4,9,5,1,2]
insertionSort(A)
A = [6,4,9,5,1,2]
selectionSort(A)
A = [6,4,3,5,1,2]
mergeSort(A)