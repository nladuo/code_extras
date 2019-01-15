#!/bin/bash

pids=$(ps -ef | grep some_process | awk '{print $2}')
for pid in $pids
do
    echo  $pid
    kill -9  $pid
done
