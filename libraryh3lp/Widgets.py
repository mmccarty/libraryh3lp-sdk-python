from Resource import Resource

class Widgets (Resource):

    def __init__(self, host, username, passwd):
        return super(Widgets, self).__init__(host, "/widgets", username, passwd)
