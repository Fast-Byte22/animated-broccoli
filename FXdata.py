import json
import urllib.request
import logging
import time

# eur/czk 74450

# if __name__ == "__main__":
#     format = "%(asctime)s: %(message)s"
#     logging.basicConfig(format=format, level=logging.INFO,
#                         datefmt="%H:%M:%S")
#     logging.info("FX    : start")

key = 'dae9gsyrj4000000'

        
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

def GetContentByEnd(timeend,instrument,offerside):
    values =[]
    Time =[]
    res =  urllib.request.urlopen(f"https://freeserv.dukascopy.com/2.0/?path=api/historicalPrices&key=dae9gsyrj4000000&instrument={instrument}&timeFrame=10sec&count=5000&offerSide={offerside}&end={timeend}&count=5000")
    content = json.loads(res.read().decode('utf-8'))
    offersideTerm = 0
    
    if 'A' == offerside :
        offersideTerm = 'ask'    
    else:
        offersideTerm = 'bid'

    for x in content['candles']:
        values.append(x.get(f'{offersideTerm}_open'))
        Time.append(x.get('timestamp'))
    return values, Time



