#!/bin/bash
sudo kill -9 `ps aux | grep -v grep | grep /usr/libexec/airportd | awk '{print $2}'`
