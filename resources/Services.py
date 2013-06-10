from Resource import Resource

class Services (Resource):

    def __init__(self, host, username, passwd):
        return super(Services, self).__init__(host, "/services", username, passwd)

    def listServices(self):
        return self.jsonRequest('GET')

    def showService(self, uuid):
        return self.jsonRequest('GET', url = '/%s' % uuid)

    def createService(self, data = {}):
        return self.jsonRequest('POST', data = data)

    def saveService(self, uuid, data = {}):
        return self.jsonRequest('PUT', url = '/%s' % uuid, data = data)

    def deleteService(self, uuid):
        return self.jsonRequest('DELETE', url = '/%s' % uuid)
