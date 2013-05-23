import requests

import sys
sys.path.append('../../src/main/python/')

from FaqAdmin import FaqAdmin
from Lh3Test  import Lh3Test

class TestFaqAdmin(Lh3Test):

    def setUp(self):
        super(TestFaqAdmin, self).setUp()
        self.faq = FaqAdmin(self.host, self.username, self.passwd)

    def xtest_init(self):
        faq = FaqAdmin(self.host, self.username, self.passwd)

    def xtest_listQuestions(self):
        results, status = self.faq.listQuestions()
        self.assertEqual(status, requests.codes.ok)
        self.assertEqual(results['totalCount'], 104)

    def xtest_showQuestion(self):
        results, status = self.faq.showQuestion("713ba6f6-45df-4e99-8415-8856907b2503")
        self.assertEqual(status, requests.codes.ok)
        self.assertEqual(results['question'], 'How many chats can I expect to get?')

    def xtest_saveQuestion(self):
        original, status = self.faq.showQuestion("713ba6f6-45df-4e99-8415-8856907b2503")
        self.assertEqual(status, requests.codes.ok)

        data = {"question" : "Who are you?",
                "answer"   : "I'm batman.",
                "topics"   : "batman,robin,chats"
                }
        results, status = self.faq.saveQuestion("713ba6f6-45df-4e99-8415-8856907b2503", data = data)
        self.assertEqual(status, requests.codes.ok)

        results, status = self.faq.saveQuestion("713ba6f6-45df-4e99-8415-8856907b2503", data = {"question" : original['question'],
                                                                                                "answer" : original['answer']})
        self.assertEqual(status, requests.codes.ok)
        
    def xtest_createDeleteQuestion(self):
        data = {"question" : "What is your favorite Star Wars movie?",
                "answer"   : "The Empire Strikes Back.",
                }
        results, status = self.faq.createQuestion(data = data)
        self.assertEqual(status, requests.codes.ok)
        createdUuid = results[0]['uuid']

        self.assertEqual(results[0]['question'], data['question'])
        self.assertEqual(results[0]['answer'], data['answer'])

        results, status = self.faq.deleteQuestion(createdUuid)
        self.assertEqual(status, requests.codes.ok)
        self.assertTrue(results['success'])

    def xtest_showSaveAnswer(self):
        data = {"question" : "What is your favorite Star Wars movie?",
                "answer"   : "The Empire Strikes Back.",
                }
        results, status = self.faq.createQuestion(data = data)
        self.assertEqual(status, requests.codes.ok)
        createdUuid = results[0]['uuid']

        results, status = self.faq.showAnswer(createdUuid)
        self.assertEqual(status, requests.codes.ok)
        self.assertEqual(results, data['answer'])

        data = "Return of the Jedi"
        results, status = self.faq.saveAnswer(createdUuid, data = data)
        self.assertEqual(status, requests.codes.ok)

        results, status = self.faq.showAnswer(createdUuid)
        self.assertEqual(status, requests.codes.ok)
        self.assertEqual(results, data)

        results, status = self.faq.deleteQuestion(createdUuid)
        self.assertEqual(status, requests.codes.ok)
        self.assertTrue(results['success'])

    def test_showSaveAnswer(self):
        data = {"question" : "What is your favorite Star Wars movie?",
                "answer"   : "The Empire Strikes Back.",
                }
        results, status = self.faq.createQuestion(data = data)
        self.assertEqual(status, requests.codes.ok)
        createdUuid = results[0]['uuid']

        results, status = self.faq.showQuestion(createdUuid)
        self.assertEqual(status, requests.codes.ok)
        print results

        results, status = self.faq.deleteQuestion(createdUuid)
        self.assertEqual(status, requests.codes.ok)
        self.assertTrue(results['success'])

if __name__ == "__main__":
    import unittest
    unittest.main()
