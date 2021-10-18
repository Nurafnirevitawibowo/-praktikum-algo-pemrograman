# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 14:19:34 2021

@author: Afni
"""

print("menghitung nilai rata rata")
n= "0"
nilaidarikondisi= list()
total = 0
n= 0
while(n!= "0"):
    n = str(input("masukkan nilai dari kondisinya :"))
    if (n==""):
        break;    
    elif(n== "A"):
        print (" nilainya adalah 4,00")
        total +=4
    elif(n== "A-"):
        print("nilainya adalah 3,75")
        total += 3,75
    elif(n== "B+ "):
        print("nilainya adalah 3,50")
        total += 3,50
    elif(n== "B"):
        print("nilainya adalah 3,00")
        total += 3,00
    elif(n== "B-"):
        print("nilainya adalah 2,75")
        total += 2,75
    elif(n== "C+"):
        print("nilainya adalah 2,50")
        total += 2,50
    elif(n== "C"):
        print("nilainya adalah 2,00")
        total += 2,00
    elif(n== "C-"):
        print("nilainya adalah 1,75")
        total += 1,75
    elif(n== "D"):
        print("nilainya adalah 1,50")
        total += 1,50
    elif(n== "E"):
        print("nilainya adalah 1,25")
        total += 1,25
    else:
        print("masukkan nilai dari kondisinya yang benar")
        n= 0
    print((f"Nilai= {n}"))
    nilaidarikondisi.append(n)
    
ratarata = sum(nilaidarikondisi) / len(nilaidarikondisi)
print("rata rata nilai siswa: " ,ratarata)
    
    