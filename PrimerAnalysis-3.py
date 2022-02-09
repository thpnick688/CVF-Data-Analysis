# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 16:37:29 2020
This script is for analysis primer efficiency. 
@author: jason
"""
import pandas as PD
import numpy as np
import matplotlib.pyplot as plot
from matplotlib.pyplot import figure
import csv

PATH='E:/Geraghty/results/UWCOVID-CVF/UWCOVID-PL1-2'
PATH_1='E:/Geraghty/results/UWCOVID-CVF'
#print(PATH)


    
   
    
def FigPlot(sortAxes, sortRead,Name):
    figure(num=None, figsize=(100,90), dpi=80, facecolor='w', edgecolor='r')
    x_pos=np.arange(len(sortAxes))
    #y_pos=np.arange(max(sortRead))
    plot.bar(x_pos, sortRead, width=0.5)
    plot.title(Name)
    plot.xlabel('PrimerName',fontsize=60)
    plot.ylabel('PrimerVal', fontsize=60)
    plot.xticks(x_pos, sortAxes, rotation=60, fontsize=40)
    plot.yticks (fontsize=40)

  
    PATH='E:/Geraghty/results/UWCOVID-CVF/UWCOVID-PL1-2_PrimerDistribution/'
    plot.savefig(PATH+'//'+Name)
    plot.show()

RawData_DF=PD.read_csv(PATH+'//'+'primer-info-RL.csv')
i=0
n=0

with open(PATH_1+'//'+'UWCOVID-PL1-2_PrimerDistribution/Primer-Distrution.csv', 'w',newline='') as result:
    writer=csv.writer(result,delimiter=',')
    Primerinfo=RawData_DF.iloc[0]
    PrimerName=Primerinfo.index.tolist()
    writer.writerow(PrimerName)        
    while i <= 191:
            workSample=RawData_DF.iloc[i]
            SampleName=workSample[0]
            B2=workSample[2]
            COVSCI=workSample[3]
            PrimerInfo=workSample[4:98]
            i=i+1
            DistriList=[]
            TotalRead=0
            if B2 ==1 and COVSCI >0:
                DistriList.append(SampleName)
                DistriList.append(' ')
                DistriList.append(' ')
                DistriList.append(' ')
                for primer in PrimerInfo:
                    TotalRead=TotalRead+primer
                for primer in PrimerInfo:
                    Distribution=primer/TotalRead
                    Distribution=round(Distribution, 3)
                    Distribution=str(Distribution)
                    DistriList.append(Distribution)
                writer.writerow(DistriList)
                
            
            # if B2 == 1 and COVSCI > 0:
            #     FigPlot(PrimerName, DistriList,SampleName)
            # else:
            #     continue
result.close()
