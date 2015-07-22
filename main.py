#!/usr/bin/env python

import urllib
import urllib2
import re
import cookielib
from bs4 import BeautifulSoup

def main():
    url = 'http://www.mache.tv/m/twitter_pickup/vote.php'
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookielib.CookieJar()))

    values = {"e_id" : "2016flash", "mode" : "vote_confirm", "p_id" : "14", "tweet_id" : "623637105617448960"}
    print(values)
    data = urllib.urlencode(values)
    print(data)
    req = urllib2.Request(url, data)
    res = opener.open(req)
    print(res.headers)
    soup = BeautifulSoup(res.read(), "html.parser")
    info = soup.a.get('onclick')
    print(info)

    p = re.compile(u"vote_hash=([a-z0-9]+)", re.UNICODE)
    vote_hash = p.search(info).group(1)
    print(vote_hash)

    values2 = {"e_id" : "2016flash", "mode" : "vote_complete", "p_id" : "14", "tweet_id" : "623637105617448960", "vote_hash" : str(vote_hash)}
    print(values2)

    data2 = urllib.urlencode(values2)
    req2 = urllib2.Request(url, data2)
    print(req2.get_data())
    try:
        res2 = opener.open(req2)
        print(res2.read())
        print(res2.headers)
    except HTTPError, e:
        print(e.code)
    except URLError, e:
        print(e.code)


if __name__ == '__main__':
    main()
