import requests

import sys
sys.path.append('../../src/main/python/')

from Users import Users
from Lh3Test  import Lh3Test

class TestUsers(Lh3Test):

    def setUp(self):
        super(TestUsers, self).setUp()
        self.users = Users(self.host, self.username, self.passwd)

    def test_init(self):
        users = Users(self.host, self.username, self.passwd)

    def test_listUsers(self):
        results, status = self.users.listUsers()
        self.assertEqual(status, requests.codes.ok)
        self.assertEqual(results[20]['name'], 'pamtest')
        self.assertEqual(results[20]['type'], 'user')
        self.assertEqual(results[20]['email'], 'psessoms@gmail.com')

    def test_showUser(self):
        results, status = self.users.showUser("dd09a03e-d527-4783-b7dd-6fdd8aecef6e")
        self.assertEqual(status, requests.codes.ok)
        self.assertEqual(results[0]['type'], 'folder')
        self.assertEqual(results[24]['name'], 'pamtest')
        self.assertEqual(results[24]['email'], 'psessoms@gmail.com')

if __name__ == "__main__":
    import unittest
    unittest.main()
