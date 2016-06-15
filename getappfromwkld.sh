#!/bin/bash
for d in ./*/;
do
    cd "$d"
    # echo "$d"
    grep "APP 0" mpi-replay-stats > AMG.csv
    grep "APP 1" mpi-replay-stats > MG.csv
    grep "APP 2" mpi-replay-stats > CR.csv
    cd ../
done
