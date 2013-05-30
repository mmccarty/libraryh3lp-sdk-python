from Resource import Resource

class Gateways (Resource):

    def __init__(self, host, username, passwd):
        return super(Gateways, self).__init__(host, "/queues", username, passwd)

    def listGateways(self, queue_uuid):
        return self.jsonRequest('GET', url = "/%s/gateways" % queue_uuid)

    def createGateway(self, queue_uuid, data = {}):
        return self.jsonRequest('POST', url = "/%s/gateways" % queue_uuid, data = data)

    def deleteGateway(self, queue_uuid, protocol, username):
        return self.jsonRequest('DELETE', url = "/%s/gateways/%s/%s" % (queue_uuid, protocol, username))
