from Resource import Resource

class Calls (Resource):

    def __init__(self, host, username, passwd):
        return super(Calls, self).__init__(host, "/queues", username, passwd)

    def emailTranscript(self, queue_name, guest_jid, chat_id, email):
        return self.jsonRequest('POST', url = "%s/calls/%s/%s/mail" % (queue_name, guest_jid, chat_id),
                                data = {'email' : email})

    def sendFile(self, queue_name, guest_jid, chat_id, filepath):
        return self.bodyRequest('POST', url = "%s/calls/%s/%s/file" % (queue_name, guest_jid, chat_id),
                                data = open(filepath, 'r'))

    def listTransferTargets(self, queue_name, guest_jid, chat_id):
        return self.jsonRequest('GET', url = "%s/calls/%s/%s/transfer" % (queue_name, guest_jid, chat_id))

    def transfer(self, queue_name, guest_jid, chat_id, target):
        return self.jsonRequest('POST', url = "%s/calls/%s/%s/transfer" % (queue_name, guest_jid, chat_id),
                                data = {'target' : target})

    def viewTranscript(self, queue_name, guest_jid, chat_id):
        results = self.httpRequest('GET', url = "%s/calls/%s/%s/transfer" % (queue_name, guest_jid, chat_id))
        return results.text, results.status_code
