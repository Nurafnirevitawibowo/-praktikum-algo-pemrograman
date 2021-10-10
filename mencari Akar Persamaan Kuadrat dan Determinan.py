# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 07:22:08 2021
praktikum3
mencari Akar Persamaan Kuadrat dan Determinan
@author: Afni
"""

#langkah1 menentukan angka
p= int(input("nilai p adalah: "))
q= int(input("nilai q adalah: "))
r= int(input("nilai p adalah: "))

#memasukan angka ke dalam rumus
import math
S = (q**2)-(4*p*r)

if (S==0):
    print("bukan merupakan persamaan kuadrat")
elif (S==0):
    x1= (-q/(2*p))
    print("persamaan kuadrat", p, "x^2", q,"x +", r)
    print("Determinannya = S")
    print("memiliki akar kembar")
    print("akar", x1)
elif(S>0):
    x1 = (-q+(math.sqrt(S)))(2*p)
    x2 = (-q-(math.sqrt(S)))(2*p)
    print("persamaan kuadrat", p, "x^2", q,"x +", r)
    print("Determinannya = S")
    print("memiliki akar berbeda")
    print("akar x1= ", x1)
    print("akar x2=", x2)
elif (S<0):
    print("persamaan kuadrat", p, "x^2", q,"x +", r)
    print("Determinannya = S")
    print("merupakan akar imajiner")
    print(-q, "+akar", S, "/2*",p)
    print(-q, "-akar", S, "/2*",p)
    
    
    
    
    
    
    
    