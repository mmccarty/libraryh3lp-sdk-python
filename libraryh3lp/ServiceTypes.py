from Resource import Resource

class ServiceTypes (Resource):

    def __init__(self, host, username, passwd):
        return super(ServiceTypes, self).__init__(host, "/service-types", username, passwd)

    def listServiceTypes(self):
        return self.jsonRequest('GET')
