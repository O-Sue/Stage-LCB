#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 15:21:15 2022

@author: ombeline
"""

import csv
import math
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np



loop= np.loadtxt("bact525.csv", delimiter=',', skiprows=1)      # nom fichier, delimiter ';' ou ','
t1 = loop[:,0]   
n1 = loop[:,1]   
x1 = loop[:,2]
y1 = loop[:,3]
zoom= np.loadtxt("frames525.csv", delimiter=',', skiprows=1)

for k in range(len(zoom)-1):
        mi=int(zoom[k,0])
        mo=int(zoom[ k, 1])
        open(str(mi)+"_"+str(mo)+".csv", 'a') 
        t=t1[mi:mo]                                 # SECTION DE 200frames 
        n=n1[mi:mo]
        x=x1[mi:mo] 
        y=y1[mi:mo]

        donnees = open(str(mi)+"_"+str(mo)+".csv", 'w') 
        writer=csv.writer(donnees)
        writer.writerow(["Temps en sec", 'Numero', 'x (pix)', 'y (pix)', 'Distance (micrometre)', 'Vitesse (microm/s)', 'Acceleration (microm/s' +"\u00B2"+")", "Angle(deg)"])
        for p in range(50):
            
            
            la=np.where(n==p) 
            la=la[0]
            angll=[]
            disto=[]
            bae=[]
            vitt=[]
            acc=[] 
            t0=t[la]
            n0=n[la]
            x0=x[la]
            y0=y[la]
            x0=np.array(x0)
            y0=np.array(y0)
            n0=np.array(n0)
            
            for i in range(len(n0)-1) :   
                
                dist= np.sqrt((abs(x0[i]-x0[i+1]))**2 + (abs(y0[i]-y0[i+1]))**2) 
                dist=dist/2.21  ###CONVERTION en micromètres si 2.21pix=1micrometr    
        
                disto.append(dist)
                
                vit=dist/((t0[i+1]-t0[i])/1000)    ## en micromètres par secondes
                vitt.append(vit)
                accc = vit/(t0[i]/1000)
                acc.append(accc)
                troip= np.sqrt((abs(y0[i]-y0[i+1]))**2) 
                troip=troip/2.21  ###CONVERTION en micromètres si 2.21pix=1micrometr    
                bae.append(troip)
                
                if x0[i+1]>x0[i] and y0[i+1]<y0[i] and dist != 0: 
                    angle= math.degrees(math.acos(troip/dist))       #    np.radians(troip/dist)))
               
                elif x0[i+1] < x0[i] and y0[i+1] < y0[i] and dist!=0: 
                
                    angle= 180-math.degrees(math.acos(troip/dist) )  
                    
                elif x0[i+1]< x0[i] and y0[i+1]>y0[i] and dist!=0 : 
                    angle= 180+math.degrees(math.acos(troip/dist) )  
                    
                elif x0[i+1] > x0[i] and y0[i+1] > y0[i] and dist!=0: 
                    angle= 360-math.degrees(math.acos(troip/dist) )  
                    
                elif y0[i+1] == y0[i] and x0[i+1] < x0[i] and dist!=0: 
                    angle= 180  
                elif y0[i+1] == y0[i] and x0[i+1] > x0[i] and dist!=0: 
                    angle= 0
                                        
                elif x0[i+1] == x0[i] and y0[i+1] < y0[i] and dist!=0: 
                    angle= 90
                    
                elif x0[i+1] == x0[i] and y0[i+1] > y0[i] and dist!=0: 
                    angle= 270
                    
                else :
                    angle=np.nan
                
                angll.append(angle)
                angll2= [x for x in angll if np.isnan(x) == False]  
                anglmoy=np.mean(angll2)
            
            with open(str(mi)+"_"+str(mo)+".csv", 'a') as donnees :  
                writer=csv.writer(donnees)
                disto[-1]=np.nan
                vitt[-1]=np.nan
                acc[-1]=np.nan
                angll[-1]=np.nan
                for i in range(len(n0)-1) :  

                        writer.writerow([t0[i]/1000, n0[i], x0[i], y0[i], disto[i], vitt[i], acc[i], angll[i]])
                        

  
                                   
                                    
                               
                                     
                                     
