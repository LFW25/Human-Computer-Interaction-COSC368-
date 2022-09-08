# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 13:19:52 2022

@author: lfw25
"""

import csv
import time
import math
import numpy as np
import pandas as pd
import scipy.stats as stat

TEXTFILE = "FitsLogbook.csv"
SUMMARYFILE = "Summary.csv"
CLICKS_PER_LOCATION = 8


def analyseFits():
    global TEXTFILE
    global SUMMARYFILE
    global CLICKS_PER_LOCATION
    
    fitsData = np.ndarray.tolist(pd.DataFrame.to_numpy(pd.read_csv(TEXTFILE, delimiter = ',').dropna()))

    with open(SUMMARYFILE, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        
        for subList in fitsData:
            A, w, t = subList[1], subList[2], subList[4]/(CLICKS_PER_LOCATION * 1000)
            ID = np.log2(A/w + 1)
            #sumList.append((A, w, round(ID, 2), round(t, 3)))
            writer.writerow([
                A,
                w,
                round(ID, 2),
                round(t, 3)
                ])      


analyseFits()