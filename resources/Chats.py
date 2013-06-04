from Resource import Resource
from datetime import datetime

class Chats (Resource):

    def __init__(self, host, username, passwd):
        return super(Chats, self).__init__(host, "/conversations", username, passwd)

    def listDay(self, year, month, day, to = None, format = 'json'):
        dt = datetime(year, month, day)
        params = {'format' : format}
        if to:
            params['to'] = to
        response = self.httpRequest('GET', url = "/%s" % dt.strftime('%Y/%m/%d'), params = params)
        return (response.json(), response.status_code) if format == 'json' else (response, response.status_code)

    def listMonth(self, year, month, to = None): 
        dt = datetime(year, month, 1)
        if to:
            params['to'] = to
        response = self.httpRequest('GET', url = "/%s" % dt.strftime('%Y/%m'))
        return response.json(), response.status_code

    def listYear(self, year, to = None): 
        if to:
            params['to'] = to
        response = self.httpRequest('GET', url = "/%s" % year)
        return response.json(), response.status_code

    def anonymizeChats(self, uuids):
        response = self.httpRequest('POST', url = "/anonymize-conversations", params = {'uuids' : ','.join(uuids)})
        return response.json(), response.status_code

    def deleteChats(self, uuids):
        response = self.httpRequest('POST', url = "/delete-conversations", params = {'uuids' : ','.join(uuids)})
        return response.json(), response.status_code

    def deleteTranscripts(self, uuids):
        response = self.httpRequest('POST', url = "/delete-transcripts", params = {'uuids' : ','.join(uuids)})
        return response.json(), response.status_code

    def archiveConversations(self, uuids):
        response = self.httpRequest('GET', url = "/archive", params = {'uuids' : ','.join(uuids)})
        return response.content, response.status_code
