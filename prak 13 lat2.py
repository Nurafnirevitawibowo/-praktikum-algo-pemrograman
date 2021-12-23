# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 20:52:19 2021

@author: Afni
"""


# dataset
import pandas as pd

df = pd.read_csv("Negara.csv")
mean = df.groupby(["Benua"]).mean ()
std = df.groupby(["Benua"]).std() 
print (df)

x = open ("negararerata.csv","w") 
x.write ("Berikut ini adalah reratanya\n") 
x.write (str(mean))
x.close() 
print (mean)

a = open("NegaraSTD.csv","w") 
a.write ("Berikut ini adalah STDnya\n") 
a.write (str(std))
a.close () 
print (std)
