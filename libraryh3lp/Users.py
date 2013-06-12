from Resource import Resource

class Users (Resource):

    def __init__(self, host, username, passwd):
        return super(Users, self).__init__(host, "/users", username, passwd)

    def listAssignments(self, uuid):
        return self.jsonRequest('GET', url ="/%s/assignments" % uuid)

    def createAssignment(self, uuid, data):
        return self.jsonRequest('POST', url = "/%s/assignments" % uuid, data = data)

    def saveAssignment(self, uuid, queueUuid, data):
        return self.jsonRequest('PUT', url = "/%s/assignments/%s" % (uuid, queueUuid), data = data)

    def destroyAssignment(self, uuid, queueUuid):
        return self.jsonRequest('DELETE', url = "/%s/assignments/%s" % (uuid, queueUuid))
