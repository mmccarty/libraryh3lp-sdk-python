from Resource import Resource

class Users (Resource):

    def __init__(self, host, username, passwd):
        return super(Users, self).__init__(host, "/2011-12-03/users", username, passwd)

    def listUsers(self):
        r = self.get()
        return r.json(), r.status_code

    def showUser(self, uuid, folder = False):
        r = self.get(url = "/%s" % uuid, data = {'type' : 'folder'}) if folder \
            else self.get(url = "/%s" % uuid)
        return r.json(), r.status_code

    def createUser(self, data):
        r = self.post(data = data)
        return r.json(), r.status_code

    def saveUser(self, uuid, data):
        r = self.put(url = "/%s" % uuid, data = data)
        return r.json(), r.status_code

    def deleteUser(self, uuid):
        r = self.delete(url = "/%s" % uuid)
        return r.json(), r.status_code

    def listAssignments(self, uuid):
        r = self.get(url = "/%s/assignments" % uuid)
        return r.json(), r.status_code

    def createAssignment(self, uuid, data):
        r = self.post(url = "/%s/assignments" % uuid, data = data)
        return r.json(), r.status_code

    def saveAssignment(self, uuid, queueUuid, data):
        r = self.put(url = "/%s/assignments/%s" % (uuid, queueUuid), data = data)
        return r.json(), r.status_code

    def destroyAssignment(self, uuid, queueUuid):
        r = self.delete(url = "/%s/assignments/%s" % (uuid, queueUuid))
        return r.json(), r.status_code
        
