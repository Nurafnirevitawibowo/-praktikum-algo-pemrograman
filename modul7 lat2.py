# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 20:41:36 2021

@author: Afni
"""
print("membuat program menampilkan output 1st, 2nd, dan 13rd")

f = False 

def st(number) :
    if number % 10 == 1 and not number in[11]:
        print(number,"st")
    else:
        th(number)
def nd(number):
    if number % 10 == 2 and not number in[12]:
        print(number,"nd")
    else:
        th(number)
def rd(number):
    if number % 10 == 3 and not number in[13]:
        print(number,"rd")
    else:
        th(number)
def th(number):
    if(number % 10 >=4) or (number % 10 == 0) or number in [11,12,13]:
        print(number,'th')
    else :
        if number % 10 == 1:
            st(number)
        elif number % 10 == 2:
            nd(number)
        elif number % 10 == 3:
            rd(number)

while (not f):
    print("ketik 0 untuk stop progam ")
    number = int(input("enter your number:"))
    if number == 0:
        print('0 th')
        f = True 
    else :
        th (number)


