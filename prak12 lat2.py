# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 10:12:03 2021

@author: afni

"""

print ("Buatlah sebuah kelas yang menerapkan method getter dan setter dimana menggunakan implementasi program percabangan serta perulangan ")
class OOP:
    
    def _init_(self, nama, nilai):
        self.nama = nama
        self.nilai = nilai
    
    def NamaNilai(self):
        print("\nNama : {}\nNilai : {}\n".format(self.nama,self.nilai))
    
    def get_namanilai(self):
        return self.nama
        return self.nilai
    
        

salah=False
while (not salah):
    try:
        print("------PROGRAM OOP------")
        print("1. Mendeklarasikan Objeks")
        print("2. Menampilkan Objek")
        print("3. Merubah Nilai Objek")
        print("4. Menghapus Objek")
        print("5. Keluar dari Program\n")
        
        pilih=int(input("Masukan Pilihan Berupa Angka (1/2/3/4/5): "))
        
        if pilih == 1 :
            NAMA=input("Masukan namamu : ")
            NILAI=int(input("Masukan nilai mu : "))
            data=OOP(NAMA,NILAI)
            print("\nData Berhasil ditambahkan\n")     
        elif pilih == 2 :
            data.NamaNilai()
        elif pilih == 3 :
            pilih1=input("Apa Yang Ingin diubah(Nama/Nilai)?: ")
            if pilih1 ==  "Nama" :
                NAMA=input("Masukan Nama : ")
                data._nama=NAMA
                print("\nData Berhasil diubah\n")
            elif pilih1 == "Nilai":
                NILAI=int(input("Masukan nilai : "))
                data._nilai=NILAI
                print("\nData Berhasil diubah\n")
            else :
                print("\n\nSilahkan pilih lagi! antara nama atau nilai!\n\n")
        elif pilih == 4:
            data._nama=None
            data._nilai=None
            print("\nData Berhasil dihapus\n")
        elif pilih == 5 :
            salah=True
            print("Terimakasih Sudah Meggunakan Program Saya") 
        else :
            print("\nDATA INVALID!!\nUlangi lagi!!!\n")
            
    except ValueError:
        print("\n\nERROR!!\nMasukan data dengan benar!\n\n\n")
    except FileNotFoundError:
        print("\n\nERROR!!\nFile yang dicari tidak ada!\n\nTulis nama file dengan benar!\n\n")
    except NameError:
        print("\n\nERROR!!\nDeklarasikan data lebih dulu\n\n")
        