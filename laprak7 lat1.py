# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 16:45:01 2021

@author: Afni
"""
#implementasi menentukan bilangan prima atau bukan 

def kategoribilangan(bil):
    if bil == 1:
        print("bilangan {bil} adalah bilangan prima")
    elif bil == 2:
        print("bilangan {bil} adalah bilangan prima")
    else:
        global x 
        for x in range(2, bil):
            if bil % x == 0: 
                stat = 0 
                break
            else:
                stat = 1 
        cekstat(stat)
def cekstat(stat):
    if stat == 0:
        print("bilangan {bil} bukan bilangan prima")
        print("{x} kali {bil//x} = {bil}")
    else:
        print("{bil} adalah bilangan prima")
a = 1
while a == 1 :
    bil = int(input("masukan angka : "))
    kategoribilangan (bil)  
    break     
bil = int(input("masukan angka : "))
