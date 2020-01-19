# Plotting Results for Parallelization of a Hartree-Fock Proxy Application

D I S C L A I M E R: This code is still in development for use in Jenna Delozier's undergraduate senior thesis. It does not run yet. The idea is to run the Hartree-Fock proxy application, read the number of hard-coded OpenMP threads from the source code, and read the mean runtime across all threads from NVProf. Then, several data points will be plotted.

Files listed here:

  hf.cc: A placeholder file that contains the variable used for the x-axis, which we will retrieve with script.sh. This file will eventually be replaced by the actual proxy app.

  script.sh: A shell script that retrieves the value of the variable used for the x-axis.

  plot-hf.py: A small Python program to plot the number of OpenMP threads against mean runtime across all threads.


Running: python3 plot-hf.py
