import time 
import json
import urllib
import numpy as np
import pandas as pd
import tensorflow as tf

import matplotlib.pyplot as plt
from matplotlib.pylab import rcParams
from FXdata import GetContentByEnd#,GetContentByStart
from graph import CreateGraph
rcParams['figure.figsize']=20,10


from datetime import timezone
from tensorflow import keras

def GetContentByStart(timestart,instrument,offerside):
    values =[]
    Time = []
    res =  urllib.request.urlopen(f'https://freeserv.dukascopy.com/2.0/?path=api/historicalPrices&key=dae9gsyrj4000000&instrument={instrument}&timeFrame=10sec&count=5000&offerSide={offerside}&start={timestart}')
    content = json.loads(res.read().decode('utf-8'))
    offersideTerm = 0
    
    if 'A' == offerside :
        offersideTerm = 'ask'    
    else:
        offersideTerm = 'bid'

    for x in content['candles']:
        values.append(x.get(f'{offersideTerm}_open'))
        Time.append(x.get('timestamp'))

    return values,Time





def splitSequence(seq, n_steps = 50):
    
    #Declare X and y as empty list
    X = []
    y = []
    
    for i in range(len(seq)):
        #get the last index
        lastIndex = i + n_steps
        
        #if lastIndex is greater than length of sequence then break
        if lastIndex > len(seq) - 1:
            break
            
        #Create input and output sequence
        seq_X, seq_y = seq[i:lastIndex], seq[lastIndex]
        
        #append seq_X, seq_y in X and y list
        X.append(seq_X)
        y.append(seq_y)
        pass
    #Convert X and y into numpy array
    X = np.array(X)
    y = np.array(y)
    
    return X,y 

def CreatLSTM(X,y,n_steps= 50,n_features = 1):

    X = X.reshape((X.shape[0], X.shape[1], n_features))

    model = tf.keras.Sequential()
    model.add(keras.layers.LSTM(50, activation='relu', input_shape=(n_steps, n_features)))
    model.add(keras.layers.Dense(1))


    model.summary()
    model.compile(optimizer=tf.keras.optimizers.Adam(0.01), loss=tf.keras.losses.MeanSquaredError(), metrics=['accuracy'])
    model.fit(X, y, epochs=1, verbose=1)
    
    return model

#real
predicted_real, predicted_reTime = GetContentByEnd( timeend= int(time.time()*1000)-10000, instrument = 74450 , offerside= 'A')

last = predicted_reTime[0]

#predict
predict_from, predict_frTime = GetContentByEnd( timeend= last, instrument = 74450 , offerside= 'A')

pfX,pfy = splitSequence(predict_from)
last = predict_frTime[0]

#create
createD, createTime =  GetContentByEnd( timeend= last, instrument = 74450 , offerside= 'A')
# createD2,createTime2 =GetContentByEnd( timeend= createTime[0], instrument = 74450 , offerside= 'A')
crX1, cry1 = splitSequence(createD)
# crX2, cry2 = splitSequence(createD2)
crX =  crX1 #crX2 +
cry =  cry1 #cry2 +
crX = crX.reshape((crX.shape[0], crX.shape[1], 1))


LSTMmodel = CreatLSTM(crX,cry)
pred = LSTMmodel.predict(crX,verbose =1)

s1 = []
s2 = pred

for x in predict_from:
    s1.append(x)

for x in predicted_real:
    s1.append(x)

st = np.arange(0, len(s1), 1)
s2t= np.arange(len(predict_from), len(s2)+len(predict_from), 1)
CreateGraph(s1,st,s2,s2t)

print()