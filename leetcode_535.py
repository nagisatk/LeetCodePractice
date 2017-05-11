#!python
# -*- coding: utf-8 -*-
import random
class Codec:
    def __init__(self):
        self.code = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        self.urls = {}
    
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        shortUrl = ""
        for (k, v) in self.urls.items():
            if v == longUrl:
                return k
        length = len(self.code)
        url_id = len(self.urls) + 1
        while url_id > 0:
            shortUrl += self.code[url_id % length]
            url_id = url_id / length
        while len(shortUrl) < 6:
            shortUrl += self.code[0]
        self.urls[shortUrl] = longUrl
        return shortUrl

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.urls[shortUrl]
if __name__ == '__main__':
    codec = Codec()
    for i in range(0, 5000):
        url = 'http://'
        while len(url) < 20:
            url += chr(random.randint(97, 97 + 26))
        if codec.decode(codec.encode(url)) != url:
            print str(i) + "\t-\t" + url