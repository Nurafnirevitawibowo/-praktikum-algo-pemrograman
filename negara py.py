# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 10:30:45 2021

@author: Afni
"""

import pandas as pd
df =pd.read_csv(r'c:?Users?MY ASUS ?Download?Negara csv')
mean= df.groupby(["benua"]).maen()
std=df.groupby(["benua"]).std()

print(df)
print("\nberikut data mean:\nz" , mean)
print ("\nberikut data standartdeviation: \n", std)