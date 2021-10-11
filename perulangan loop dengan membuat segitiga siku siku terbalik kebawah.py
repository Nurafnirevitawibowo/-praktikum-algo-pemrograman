# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 13:45:34 2021
perulangan loop dengan membuat segitiga siku siku terbalik kebawah
Nurafni Revita Wibowo
NIM 065002100013
@author: Afni
"""
n = int(input("masukin angka:"))
for baris in range(n,0,-1):
    for kolom in range(1, baris+1):
        print(baris, end='')
    print()