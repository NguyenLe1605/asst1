#!/usr/bin/bash

END=16

for i in $(seq 2 $END); do
    echo "----------------Thread $i --------------"
    # view 1
    ./mandelbrot -t $i
    # view 2
    ./mandelbrot -t $i --view 2
done
