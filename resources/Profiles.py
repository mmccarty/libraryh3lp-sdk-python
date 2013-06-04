from Resource import Resource

class Profiles (Resource):

    def __init__(self, host, username, passwd):
        return super(Profiles, self).__init__(host, "/queues", username, passwd)

    def showQueueProfile(self, queue_uuid):
        return self.jsonRequest('GET', url = "/%s/profiles/staff" % queue_uuid, json_response = False)

    def saveQueueProfile(self, queue_uuid, data = ""):
        results = self.bodyRequest('PUT', url = "/%s/profiles/staff" % queue_uuid, data = data)
        return results.text, results.status_code
