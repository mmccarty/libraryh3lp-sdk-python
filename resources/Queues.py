from Resource import Resource

class Queues (Resource):

    def __init__(self, host, username, passwd):
        return super(Queues, self).__init__(host, "/queues", username, passwd)

    def listOperators(self, uuid):
        return self.jsonRequest('GET', url ="/%s/operators" % uuid)

    def createOperator(self, uuid, data):
        return self.jsonRequest('POST', url = "/%s/operators" % uuid, data = data)

    def saveOperator(self, uuid, userUuid, data):
        return self.jsonRequest('PUT', url = "/%s/operators/%s" % (uuid, userUuid), data = data)

    def destroyOperator(self, uuid, userUuid):
        return self.jsonRequest('DELETE', url = "/%s/operators/%s" % (uuid, userUuid))

    def listGateways(self, queue_uuid):
        return self.jsonRequest('GET', url = "/%s/gateways" % queue_uuid)

    def createGateway(self, queue_uuid, data = {}):
        return self.jsonRequest('POST', url = "/%s/gateways" % queue_uuid, data = data)

    def deleteGateway(self, queue_uuid, protocol, username):
        return self.jsonRequest('DELETE', url = "/%s/gateways/%s/%s" % (queue_uuid, protocol, username))

    def showProfile(self, queue_uuid):
        return self.jsonRequest('GET', url = "/%s/profiles/staff" % queue_uuid, json_response = False)

    def updateProfile(self, queue_uuid, data = ""):
        results = self.bodyRequest('PUT', url = "/%s/profiles/staff" % queue_uuid, data = data)
        return results.text, results.status_code
