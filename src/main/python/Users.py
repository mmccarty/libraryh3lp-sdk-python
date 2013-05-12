from Resource import Resource

class Users (Resource):

    def __init__(self, host, username, passwd):
        return super(Users, self).__init__(host, "/2011-12-03/users", username, passwd)

    
