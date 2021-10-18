# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 14:19:34 2021

@author: Afni
"""
print("menghitung nilai rata rata")
n = '0'
total = 0
x = 0

while (n != "") :
    n = str(input("masukkan nilai :"))
    x = x + 1
    if (n == ''):
        break ;
    elif (n== "A"):
        print ("nilai = 4.00")
        total += 4.00
    elif (n == "A-"):
        print ("nilai = 3.75")
        total += 3.75
    elif (n== "B+"):
        print ("nilai = 3.50")
        total += 3.50
    elif (n == 'B'):
        print ("nilai = 3.00")
        total += 3.00
    elif (n== "B-"):
        print ("nilai = 2.75")
        total += 2.75
    elif (n == "C+"):
        print ("nilai = 2.50")
        total += 2.50
    elif (n == "C"):
        print ("nilai = 2.00")
        total += 2.00
    elif (n == "C-"):
        print ("nilai = 1.75")
        total += 1.75
    elif (n == "D"):
        print ("nilai = 1.50")
        total += 1.50
    elif (n == "E"):
        print ("nilai = 1.25")
        total += 1.25
    else :
        x= x-1
        print ("masukkan nilai yang benar :")
if (x ==1):
        print ("rata ratanya adalah 0")
else :
        ratarata  = total/(x-1)
        print ("rata ratanya adalah :", ratarata)