# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 23:31:19 2020
This is for continue of primer analysis

@author: jason
"""
import pandas as PD
import numpy as np
import matplotlib.pyplot as plot
from matplotlib.pyplot import figure

PATH='E:/Geraghty/results/UWCOVID-CVF/'
PATH_1='E:/Geraghty/results/UWCOVID-CVF/UWCOVID-PL1-2_PrimerAnalysis'

def primerCount (PrimerList, AMP_List,):
    Count_dict={}
    for primer in AMP_List:
        Count_dict.update({primer:0})
    for primer in PrimerList:
        for item in Count_dict:
            if primer==item:
                val=Count_dict[item]
                val=val+1
                Count_dict.update({item:val})
            else:
                continue
    return Count_dict


def FigData (PrimerCount_Sort):
    primerName=[]
    primercount=[]
    for primer in PrimerCount_Sort:
        primerName.append(primer[0])
        primercount.append(primer[1])
    return primerName, primercount

def BarFig(sortAxes, sortRead,Name):
    figure(num=None, figsize=(100,90), dpi=80, facecolor='w', edgecolor='r')
    x_pos=np.arange(len(sortAxes))
    #y_pos=np.arange(max(sortRead))
    plot.bar(x_pos, sortRead, width=0.5)
    plot.title(Name, fontsize=120)
    plot.xlabel('PrimerName',fontsize=60)
    plot.ylabel('PrimerVal', fontsize=60)
    plot.xticks(x_pos, sortAxes, rotation=60, fontsize=40)
    plot.yticks (fontsize=40)
    PATH='E:/Geraghty/results/UWCOVID-CVF/UWCOVID-PL1-2_PrimerAnalysis'
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
    
HighPrimer_DF=PD.read_csv(PATH_1+'//'+'Primer_High.csv', sep=',')
LowPrimer_DF=PD.read_csv(PATH_1+'//'+'Primer_low.csv')

count=0
HighPrimerList=[]
LowPrimerList=[]
while count <= 282:
    HighPrimer=HighPrimer_DF.iloc[count]
    LowPrimer=LowPrimer_DF.iloc[count]
    count_1=0
    while count_1<10:
        NameHP=HighPrimer[count_1]
        NameLP=LowPrimer[count_1]
        HighPrimerList.append(NameHP)
        LowPrimerList.append(NameLP)
        count_1=count_1+1
    count=count+3
    
#generate blank dictionary
# A1_dict={}
# A2_dict={}
# for primer in A1_List:
#     A1_dict.update({primer:0})
# for primer in A2_List:
#     A2_dict.update({primer:0})    

#Generate count read
High_A1PrimerCount=primerCount(HighPrimerList, A1_List)
High_A2PrimerCount=primerCount(HighPrimerList, A2_List) 
Low_A1PrimerCount=primerCount(LowPrimerList, A1_List)
Low_A2PrimerCount=primerCount(LowPrimerList, A2_List)

#sorting count readings
High_A1PrimerCount_sort=sorted(High_A1PrimerCount.items(), key=lambda x:x[1], reverse=True)
High_A2PrimerCount_sort=sorted(High_A2PrimerCount.items(), key=lambda x:x[1], reverse=True)
Low_A1PrimerCount_sort=sorted(Low_A1PrimerCount.items(), key=lambda x:x[1], reverse=True)
Low_A2PrimerCount_sort=sorted(Low_A2PrimerCount.items(), key=lambda x:x[1], reverse=True)

#plot bar graph
BarFig(FigData(High_A1PrimerCount_sort)[0],FigData(High_A1PrimerCount_sort)[1], 'A1_HighPrimer')
BarFig(FigData(High_A2PrimerCount_sort)[0],FigData(High_A2PrimerCount_sort)[1], 'A2_HighPrimer')
BarFig(FigData(Low_A1PrimerCount_sort)[0],FigData(Low_A1PrimerCount_sort)[1], 'A1_LowPrimer')
BarFig(FigData(Low_A2PrimerCount_sort)[0],FigData(Low_A2PrimerCount_sort)[1], 'A2_LowPrimer')




