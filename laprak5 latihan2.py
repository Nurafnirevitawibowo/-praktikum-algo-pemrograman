# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 11:04:43 2021

@author: Afni
"""

print (' Selamat Datang di KEBUN BINATANG RAGUNAN')
print (' silahkan membeli tiket trerlebih dahulu ')

n = '0'
total = 0
a = 0
b = 0


while n != '':
    n = float(input(' Berapa Umurnya = '))
    a += 1
    if n == 0 :
        break;    
    elif n <= 2 :
        print (' Harga = Gratis')
        total += 0
        print (" Totalnya adalah = ", total)
    elif n >= 3  and n <= 12 :
        print (' Harga = $14.00')
        total += 14.00
        print (" Totalnya adalah = ", total)
    elif n >= 65 :
        print (' Harga = $18.00')
        total += 18.00
        print (" Totalnya adalah = ", total)
    else :
        print (' Harga = $23.00')
        total += 23.00
        print (" Totalnya adalah = ", total)
if a == 1:
        print (" Gratisss ")
else :
        b =float(input(' Masukan Uang Anda ='))
        kembalian = b-total
        print (" Kembaliannya adalah :", kembalian)