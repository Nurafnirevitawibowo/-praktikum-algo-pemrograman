# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 07:22:08 2021
praktikum3
menentukan nilai rat rata
@author: Afni
"""
r,jumlah,c = 0,0,0
jawab = 'ya'

while jawab == "ya" :
    r = int(input("masukkan nilai mahasiswa :"))
    while (r!= -1) and (r <= 100) :
        c +=1
        jumlah = jumlah + r
        r = int(input("masukkan nilai mahasiswa :"))
    
    if (c!=0):
        ratarata = jumlah/c
        print ("total nilai mahasiswa :", jumlah)
        print ("jumlah mahasiswa :", c)
        print ("nilai rata-rata mahasiswa :", ratarata)
    else :
        print ("rata rata tidak ada")
    u = input("do u wanna continue this program? (ya or tidak):")
    if u == "tidak" and u!="ya" :
        print ("program is stop")
        break;
    print ("thanks for using this program ")