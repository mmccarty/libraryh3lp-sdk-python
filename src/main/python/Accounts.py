from Resource import Resource

class Accounts (Resource):

    def __init__(self, host, username, passwd):
        return super(Accounts, self).__init__(host, "/accounts", username, passwd)
    
    def listAccounts(self):
        return self.jsonRequest('GET')

    def showAccount(self, uuid):
        return self.jsonRequest('GET', url = "/%s" % uuid)

    def updateAccount(self, uuid, data = {}):
        return self.jsonRequest('PUT', url = "/%s" % uuid, data = data)
