#!/usr/bin/python

import threading
import time
from subprocess import Popen, PIPE

#plots the data using matplotlib
def make_plot():
	threads = range(0,300,5) #xs for plot (in seconds)

	#debugging prints
	print ("threads: ", threads) #print values for x axis
	print ("runtime: ", runtime) #print values for y axis

	#TO DO: matplot lib command to generate plot:


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

