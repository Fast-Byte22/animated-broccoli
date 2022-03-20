print(len('1644842741975'))
print(len('864000000000'))
print(len('634636033446495283'))

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
print(	int(round(time.time() * 1000)))
print(	int(round(time.time() * 1000)))
contents =  urllib.request.urlopen("https://freeserv.dukascopy.com/2.0/?path=api/historicalPrices&key=dae9gsyrj4000000&instrument=74450&timeFrame=10sec&count=5000")
contentsJ = json.loads(contents.read().decode('utf-8'))

print(	int(round(time.time() * 1000)))
print(	int(round(time.time() * 1000)))
print(	int(round(time.time() * 1000)))