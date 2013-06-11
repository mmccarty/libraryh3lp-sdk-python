import requests
import json

VERSION = '/2011-12-03'

class Resource (object):

    def __init__(self, host, baseurl, username, passwd, ssl_verify = False, timeout = 60):
        self.host = host
        self.baseurl    = VERSION + baseurl
        self.ssl_verify = ssl_verify
        self.timeout    = timeout
        self.session    = requests.Session()
        self.session.post(host + VERSION + "/auth/login",
                          params = {'username' : username, 'password' : passwd},
                          verify = self.ssl_verify)
        self.methodHandlers = {'GET':    self.session.get,
                               'POST':   self.session.post,
                               'PUT':    self.session.put,
                               'DELETE': self.session.delete}

    def jsonRequest(self, method, url = "", data = {}, json_response = True):
        response = self.methodHandlers[method](self.host + self.baseurl + url,
                                               data = json.dumps(data),
                                               timeout = self.timeout,
                                               headers = {'content-type' : 'application/json'},
                                               verify  = self.ssl_verify)

        return (response.json() if json_response else response.text, 200) if response.status_code == 200 else \
               (response, response.status_code)

    def bodyRequest(self, method, url = "", data = ""):
        return self.methodHandlers[method](self.host + self.baseurl + url,
                                           data = data,
                                           timeout = self.timeout,
                                           verify  = self.ssl_verify)

    def httpRequest(self, method, url = "", params = {}):
        return self.methodHandlers[method](self.host + self.baseurl + url,
                                           params = params,
                                           timeout = self.timeout,
                                           headers = {'content-type' : 'text/plain'},
                                           verify  = self.ssl_verify)

    def list(self):
        return self.jsonRequest('GET')

    def read(self, uuid, folder = False):
        return self.jsonRequest('GET',
                                url = "/%s" % uuid,
                                data = {'type': 'folder'} if folder else {})

    def create(self, data):
        return self.jsonRequest('POST', data = data)

    def update(self, uuid, data):
        return self.jsonRequest('PUT', url = "/%s" % uuid, data = data)

    def delete(self, uuid):
        return self.jsonRequest('DELETE', url = "/%s" % uuid)
