# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 14:07:39 2021

@author: Afni
"""

n = '0'
total = 0
menampung = 0

def kategori(n="0", total=0, menampung =0):
    while (n != "") :
         n = str(input("masukkan nilai :"))
         menampung = menampung + 1
         if (n == ''):
                return total/ (menampung-1)
         elif (n== 'A'):
             print ("nilai = 4.00")
             total += 4.00
         elif (n == 'A-'): 
              print ("nilai = 3.75")
              total += 3.75
         elif (n== 'B+'):
            print ("nilai = 3.50")
            total += 3.50
         elif (n == 'B'):
             print ("nilai = 3.00")
             total += 3.00
         elif (n== 'B-'):
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
            print ("masukkan nilai yang benar")
ratarata = kategori ()
print("rataratanya adalah:", ratarata)