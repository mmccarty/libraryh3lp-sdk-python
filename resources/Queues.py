from Resource import Resource

class Queues (Resource):

    def __init__(self, host, username, passwd):
        return super(Queues, self).__init__(host, "/2011-12-03/queues", username, passwd)

    def listQueues(self):
        return self.jsonRequest('GET')

    def showQueue(self, uuid, folder = False):
        return self.jsonRequest('GET',
                                url = "/%s" % uuid,
                                data = {'type' : 'folder'} if folder else {})

    def createQueue(self, data = {}):
        return self.jsonRequest('POST', data = data)

    def saveQueue(self, uuid, data = {}):
        return self.jsonRequest('PUT', url = "/%s" % uuid, data = data)

    def deleteQueue(self, uuid, folder = False):
        return self.jsonRequest('DELETE',
                                url = "/%s" % uuid,
                                data = {'type' : 'folder'} if folder else {})

    def listOperators(self, uuid):
        return self.jsonRequest('GET', url ="/%s/operators" % uuid)

    def createOperator(self, uuid, data):
        return self.jsonRequest('POST', url = "/%s/operators" % uuid, data = data)

    def saveOperator(self, uuid, userUuid, data):
        return self.jsonRequest('PUT', url = "/%s/operators/%s" % (uuid, userUuid), data = data)

    def destroyOperator(self, uuid, userUuid):
        return self.jsonRequest('DELETE', url = "/%s/operators/%s" % (uuid, userUuid))
        
