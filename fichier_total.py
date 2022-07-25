#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 12:18:49 2022

@author: ombeline
"""
import math
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv



zoom= np.loadtxt("frames525.csv", delimiter=',', skiprows=1)
plt.figure(figsize = (20, 20))
open("total.csv", 'a') 
donnees = open("total525.csv", 'w') 
writer=csv.writer(donnees)
writer.writerow(["Temps en sec", 'Numero', 'x (pix)', 'y (pix)', 'Distance (micrometre)', 'Vitesse (microm/s)', 'Acceleration (microm/s' +"\u00B2"+")", "Angle(deg)"])
for k in range(len(zoom)-1):
        #l=zoom[k]
        #mi=int(l[0])
        #mo=int(l[1])
        mi=int(zoom[k,0])
        mo=int(zoom[ k, 1])
      

        
        loop= np.loadtxt(str(mi)+"_"+ str(mo) +".csv", delimiter=',', skiprows=1)
        anlg = loop[:, -1]
        acc = loop[:, -2]
        vitt=loop[:, -3]
        dist=loop[:, -4]
        y=loop[:, -5]
        x=loop[:, -6]
        num=loop[:, -7]
        t=loop[:, -8]
        
        for j in range(len(t)-1) : 
            writer=csv.writer(donnees)
            writer.writerow([t[j], num[j], x[j], y[j], dist[j], vitt[j], acc[j], anlg[j]])
