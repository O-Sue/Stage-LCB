#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 15:21:15 2022

@author: ombeline
"""
import csv
import numpy as np
o=100 
########################################## o -> coupe avant l'itération renseignée ici
la=[]
bi=[]
sect=[o]
a=[]
loop= np.loadtxt("bact525.csv", delimiter=',', skiprows=1)
bio=[]
angll=[] 
t = loop[:,0]   
n = loop[:,1]    
x = loop[:,2]
y = loop[:,3]
sol=[]
t=t[o:]  
n=n[o:]
x=x[o:]        
y=y[o:]    
la=np.where(n==0) 
la=la[0]
disto=[]
t0=t[la]
n0=n[la]
x0=x[la]
y0=y[la]
x0=np.array(x0)
y0=np.array(y0)
n0=np.array(n0)

for i in range(len(t0)-1):
    dist= np.sqrt((abs(x0[i]-x0[i+1]))**2 + (abs(y0[i]-y0[i+1]))**2) 
    dist=dist/2.21  ###CONVERTION en micromètres si 2.21pix=1micrometr    
    disto.append(dist) 
    if disto[i]> 20 :      
            a.append(i+1)
for k in a : 
  b=np.where(t0[k]==t)
  b=list(b)
  b=b[0]
  b=b[0]
  bi.append(b)
  bb=t[b]
  bio.append(bb)
for m in range(len(bio)) : 
  zzz=np.where(t==bio[m])
  zzz=zzz[0]
  zzz=zzz[0]
  sol.append(zzz)
for p in range(len(sol)):
    section=o+sol[p]
    sect.append(section)            
    for l in range(len(sect)-1) :
      mi=sect[l]
      mo=sect[l+1]
      t=t[mi:mo]  
      n=n[mi:mo] 
      x=x[mi:mo]          
      y=y[mi:mo] 
    print(mi, mo)
with open('frames525.csv', 'w') as donnees :   
        
        writer=csv.writer(donnees)
        writer.writerow(["debut 200fr", 'fin 200 fr'])
        for o in range(len(sect)-1) :   
             
                   writer.writerow([sect[o],sect[o+1]])
