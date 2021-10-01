# -*- coding: utf-8 -*-
""" 
Calculate the great circle distance between two points
on the earth (specified in decimal degrees)

praktikum 2 latihan 2
created on monday,30 sept 21
@author: Nurafni Revita Wibowo
NIm: 065002100013
"""
print("Namaku adalah? Nurafni revita wibowo")
print("Menghitung jarak Antara Dua Titik di permukaan bumi")


from math import *
def haversine(lon1, lat1, lon2, lat2):
    
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)*2 + cos(lat1) * cos(lat2) * sin(dlon/2)*2
    c = 2 * asin(sqrt(a))
    r = 6371 
    return c * r


coordinate1 = [{'lat':  -6.167801462144129, 'lng':  106.79106059612253}]
coordinate2 = [{'lat':  -6.124536040966865, 'lng':  106.8128928531131}]

lat1 = coordinate1 [0]['lat']
lon1 = coordinate1 [0]['lng']
lat2 = coordinate2 [0]['lat']
lon2 = coordinate2 [0]['lng']

a = haversine(lon1, lat1, lon2, lat2)

print("lattitude coordinate first ={} ".format((lat1)))
print("longitude coordinate first ={} ".format((lon1)))
print("lattitude coordinate second ={} ".format((lat2)))
print("longitude coordinate second ={} ".format((lon2)))

print('Distance coordinate is (km)  : ', a, ("km"))