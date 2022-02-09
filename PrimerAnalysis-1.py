# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 22:50:01 2020
This script is written to anaylsis the COVID-CVF primer results 
especially for those primers with very high efficiency or low efficiency
@author: jason
"""
import pandas as PD
import numpy as np
import os as os
import matplotlib.pyplot as plot
from matplotlib.pyplot import figure
import csv
PATH='E:/Geraghty/results/UWCOVID-CVF/'
PATH_1='E:/Geraghty/results/UWCOVID-CVF/UWCOVID-PL1-2_PrimerAnalysis/'
#print(PATH)
FileNameList=os.listdir(PATH)

    
   
    
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

  
    PATH='E:/Geraghty/results/UWCOVID-CVF/PrimerFig/'
    plot.savefig(PATH+'//'+Name)
    plot.show()
   


RawPrimerList_DF=PD.read_csv(PATH+'//'+'20200601-CV-full.csv', sep=',')
count=0
A1_List=[]
A2_List=[]

while count <= 46:
    WorkPrimer=RawPrimerList_DF.iloc[count]
    count=count+1
    A1_Primer=WorkPrimer[0]
    A2_Primer=WorkPrimer[4]
    A1_List.append(A1_Primer)
    A2_List.append(A2_Primer)

RawData_DF=PD.read_csv((PATH+'//'+'UWCOVID-PL1-2/Primer-info-RL.csv'))
i=0
n=0
Sort_Data={}
with open(PATH_1+'//'+'Primer_Low.csv', 'w',newline='') as result:
     writer=csv.writer(result,delimiter=',')
     while i <= 191:
        workSample=RawData_DF.iloc[i]
        SampleName=workSample[0]
        B2=workSample[2]
        COVSCI=workSample[3]
        PrimerInfo=workSample[4:98]
        i=i+1
        PrimerInfo_sort=sorted(PrimerInfo.items(), key=lambda x:x[1], reverse=False)
       
        PrimerName=[]
        PrimerVal=[]
        count_1=0
        if B2 ==1 and COVSCI >0:
            print(SampleName, file=result)
            for primer in PrimerInfo_sort:
                PrimerName.append(primer[0])
                PrimerVal.append(primer[1])
                count_1=count_1+1
                if count_1 <=9:
                    continue
                else:
                    break
        else:
            continue
        writer.writerow(PrimerName)
        writer.writerow(PrimerVal)
            
   
        if B2 == 1 and COVSCI > 0:
            FigPlot(PrimerName, PrimerVal,SampleName)
        else:
            continue
result.close()


          
        
    
    
    
    
