#!/bin/bash
#Description:  计算所网络认证登陆脚本
#Author: Kalen Blue

username=""
password=""

pass_salt=$(echo -n $password | md5sum | cut -d ' ' -f1)
pass_salt=${pass_salt:8:16}

formdata="username="$username"&password="$pass_salt"&drop=0&type=1&n=100"

curl -d $formdata -H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"  http://159.226.39.22/cgi-bin/do_login
echo ""
./infoict.py
