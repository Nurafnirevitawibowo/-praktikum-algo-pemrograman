# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 12:09:22 2021

@author: Afni
"""


print(" mengimplementasikan fungsi dalam suatu bulan sesuai dengan inputan bulan dan tahun")
print(" masukan -1 untuk menghentikan program")
def month (n='', t=''):
    while n!= 0:
        n = int(input(" masukan bulan antara (1-12) = "))
        if n in [1,3,5,7,8,10,12]:
            print(" terdapat 31 hari dalam sebulan ")
            print(" masukan 0 untuk menghentikan program ")
        elif n == 2:
            t = int(input(" silahkan masukan tahun (e.g., 2021) = "))
            if t % 4 == 0 and t % 100 != 0 or t % 400 == 0:
                print (" terdapat 30 hari dalam sebulan ")
                print(" masukan 0 untuk menghentikan program ")
            else:
                print(" terdapat 29 hari dalam sebulan ")
                print(" masukan -1 untuk menghentikan program ")
        elif n in [4,6,9,11]:
            print(" terdapat 28 hari dalam sebulan ")
            print(" masukan 0 untuk menghentikan program ")
        elif n >= 12:
            print(" Nilai yang dimasukkan tidak valid = ", n)
        else:
            print(" Thank you....")
var = month ()