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
        self.methodHandlers = {'GET':    self.session.get,
                               'POST':   self.session.post,
                               'PUT':    self.session.put,
                               'DELETE': self.session.delete}

    def jsonRequest(self, method, url = "", data = {}):
        response = self.methodHandlers[method](self.host + self.baseurl + url,
                                               data = json.dumps(data),
                                               timeout = TIMEOUT,
                                               headers = {'content-type' : 'application/json'},
                                               verify  = self.ssl_verify)
                                               
        return response.json(), response.status_code
