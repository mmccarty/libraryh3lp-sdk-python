from Resource import Resource

class Services (Resource):

    def __init__(self, host, username, passwd):
        return super(Services, self).__init__(host, "/services", username, passwd)

    def listServices(self):
        return self.jsonRequest('GET')

    def showService(self, uuid):
        return self.jsonRequest('GET', url = '/%s' % uuid)

    def deleteService(self, uuid):
        return self.jsonRequest('DELETE', url = '/%s' % uuid)