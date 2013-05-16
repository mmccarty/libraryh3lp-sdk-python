import requests

import sys
sys.path.append('../../src/main/python/')

from Chats import Chats
from Lh3Test  import Lh3Test

class TestChats(Lh3Test):

    def setUp(self):
        super(TestChats, self).setUp()
        self.chats = Chats(self.host, self.username, self.passwd)

    def test_init(self):
        chats = Chats(self.host, self.username, self.passwd)

    def test_listDay(self):
        results, status = self.chats.listDay(2013, 4, 15)
        self.assertEqual(status, requests.codes.ok)
        self.assertTrue(len(results) == 2)

        response, status = self.chats.listDay(2013, 4, 15, format = 'csv')
        self.assertEqual(status, requests.codes.ok)
        self.assertTrue('uuid' in response.text)

        results, status = self.chats.listDay(2013, 4, 15, to = "2013/05/01")
        self.assertEqual(status, requests.codes.ok)
        self.assertTrue(len(results) == 25)

    def test_listMonth(self):
        results, status = self.chats.listMonth(2013, 4)
        self.assertEqual(status, requests.codes.ok)
        self.assertEqual(results[0]['count'], 16)

    def test_listYear(self):
        results, status = self.chats.listYear(2013)
        self.assertEqual(status, requests.codes.ok)
        self.assertEqual(results[0]['count'], 2)
        self.assertEqual(results[1]['count'], 4)

    def test_anonymizeChats(self):
        results, status = self.chats.listDay(2013, 4, 17)
        self.assertEqual(status, requests.codes.ok)

        self.chats.anonymizeChats([r['uuid'] for r in results[0:2]])

    def test_deleteChats(self):
        uuids = ['8a997d7b-f88b-4812-a317-ce1639990fab',
                 '4812b2b9-ef20-40a1-8285-6bc6d087c0f4']
        
        results, status = self.chats.deleteChats(uuids)
        self.assertEqual(status, requests.codes.ok)
        self.assertTrue(results['success'])

    def test_deleteTranscripts(self):
        results, status = self.chats.listDay(2013, 4, 18)
        self.assertEqual(status, requests.codes.ok)

        results, status = self.chats.deleteTranscripts([r['uuid'] for r in results])
        self.assertEqual(status, requests.codes.ok)

        results, status = self.chats.listDay(2013, 4, 18)
        self.assertEqual(status, requests.codes.ok)
        self.assertFalse(results[0]['transcript'])

    def xtest_archiveConversations(self):
        results, status = self.chats.listDay(2013, 4, 19)
        self.assertEqual(status, requests.codes.ok)

        results, status = self.chats.archiveConversations([r['uuid'] for r in results])

        self.assertEqual(status, requests.codes.ok)
        print results
            
if __name__ == '__main__':
    import unittest
    unittest.main()
