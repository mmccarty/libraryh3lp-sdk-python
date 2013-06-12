from Resource import Resource

class Questions (Resource):

    def __init__(self, host, username, passwd):
        return super(Questions, self).__init__(host, "/ask/questions", username, passwd)

    def showAnswer(self, uuid):
        return self.jsonRequest('GET', url = "/%s/answer" % uuid, json_response = False)

    def saveAnswer(self, uuid, data = ""):
        results = self.bodyRequest('PUT', url = "/%s/answer" % uuid, data = data)
        return results.text, results.status_code

    def resetLikes(self, uuid):
        return self.jsonRequest('DELETE', url = "/%s/likes" % uuid)

    def resetDislikes(self, uuid):
        return self.jsonRequest('DELETE', url = "/%s/dislikes" % uuid)

    def resetViews(self, uuid):
        return self.jsonRequest('DELETE', url = "/%s/views" % uuid)

    def addQuestionTopic(self, uuid, topic):
        return self.jsonRequest('POST', url = "/%s/topics" % uuid, data = {'topic' : topic})
