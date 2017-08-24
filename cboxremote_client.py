# -*- coding: utf-8 -*-
import json

import socket
import fcntl
import struct
import urllib
import urllib2
import httplib

id='mydevice-id-test2'
name='mydevice-name'
  
def get_ip_address(ifname):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(
            s.fileno(),
            0x8915,  # SIOCGIFADDR
            struct.pack('256s', ifname[:15])
        )[20:24])
    except Exception, e:
        print e
        return ""

if __name__ == "__main__":
    ipeth0 = get_ip_address('eth0')
    ipeth1 = get_ip_address('eth1')

    obj = {'id': id, 'name': name, 'ipeth0': '192.168.8.112', 'ipeth1': '222'}
    encodedjson = json.dumps(obj)
    print(encodedjson)
    #conn = httplib.HTTPConnection('www.baidu.com', timeout=10)
    #conn = httplib.HTTPConnection("http://127.0.0.1", 8888, timeout=10)
    conn = httplib.HTTPConnection("192.168.9.159", 8888, timeout=10)
try:
    headers = {"Content-Type": "application/json", 'Accept': 'text/plain'}
    response = conn.request('POST', '/register/', encodedjson, headers)
    # response = conn.getresponse()
    if response:
        print response.status
        print response.reason
        print response.read()
        print response.getheaders()
    else:
        print("response null")
except Exception, e:
    print e
finally:
    if conn:
        conn.close()
