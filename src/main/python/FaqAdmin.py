from Resource import Resource

class FaqAdmin (Resource):

    def __init__(self, host, username, passwd):
        return super(FaqAdmin, self).__init__(host, "/2011-12-03/ask", username, passwd)
    
    def listQuestions(self):
        return self.jsonRequest('GET', url = "/questions")

    def showQuestion(self, uuid):
        return self.jsonRequest('GET', url = "/questions/%s" % uuid)

    def createQuestion(self, data = {}):
        return self.jsonRequest('POST', url = "/questions", data = data)

    def saveQuestion(self, uuid, data = {}):
        return self.jsonRequest('PUT', url = "/questions/%s" % uuid, data = data)

    def deleteQuestion(self, uuid):
        return self.jsonRequest('DELETE', url = "/questions/%s" % uuid)

    def showAnswer(self, uuid):
        return self.jsonRequest('GET', url = "/questions/%s/answer" % uuid, json_response = False)

    def saveAnswer(self, uuid, data = {}):
        results = self.bodyRequest('PUT', url = "/questions/%s/answer" % uuid, data = data)
        return results.text, results.status_code

    def resetLikes(self, uuid):
        return self.jsonRequest('DELETE', url = "/questions/%s/likes" % uuid)

    def resetDislikes(self, uuid):
        return self.jsonRequest('DELETE', url = "/questions/%s/dislikes" % uuid)

    def resetViews(self, uuid):
        return self.jsonRequest('DELETE', url = "/questions/%s/views" % uuid)

    def addQuestionTopic(self, uuid, topic):
        return self.jsonRequest('POST', url = "/questions/%s/topics" % uuid, data = {'topic' : topic})
