import matplotlib.pyplot as plt
import numpy as np

def CreateGraph(s1,s1t,s2,s2t):
    fig, ax = plt.subplots()

    twin1 = ax.twinx()

    p1, = ax.plot(s1t, s1, "b-", label="base")
    p2, = twin1.plot(s2t, s2, "g-", label="predict")

    #time
    ax.set_xlim(0, s1t[len(s1t)-1] +1)
    #price
    ax.set_ylim(0, s1[len(s1)-1] +1)

    twin1.set_ylim(0, s1[len(s1)-1] +1)

    ax.set_xlabel("time")
    ax.set_ylabel("price")

    ax.yaxis.label.set_color(p1.get_color())

    tkw = dict(size=4, width=1.5)
    ax.tick_params(axis='y', colors=p1.get_color(), **tkw)
    twin1.tick_params(axis='y', colors=p2.get_color(), **tkw)

    ax.tick_params(axis='x', **tkw)

    ax.legend(handles=[p1, p2])

    plt.show()
    


# s = np.arange(0.1, 10.0, 0.1)
# s2= np.arange(5.0, 10.0, 0.15)
# st = np.arange(0, len(s), 1)
# s2t= np.arange(30.0, len(s2)+30, 1)


# CreateGraph(s,st,s2,s2t)