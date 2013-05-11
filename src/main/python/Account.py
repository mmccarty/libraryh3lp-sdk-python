from Resource import Resource

class Account (Resource):

    def __init__(self, host, username, passwd):
        return super(Account, self).__init__(host, "/2011-12-03/accounts", username, passwd)
    
    def listAccounts(self):
        r = self.get()
        return r.json(), r.status_code

    def showAccount(self, uuid):
        r = self.get(url = "/%s" % uuid)
        return r.json(), r.status_code
