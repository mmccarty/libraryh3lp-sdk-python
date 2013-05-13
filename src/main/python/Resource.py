import requests
import json

TIMEOUT = 60

class Resource (object):

    def __init__(self, host, baseurl, username, passwd):
        self.host = host
        self.baseurl    = baseurl
        self.ssl_verify = False
        self.session    = requests.Session()
        self.session.post(host + "/2011-12-03/auth/login",
                          params = {'username' : username, 'password' : passwd},
                          verify = self.ssl_verify)

    def get(self, url = "", params = {}):
        uri = self.host + self.baseurl + url
        return self.session.get(uri,
                                params = params,
                                timeout = TIMEOUT,
                                verify = self.ssl_verify)

    def post(self, url = "", data = {}):
        return self.session.post(self.host + self.baseurl + url,
                                 data    = json.dumps(data),
                                 headers = {'content-type' : 'application/json'},
                                 timeout = TIMEOUT,
                                 verify = self.ssl_verify)

    def put(self, url = "", data = {}):
        return self.session.put(self.host + self.baseurl + url,
                                data = data,
                                headers = {'content-type' : 'application/json'},
                                timeout = TIMEOUT,
                                verify = self.ssl_verify)

    def delete(self, url = ""):
        return self.session.delete(self.host + self.baseurl + url,
                                   timeout = TIMEOUT,
                                   verify = self.ssl_verify)
