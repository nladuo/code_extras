#!/bin/bash
# 计算所登陆校园网脚本
# 填写用户名和密码[密码为md5后的字符串的substr(8,16)]
curl -d "username=&password=&drop=0&type=1&n=100" -H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"  http://159.226.39.22/cgi-bin/do_login
echo ""
curl -d "uid=" http://159.226.39.22/cgi-bin/keeplive
echo ""
