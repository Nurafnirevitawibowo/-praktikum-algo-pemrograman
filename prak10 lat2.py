# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 12:07:23 2021

@author: Afni
"""
print("implementasikan fungsi dan percabangan serta perulangan dapat membuat file,membaca file dan menambahkan text ke dalam file")
def BuatTulis(data):
    file = open(namafile+".txt", "w")
    file.write(data)
    file.close()
    
def BuatBaca():
    file = open(namafile+".txt", "r")
    text = file.read()
    print(text)
    file.close()
    
def BuatTambah(data):
    file = open(namafile+".txt", "a")
    file.write(data)
    file.close()
    

salah=False
while (not salah) :
    try:
        print("====PROGRAM FILE HANDLING====")
        print("1. Membuat dan Menulis File")
        print("2. Membaca File")
        print("3. Menambahkan Text Pada File")
        print("4. Keluar dari Program")
        print("")
        pilih=int(input("Masukan Pilihan Berupa Angka (1/2/3/4): "))
        if pilih==4 :
            salah=True
            print("Terimakasih Sudah Meggunakan Program Saya")
        elif pilih==1:
            namafile=input("Masukan Nama File: ")
            nama=input("Masukan Namamu: ")
            nim=int(input("Masukan NIM kamu: "))
            tahun=int(input("Masukan Tahun Angkatanmu: "))
            data="Nama: {}\nNIM: {}\nAngkatan: {}".format(nama,nim,tahun)
            BuatTulis(data)
            print("\n\nFile Berhasil dibuat\n\n")
        elif pilih==2:
            namafile=input("Masukan Nama File: ")
            print("")
            print("")
            BuatBaca()
            print("")
            print("")
        elif pilih==3:
            namafile=input("Masukan Nama File: ")
            Nama=input("Masukan Nama Temanmu: ")
            catatan=input("Masukan Catatan Tambahahn Kamu: ")
            data="\nNama Teman: {}\nCatatan: {}".format(Nama,catatan)
            print("")
            BuatTambah(data)
            print("\n\nFile Berhasil ditambahkan\n\n")
        else :
            print("\nDATA INVALID!!\nUlangi lagi!!!\n")
    except ValueError:
        print("\n\nERROR!!\nMasukan data dengan benar!\n\n\n")
    except FileNotFoundError:
        print("\n\nERROR!!\nFile yang dicari tidak ada!\n\nTulis nama file dengan benar!\n\n")