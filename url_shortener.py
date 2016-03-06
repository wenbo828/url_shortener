#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Wenbo Wang"
# __email__ = "wenbo828@gmail.com
# __version__ = "0.1"

import httplib
import urllib
import json

#originURL = "https://docs.python.org/2.7/library/json.html?highlight=json#module-json"
originURL = raw_input("\nPlease enter the original URL:\n")
originURLEncode = urllib.quote(originURL)
params = urllib.urlencode({'format': 'json', 'url': originURL})
headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}

def urlShorten():
    conn = httplib.HTTPConnection("is.gd", port=80, timeout=30)
    conn.request("POST", "/create.php", params, headers)
    data = conn.getresponse()
    response = data.read()
    result = json.loads(response)["shorturl"]
    print response
    print originURLEncode
    print "Result:\n%s" % result

if __name__ == '__main__':
    urlShorten()


# vim:set nu et ai ts=4 sw=4:
