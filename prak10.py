# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 09:34:41 2021

@author: Afni
"""
# input output file



"""
w = write mode / mode menulis dan menghapus file lama, jika file tidak ada maka akan dibuat file baru
r = read mode only / hanya bisa baca
"""
# membuat file text
print("Text File dengan nama Biodata.txt menggunakan impelementasi File Handling")

def write(data):
    f = open("Biodata.txt", "w")
    f.write(data)
    f.close()
    
def read():
    h = open("Biodata.txt", 'r')

    line = h.readline()
    print(line)
    while line:
        line = h.readline()
        print(line)

    h.close()
        
print ("Masukan Biodata kamu")

nama = input("Nama: ")
umur = input("Umur: ")
alamat = input("Alamat: ")
email = input ("Email:")
dosen = input ("Dosen :")
data= "Nama: {}\nUmur: {}\nAlamat: {}\nEmail: {}\nDosen: {}\n".format(nama, umur, alamat, email, dosen)

print("=========================")
write(data)
print("ini nih data kamu")
read()

