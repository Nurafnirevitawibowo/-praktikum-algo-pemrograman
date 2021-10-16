# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 11:52:23 2021
Nurafni Revita Wibowo
NIM 065002100013
@author: Afni
"""

#
print(" This program will determine the number of days of a given month")
print(" Enter -1 to stop the program")
n = ''
t = ''
while n != -1:
    n = int(input(" masukan bulan (1-12) = "))
    if n == 1:
        print(" ada 31 hari dalam sebulan ")
        print(" Masukkan -1 untuk menghentikan program ")
    elif n == 2:
        t = int(input(" masukan tahun (e.g., 2021) = "))
        if t % 4 == 0 and t % 100 != 0 or t % 400 == 0:
            print (" Ada 29 hari dalam sebulan ")
            print(" Masukkan -1 untuk menghentikan program ")
        else:
            print(" Ada 28 hari dalam sebulan ")
            print(" Masukkan -1 untuk menghentikan program ")
    elif n == 3:
        print(" Ada 31 hari dalam sebulan ")
        print(" Masukkan -1 untuk menghentikan program ")
    elif n == 4:
        print(" Ada 31 hari dalam sebulan ")
        print(" Masukkan -1 untuk menghentikan program ")
    elif n == 5:
        print(" Ada 31 hari dalam sebulan ")
        print(" Masukkan -1 untuk menghentikan program ")
    elif n == 6:
        print(" Ada 30 hari dalam sebulan ")
        print(" Masukkan -1 untuk menghentikan program ")
    elif n == 7:
        print(" Ada 31 hari dalam sebulan ")
        print(" Masukkan -1 untuk menghentikan program ")
    elif n == 8:
        print(" Ada 31 hari dalam sebulan ")
        print(" Masukkan -1 untuk menghentikan program ")
    elif n == 9:
        print(" Ada 30 hari dalam sebulan ")
        print(" Masukkan -1 untuk menghentikan program ")
    elif n == 10:
        print(" Ada 31 hari dalam sebulan ")
        print(" Masukkan -1 untuk menghentikan program ")
    elif n == 11:
        print(" Ada 30 hari dalam sebulan ")
        print(" Masukkan -1 untuk menghentikan program ")
    elif n == 12:
        print(" Ada 31 hari dalam sebulan ")
        print(" Masukkan -1 untuk menghentikan program ")
    elif n >= 12:
        print(" Nilai yang dimasukkan tidak valid = ", n)
    else:
        print(" selesai ")
