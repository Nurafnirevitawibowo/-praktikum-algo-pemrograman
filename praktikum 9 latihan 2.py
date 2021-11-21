## -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 18:49:11 2021

@author: Afni
NIM; 065002100013
praktikum 9 latihan 2 
"""
print("fungsi perpangkatan menggunakan konsep rekursif")

def pangkat(nomor,doble ) :
    if nomor == 1:
        return 1 
    elif nomor == 0:
        return 0
    else :
        if doble == 1:
            return nomor 
        elif doble == 0:
            return 1
        elif doble > 1 :
            return nomor * pangkat(nomor,doble-1)
        elif doble < 0 :
            return 1/nomor * pangkat(nomor,doble-1)
        else :
            print("data invalid")
            
def start(x=0,y=0):
    print("ini merupakan progam perpangkatan")
    x=int(input("masukan nilai angka yang diinginkan :"))
    y=int(input('masukan nilai pangkat yang diinginkan:'))
    hasil = pangkat(nomor = x,doble = y)
    print("hasil dari  ",x,"pangkat",y,"adalah :",hasil)
    stop()

def stop():
    a=input("ingin tetap melanjutkannya? (ya/tidak)")
    if a == "ya":
        start()
    elif a == "tidak":
        print("thank you")
    else :
        print("data yang anda masukan salah")
        stop()
start()
