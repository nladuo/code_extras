"""
    计算所网络认证登陆脚本
    Author: Kalen Blue
"""
import requests
from bs4 import BeautifulSoup
import json
import hmac
import hashlib
from js_lib import js_lib


username = "liujiaming"
password = "12345678"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
    "Referer": "https://gw.ict.ac.cn/srun_portal_pc.php?ac_id=6"
}


def hmac_md5(key, s):
    return hmac.new(key.encode('utf-8'), s.encode('utf-8'), 'MD5').hexdigest()


session = requests.session()
resp = session.get("https://gw.ict.ac.cn/srun_portal_pc.php?ac_id=6")

# first: get ip
soup = BeautifulSoup(resp.content.decode("utf-8"), "lxml")
user_ip = soup.find("input", {"id": "user_ip"}).attrs["value"]
print("Your IP:", user_ip)

# second: get_challenge
resp = session.get("https://gw.ict.ac.cn/cgi-bin/get_challenge?callback=jQuery23&username={username}&ip={ip}".format(
    username=username, ip=user_ip
), headers=headers)
challenge_res = resp.content.decode("utf-8")
challenge_data = json.loads(challenge_res[9:len(challenge_res)-1])
print(challenge_data)
token = challenge_data["challenge"]

print("token:", token)

# third: login
info = "{SRBX1}" + js_lib.b64_encode(js_lib.x_encode(json.dumps({
    "username": username,
    "password": password,
    "ip": user_ip,
    "acid": "6",
    "enc_ver": "srun_bx1"
}), token))


hmd5 = hmac_md5(token, password)
passwd = "{MD5}" + hmd5
ac_id = '6'
n = '200'
_type = '1'
chksum_str = token+username+token+hmd5+token+ac_id+token+user_ip+token+n+token+_type+token+info

print(chksum_str)
chksum = hashlib.sha1(chksum_str.encode("utf-8")).hexdigest()


print("hmd5:", hmd5)
print("chksum:", chksum)
print("passwd:", passwd)
print("info:", info)


resp = session.get("https://gw.ict.ac.cn/cgi-bin/srun_portal?callback=jQuery23&action=login&username="
                   "{username}&password={passwd}&ac_id=6&ip={ip}&info={info}&"
                   "chksum={chksum}&n=200&type=1".format(
                        username=username,
                        passwd=passwd,
                        ip=user_ip,
                        info=info,
                        chksum=chksum,
                    ), headers=headers)
res = resp.content.decode("utf-8")
data = json.loads(res[9:len(res)-1])
print("Login Result:", data)
