#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Wenbo Wang"
# __email__ = "wenbo828@gmail.com
# __version__ = "0.1"

import httplib
import urllib
import json

longUrl = raw_input("\nPlease enter the original URL:\n")

def urlShorten():
    apiHost = "api-ssl.bitly.com"
    apiName = "/v3/shorten"
    Header = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    Param = urllib.urlencode({'access_token': '5a5ce2397a0c314b50a34eb7012c22e7625d2432', 'longUrl': longUrl})
    httpsConnection = httplib.HTTPSConnection(host=apiHost, port=443, timeout=15)
    httpsConnection.request(method='GET', url=apiName, body=Param, headers=Header)
    httpsResponse = httpsConnection.getresponse()
    httpsResponseContent = httpsResponse.read()
    #parsedResult = json.loads(httpsResponseContent)['url']
    httpsConnection.close()
    print "\n"
    print Param
    print "Result:"
    print httpsResponseContent
    #print parsedResult

if __name__ == '__main__':
    urlShorten()


# vim:set nu et ai ts=4 sw=4:
