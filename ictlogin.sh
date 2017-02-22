#!/bin/bash
# 计算所登陆校园网脚本

username=""
password=""

pass_salt=$(echo -n '12345678'|md5sum|cut -d ' ' -f1)
pass_salt=${pass_salt:8:16}

formdata="username="$username"&password="$pass_salt"&drop=0&type=1&n=100"

curl -d $formdata -H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"  http://159.226.39.22/cgi-bin/do_login
echo ""
curl -d "uid=" http://159.226.39.22/cgi-bin/keeplive
echo ""
