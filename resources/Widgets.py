from Resource import Resource

class Widgets (Resource):

    def __init__(self, host, username, passwd):
        return super(Widgets, self).__init__(host, "/widgets", username, passwd)

    def listWidgets(self):
        return self.jsonRequest('GET')

    def showWidget(self, uuid):
        return self.jsonRequest('GET', url = '/%s' % uuid)

    def createWidget(self, data = {}):
        return self.jsonRequest('POST', data = data)

    def saveWidget(self, uuid, data = {}):
        return self.jsonRequest('PUT', url = '/%s' % uuid, data = data)

    def deleteWidget(self, uuid):
        return self.jsonRequest('DELETE', url = '/%s' % uuid)
