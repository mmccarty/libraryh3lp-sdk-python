from Resource import Resource

class Accounts (Resource):

    def __init__(self, host, username, passwd):
        return super(Accounts, self).__init__(host, "/accounts", username, passwd)
