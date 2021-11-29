# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 14:10:51 2021

@author: Afni
"""
print ("fungsi binary search mencari element didalam list jika list acak maka urutkan dengan fungsi sorting")
print("Sebelum diurutkan [0,8,2,12,4,10,6,14,20,16,18]")
def bubbleSort(array):
    for passnum in range(len(array)-1,0,-1):
        for i in range(passnum):
            if array[i]>array[i+1]:
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp

def binary_search(array,num_find):

    start = 0
    end = len(array) - 1
    mid = (start + end)//2
    found = False
    position = -1
    bubbleSort(array)
    while start <= end:
        if array[mid] == num_find:
            found = True
            position = mid
            break
        if num_find > array[mid]:
            start = mid + 1
            mid = (start + end)//2
        else:
            end = mid - 1
            mid = (start + end)//2

    print("Sesudah diurutkan: ", array)
    return (found, position-1)

array=[0,8,2,12,4,10,6,14,20,16,18]
num = int(input('Masukkan angka yang dicari: '))

found = binary_search(array,num )
if found[0]:
    print('Nomor %d ditemukan di posisi %d'%(num, found[1]+2))
else:
    print('Nomor %d tidak ditemukan'%num)