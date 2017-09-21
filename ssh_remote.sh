#!/bin/bash
nohup ssh -gR 22222:localhost:22 root@hostname "vmstat 30" &
