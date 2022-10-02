# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 10:33:16 2022

@author: fariz
"""
import math as m
#input
print('program pencari persamaan kuadrat dan determinant')
x1=int(input('nilai a(x²): '))
x2=int(input('nilai b(x): '))
x3=int(input('nilai c: '))

#determinan
if x1==0:
    print('bukan merupakan persamaan kuadrat')
else:
    D = pow(x2, 2)-(4*x1*x3)
    if (D>0):
        d1 = ((-x2)+m.sqrt(D))/(2*x1)
        d2 = ((-x2)-m.sqrt(D))/(2*x1)
        print('persamaan kuadrat:',x1,'x² +',x2,'x +',x3)
        print('determinan: ',D)
        print('memiliki akar x yang berbeda')
        print('akar (x) pertama:',d2)
        print('akar (x) kedua:',d1)
    elif D==0:
        d1 = (x2)/(2*x1)
        d2 = (x2)/(2*x1)
        print('persamaan kuadrat:',x1,'x² +',x2,'x +',x3)
        print('determinan: ',D)
        print('memiliki akar x yang sama/kembar')
        print('akar (x) pertama:',d2)
        print('akar (x) kedua:',d1)
    elif D<0:
        print('persamaan kuadrat:',x1,'x² +',x2,'x +',x3)
        print('determinan: ',D)
        print('merupakan akar imaginer')
        print('akar (x) pertama: ',x2,'+√',D,'/2',x1)
        print('akar (x) pertama: ',x2,'-√',D,'/2',x1)
    else:
        print('tidak bisa di hitung')
        
