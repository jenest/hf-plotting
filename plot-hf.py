#!/usr/bin/python

#Author: Jenna Delozier
#
#A small program to get data for plotting number of OpenMP
#threads against mean runtime across all threads. 
#
#

import threading
import time
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from subprocess import Popen, PIPE

#plots the data using matplotlib
def make_plot():
        threads = range(0,300,5) #xs for plot (in seconds)

        #debugging prints
        print ("threads: ", threads) #print values for x axis
        print ("runtime: ", runtime) #print values for y axis

        #generate plot using matplotlob and pandas:
        x1 = pd.Series(threads, name="Threads")
        x2 = pd.Series(runtime, name="Runtime")

        data1 = pd.concat([x1, x2], axis=1)
        g = sns.lmplot("Threads", "Runtime", data1,
                scatter_kws={"marker": ".", "color": "navy", "alpha": 0.4 },
                line_kws={"linewidth": 1, "color": "orange"},
                height=8, aspect=1);
        plt.plot(ls="--", c=".1")
        plt.title('OpenMP Threads vs. Runtime', fontsize=20)

#generate the plot of threads vs runtime
def gather_data():

        make_plot()

        runHF = Popen(['nvprof --cpu-profiling on ./hf water.xyz'], stdout=PIPE) #running my script and recording output
                               #re-directing stdout to record echo-ed
                               #output from the script
        datapointX = runHF.communicate()[0] #subprocess returns a stdout, stderr tuple, not interested in stderr

        getThreads = Popen(['./script.sh'], stdout=PIPE) #running my script and recording output
                               #re-directing stdout to record echo-ed
                               #output from the script
        datapointY = getThreads.communicate()[0] #subprocess returns a stdout, stderr tuple, not interested in stderr

        #debugging print
        print (datapoint)
        runtime.append(float(datapoint))


#MAIN (exec starts here)

#array to record data (y-vals for plot)
runtime = []


