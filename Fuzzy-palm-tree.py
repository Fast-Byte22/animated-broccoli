import os
import time
import threading as th
import json
import urllib.request
from ast import literal_eval

# import tensorflow as tf
# import pathlib

# import matplotlib.pyplot as plt
# import pandas as pd
# import numpy as np

#np.set_printoptions(precision=4)


# eur/czk 74450 

contents =  urllib.request.urlopen("https://freeserv.dukascopy.com/2.0/?path=api/historicalPrices&key=dae9gsyrj4000000&instrument=74450&timeFrame=tick&count=5000")
contentsJ = json.loads(contents.read().decode('utf-8'))
tList = []
DiffList = []
Abid, Aask, tot, Hbid, Lbid, Hask, Lask = 0 , 0 ,0 , 0, contentsJ['ticks'][0].get('bid'), 0,  contentsJ['ticks'][0].get('ask')
for x in contentsJ['ticks']:
    bid = x.get('bid')
    ask = x.get('ask')
    DiffList.append(ask-bid)
    # times = 1/128 
    # time.sleep(times)
    print('bid - ' + str(bid)+ ': ask - ' + str(ask))
    Abid +=  bid
    Aask += ask
    tot += 1
    if Hbid < bid:
        Hbid = bid
    if Lbid > bid:
        Lbid = bid
    if Hask < ask:
        Hask = ask
    if Lask > ask:
        Lask = ask

input('continue')
last100ticks = []
last100smallbid = 0
last100highask = 0
i = 0
u = 0
for x in contentsJ['ticks']:
    
    bid = x.get('bid')
    ask = x.get('ask')

    if i == 0:
        last100smallbid = x.get('bid')
        last100highask = x.get('ask')
    if  10 > i:
        if ask < last100smallbid:
            u = u + 1
            print(ask - last100smallbid)
        if last100highask > ask:
            last100highask = ask
        if last100smallbid < bid:
            last100smallbid = bid
    else:
        i = 0
        last100smallbid = 0
        last100highask = 0
            
    i +=1
        











print('--- avg. bid - '+ str(Abid/tot) + ' -- avg. ask - ' + str( Aask/tot) +' ---' )
input('continue')
print('--- hig. bid - '+ str(Hbid) +     ' -- low bid - '  + str( Lbid) +' ---'     )
input('continue')
print('--- hig. ask - '+ str(Hask) +     ' -- low ask - '  + str( Lask) +' ---'     )
input('continue')
print('--- ticks - ' + str(tot)+ ' ---' )
input('continue')
AvgSumDiff= 0
for x in DiffList:
    AvgSumDiff += x
    print(x)
input('continue')
print(AvgSumDiff/len(DiffList))
input('press enter to exit')