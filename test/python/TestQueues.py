import requests

import sys
sys.path.append('../../src/main/python/')

from Queues import Queues
from Lh3Test  import Lh3Test

QUEUE_UUID = 'bb13517d-e0d3-438c-a378-b97c70dd322b'

class TestQueues(Lh3Test):

    def setUp(self):
        super(TestQueues, self).setUp()
        self.queues = Queues(self.host, self.username, self.passwd)

    def test_init(self):
        queues = Queues(self.host, self.username, self.passwd)

    def test_listQueues(self):
        results, status = self.queues.listQueues()
        self.assertEqual(status, requests.codes.ok)
        self.assertTrue(len(results) > 0)

    def test_showQueue(self):
        results, status = self.queues.showQueue("a766da18-a5af-48c3-962a-aaa7ab587693")
        self.assertEqual(status, requests.codes.ok)
        self.assertEqual(results['jid'], 'april2@chat.dev.libraryh3lp.com')
        self.assertEqual(results['email'], 'psessoms@gmail.com')

        results, status = self.queues.showQueue("a766da18-a5af-48c3-962a-aaa7ab587693", folder = True)
        self.assertEqual(status, requests.codes.ok)
        self.assertTrue(len(results) > 0)

    def test_100createQueue(self):
        _, status = self.queues.deleteQueue("aad7ba74-7bcf-4749-9488-ed4c02f026c6")
        self.assertEqual(status, requests.codes.ok)
        _, status = self.queues.deleteQueue(QUEUE_UUID)
        self.assertEqual(status, requests.codes.ok)

        data = {'name' : 'unittest_queue&',
                'type' : 'queue',
                'parent-uuid' : '8fcf1c72-d77b-4fa6-bbe2-5b7834022ed6'}

        results, status = self.queues.createQueue(data = data)
        self.assertEqual(status, requests.codes.ok)
        self.assertEqual(results['message'], 'Queue names cannot contain spaces or any of the characters "&\'/:<>@\\.') 
        self.assertEqual(results['success'], 'false')

        data['name'] = 'unittest_queue'
        results, status = self.queues.createQueue(data = data)
        self.assertEqual(status, requests.codes.ok)
        self.assertEqual(results[0]['jid'], data['name'] + '@chat.dev.libraryh3lp.com')

    def test_101saveQueue(self):
        data = {'name' : 'unittest_queue2',
                'password' : 'asdf5!',
                'type'     : 'queue',
                'email'    : 'unittest@test.com',
                'parent-uuid' : '8fcf1c72-d77b-4fa6-bbe2-5b7834022ed6'
                }

        results, status = self.queues.saveQueue(QUEUE_UUID, data = data)

        self.assertEqual(status, requests.codes.ok)
        self.assertEqual(results[0]['email'], data['email'])
        self.assertEqual(results[0]['name'], data['name'])

    def test_102listOperators(self):
        results, status = self.queues.listOperators(QUEUE_UUID)
        self.assertEqual(status, requests.codes.ok)
        self.assertTrue(len(results) == 0)

        results, status = self.queues.listOperators("a766da18-a5af-48c3-962a-aaa7ab587693")
        self.assertEqual(status, requests.codes.ok)
        self.assertTrue(len(results) > 0)
        
    def test_103createOperator(self):
        results, status = self.queues.listOperators("a766da18-a5af-48c3-962a-aaa7ab587693")
        self.assertEqual(status, requests.codes.ok)

        data = {'user-uuid' : results[0]['userUuid']}

        results, status = self.queues.createOperator(QUEUE_UUID, data = data)
        self.assertEqual(status, requests.codes.ok)

    def test_104saveOperator(self):
        results, _      = self.queues.listOperators(QUEUE_UUID)
        results, status = self.queues.saveOperator(QUEUE_UUID,
                                                    results[0]['userUuid'],
                                                    data = {'enabled' : False})
        self.assertEqual(status, requests.codes.ok)
        self.assertFalse(results[0]['enabled'])

    def test_105destroyOperator(self):
        results, _      = self.queues.listOperators(QUEUE_UUID)
        results, status = self.queues.destroyOperator(QUEUE_UUID, results[0]['userUuid'])
        self.assertEqual(status, requests.codes.ok)
        
    def test_110deleteQueue(self):
        results, status = self.queues.deleteQueue(QUEUE_UUID)
        self.assertEqual(status, requests.codes.ok)
        self.assertTrue(results['success'])

        _, status = self.queues.deleteQueue("aad7ba74-7bcf-4749-9488-ed4c02f026c6")
        self.assertEqual(status, requests.codes.ok)

if __name__ == "__main__":
    import unittest
    unittest.main()
