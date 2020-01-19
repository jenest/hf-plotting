#!/bin/bash

#shell. but not the sea kind.


#get the number of OpenMP threads used in this run

arr=(egrep -o "numthreads = [0-9]+" hf.cc')


