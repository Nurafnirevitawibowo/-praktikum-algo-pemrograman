# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 13:08:40 2021

@author: afni
"""

print("implementasi class yang memiliki nama class mahasiswa dan memiliki method yang dapat digunakan untuk menampilkan biodata")

class Mahasiswa:
    mahasiswaCount = 0
    
    def _init_(self, nama, nim, angkatan):
        self.nama = nama
        self.nim = nim
        self.angkatan = angkatan
        Mahasiswa.mahasiswaCount += 1
        
    def printMaha(self):
        print("Nama : " + self.nama + "\nNim " + str(self.nim)+ "\nAngkatan :" + str(self.angkatan))
                
nama=input ("Masukan Namamu :")
nim=str(input("masukan NIM-mu :"))
angkatan=str(input("Masukan Angkatanmu :"))
print("=========================")

maha = Mahasiswa(nama,nim,angkatan)
maha.printMaha()
print("")
print("Total Mahasiwanya adalah", Mahasiswa.mahasiswaCount)

