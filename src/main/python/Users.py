from Resource import Resource

class Users (Resource):

    def __init__(self, host, username, passwd):
        return super(Users, self).__init__(host, "/users", username, passwd)

    def listUsers(self):
        return self.jsonRequest('GET')

    def showUser(self, uuid, folder = False):
        return self.jsonRequest('GET',
                                url = "/%s" % uuid,
                                data = {'type': 'folder'} if folder else {})

    def createUser(self, data):
        return self.jsonRequest('POST', data = data)

    def saveUser(self, uuid, data):
        return self.jsonRequest('PUT', url = "/%s" % uuid, data = data)

    def deleteUser(self, uuid):
        return self.jsonRequest('DELETE', url = "/%s" % uuid)

    def listAssignments(self, uuid):
        return self.jsonRequest('GET', url ="/%s/assignments" % uuid)

    def createAssignment(self, uuid, data):
        return self.jsonRequest('POST', url = "/%s/assignments" % uuid, data = data)

    def saveAssignment(self, uuid, queueUuid, data):
        return self.jsonRequest('PUT', url = "/%s/assignments/%s" % (uuid, queueUuid), data = data)

    def destroyAssignment(self, uuid, queueUuid):
        return self.jsonRequest('DELETE', url = "/%s/assignments/%s" % (uuid, queueUuid))
        
