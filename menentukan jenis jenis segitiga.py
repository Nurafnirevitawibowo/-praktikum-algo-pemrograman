# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 14:50:55 2021

@author: Afni
"""

print("menentukan  jenis jenis segitiga")
a = float(input("panjang sisi A:"))
b = float(input("panjang sisi B:"))
c = float(input("panjang sisi C:"))


if(a == b == c):
    print("ini adalah segitiga sama sisi")
elif((a + b <= c) or (a + c <= b) or (b + c <= a)):
    print(" ini adalah bukan segitiga")
elif (a==b) or (b==c) or (c==a):
    print("ini adalah segitiga sama kaki")
else:
    print("merupakan segitiga sembarang")