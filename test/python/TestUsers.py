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
        self.assertEqual(results['type'], 'user')
        self.assertEqual(results['name'], 'pamtest')
        self.assertEqual(results['email'], 'psessoms@gmail.com')

    def test_createUser(self):
        data = {'name' : 'unittest&',
                  'password' : 'asdf5!',
                  'type'     : 'user',
                  'email'    : 'unittest@test.com',
                  'parent-uuid' : '8fcf1c72-d77b-4fa6-bbe2-5b7834022ed6'
                }

        results, status = self.users.createUser(data = data)
        self.assertEqual(status, requests.codes.ok)
        self.assertEqual(results['message'], 'User names cannot contain spaces or any of the characters "&\'/:<>@\\.') 
        self.assertEqual(results['success'], 'false')
        
        data = {'name' : 'unittest',
                  'password' : 'asdf5!',
                  'type'     : 'user',
                  'parent-uuid' : '8fcf1c72-d77b-4fa6-bbe2-5b7834022ed6'
                }
        results, status = self.users.createUser(data = data)

        self.assertEqual(status, requests.codes.ok)
        self.assertEqual(results[0]['name'], data['name'])
        self.assertEqual(results[0]['type'], data['type'])

    def test_deleteUser(self):
        results, status = self.users.deleteUser("deccfef7-0cdc-4ed1-a827-b3dbd4cc3d88")
        self.assertEqual(status, requests.codes.ok)
        self.assertTrue(results['success'])
        
        
if __name__ == "__main__":
    import unittest
    unittest.main()