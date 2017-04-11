#!/usr/bin/env python
#coding=utf8
""" 查看计算所网络使用情况 """
import requests
import math

def format_time(sec):
    sec = int(sec)
    h = math.floor(sec / 3600);
    m = math.floor((sec % 3600) / 60)
    s = sec % 3600 % 60
    out = ""
    if h > 0:
        out += "%d小时" % h
    if h > 0 or m>0:
        out += "%d分" %m
    out += "%d秒" % s;
    return out;

def format_flux(byte):
    byte = int(byte)
    if byte > (1024*1024):
        return "%dM" % format_number((byte / (1000*1000)), 2)

    if byte>1000:
        return "%dK" % format_number((byte / 1000), 2) ;

    return "%dB" % byte


def format_number(num, count):
    n = math.pow(10, count);
    t = math.floor(num*n);
    return t / n

resp = requests.post("http://159.226.39.22/cgi-bin/keeplive", data={"url": ""})
arr = resp.content.split(",")

print "使用时间:", format_time(arr[0]), "入流量:",format_flux(arr[1]),  "出流量:", format_flux(arr[2])
print "当前在线用户:", arr[7]


