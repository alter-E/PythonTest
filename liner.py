# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 21:45:51 2020

@author: 17382
"""

import numpy as np
import matplotlib.pyplot as plt

def load(filename):
    xArr = []
    yArr = []
    fp=open(filename)
    for i in fp.readlines():
        a = i.strip().split()
        xArr.append(float(a[1]))
        yArr.append(float(a[2]))
    return xArr,yArr

def findAB(x,y):
    x1=np.sum(x)/len(x)
    y1=np.sum(y)/len(y)
    xs=0
    for i in range(0,len(x)) :
        xs+=(x[i]-x1)*(y[i]-y1)
    xx=0
    for i in range(0,len(x)):
        xx+=(x[i]-x1)**2
    a=xs/xx
    b=y1-a*x1
    return a,b

def paint(x,y,a,b):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_title('test')
    ax.set_xlabel('area')
    ax.set_ylabel('price')
    ax.scatter(x,y,marker='.',color='red',s=100)
    yk = []
    for i in x:
        yk.append(float(a*i+b))
    plt.plot(x,yk)
    plt.show()
    
    
if __name__ == '__main__':
    x,y = load('testdata.txt')
    a,b=findAB(x,y)
    paint(x,y,a,b)
    