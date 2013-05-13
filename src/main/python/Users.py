from Resource import Resource

class Users (Resource):

    def __init__(self, host, username, passwd):
        return super(Users, self).__init__(host, "/2011-12-03/users", username, passwd)

    def listUsers(self):
        r = self.get()
        return r.json(), r.status_code

    def showUser(self, uuid):
        r = self.get(url = "/%s" % uuid)
        return r.json(), r.status_code
