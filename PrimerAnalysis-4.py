# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 15:52:24 2020
This script continus the analysis of Primerefficiency distribution.
@author: jason
"""
import pandas as PD
import numpy as np
import matplotlib.pyplot as plot
from matplotlib.pyplot import figure


PATH='E:/Geraghty/results/UWCOVID-CVF/UWCOVID-PL1-2'
PATH_1='E:/Geraghty/results/UWCOVID-CVF'
#print(PATH)


    
   
    
def FigPlot(sortAxes, sortRead,Name):
    figure(num=None, figsize=(100,90), dpi=80, facecolor='w', edgecolor='r')
    x_pos=np.arange(len(sortAxes))
    #y_pos=np.arange(max(sortRead))
    plot.bar(x_pos, sortRead, width=0.5)
    plot.title(Name, fontsize=80)
    plot.xlabel('PrimerName',fontsize=60)
    plot.ylabel('PrimerVal', fontsize=60)
    plot.xticks(x_pos, sortAxes, rotation=60, fontsize=40)
    plot.yticks (fontsize=40)

  
    PATH='E:/Geraghty/results/UWCOVID-CVF/UWCOVID-PL1-2_PrimerDistribution/PrimerDistributionplot'
    plot.savefig(PATH+'//'+Name)
    plot.clf()
    plot.show()

RawDistriData_DF=PD.read_csv(PATH_1+'//'+'UWCOVID-PL1-2_PrimerDistribution/Primer-Distribution.csv')

RawPrimerList_DF=PD.read_csv(PATH_1+'//'+'20200601-CV-full.csv', sep=',')
count=0
Primer_List=[]

while count <= 46:
    WorkPrimer=RawPrimerList_DF.iloc[count]
    count=count+1
    A1_Primer=WorkPrimer[0]
    A2_Primer=WorkPrimer[4]
    Primer_List.append(A1_Primer)
    Primer_List.append(A2_Primer)

for primer in Primer_List:
     SampleName=RawDistriData_DF['Sample']
     Primerefficiency=RawDistriData_DF[primer]
     FigPlot(SampleName, Primerefficiency, primer)

     
for primer in Primer_List:
    SampleName=RawDistriData_DF['Sample']
    PrimerEff=RawDistriData_DF[primer]
    primer=primer+'-sorted'
    Eff_Dict={}
    i=0
    while i<=94:
        SP_Dict={SampleName[i]:PrimerEff[i]}
        Eff_Dict.update(SP_Dict)
        i=i+1
    Eff_DictSort=sorted(Eff_Dict.items(),key=lambda x:x[1],reverse=True)
    sampleList=[]
    Eff_List=[]
    for items in Eff_DictSort:
        sample=items[0]
        Eff=items[1]
        
        sampleList.append(sample)
        Eff_List.append(Eff)
    FigPlot(sampleList, Eff_List, primer)
