# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 10:33:16 2022

@author: fariz
"""

print('program pembeda jenis segitiga')
x1=int(input('sisi 1: '))
x2=int(input('sisi 2: '))
x3=int(input('sisi 3: '))

if (x1==x2)and(x2==x3):
    print('jenis segitiga anda adalah : segitiga sama sisi.')
elif (x1==x2)or(x2==x3)or(x1==x3):
    print('jenis segitiga anda adalah : segitiga sama kaki.')
elif (x1+x2<=x3)or(x1+x3<=x2)or(x3+x2<=x1):
    print('tidak mungkin membentuk segitiga')
elif(x1+x2>x3)or(x1+x3>x2)or(x3+x2>x1):
    print('jenis segitiga anda adalah : segitiga sembarang.')
