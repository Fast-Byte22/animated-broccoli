import os
import FXdata
import LSTM
import threading as th
import logging
import time

#from matplotlib.pyplot import cla
# import tensorflow as tf
# import pathlib
# import matplotlib.pyplot as plt
# import pandas as pd
# import numpy as np
#np.set_printoptions(precision=4)

# if __name__ == "__main__":
#     format = "%(asctime)s: %(message)s"
#     logging.basicConfig(format=format , filename="Main.log", level=logging.INFO,
#                         datefmt="%H:%M:%S")
#     logging.warn('')
#     logging.info("Main start")

instruments= {
    74450 : 'eur to czk' 
    
}


instrumentsT= []

# for x in instruments.keys():
#     tic = time.perf_counter()
#     Thread = th.Thread(target=FXdata.FX, args=(x,))
#     logging.info(f"Main thread {instruments.get(x)} : before running thread")
#     Thread.start()
#     logging.info(f"Main thread {instruments.get(x)} :  thread running ")
#     Thread.join()
#     instrumentsT.append(Thread)
#     toc = time.perf_counter()
#     logging.error(f"Main thread {instruments.get(x)} : all done in time { toc - tic}")
# input()
# for x in instrumentsT:
#     x.kill()



