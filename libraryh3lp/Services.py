from Resource import Resource

class Services (Resource):

    def __init__(self, host, username, passwd):
        return super(Services, self).__init__(host, "/services", username, passwd)

    def listServiceLevels(self, service_uuid):
        return self.jsonRequest('GET', url = '/%s/levels' % service_uuid)

    def showServiceLevel(self, service_uuid, level):
        return self.jsonRequest('GET', url = '/%s/levels/%s' % (service_uuid, level))

    def createServiceLevel(self, service_uuid, data = {}):
        return self.jsonRequest('POST', url = '/%s/levels' % service_uuid, data = data)

    def saveServiceLevel(self, service_uuid, level, data = {}):
        return self.jsonRequest('PUT', url = '/%s/levels/%s' % (service_uuid, level), data = data)

    def deleteServiceLevel(self, service_uuid, level):
        return self.jsonRequest('DELETE', url = '/%s/levels/%s' % (service_uuid, level))

    def upServiceLevel(self, service_uuid, level):
        return self.jsonRequest('POST', url = '/%s/levels/%s/up' % (service_uuid, level))

    def downServiceLevel(self, service_uuid, level):
        return self.jsonRequest('POST', url = '/%s/levels/%s/down' % (service_uuid, level))
