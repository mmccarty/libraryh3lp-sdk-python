from ConfigParser import ConfigParser
import requests
import unittest

import sys
sys.path.append('../../src/main/python/')

from Account import Account

class TestAccounts(unittest.TestCase):

    def setUp(self):
        #self.host = "https://test.libraryh3lp.com"
        self.host = "https://dev.libraryh3lp.com"

        config = ConfigParser()
        config.read("test.cfg")
        self.username = config.get("auth", "username")
        self.passwd   = config.get("auth", "password")
        self.account  = Account(self.host, self.username, self.passwd)

    def test_init(self):
        account = Account(self.host, self.username, self.passwd)

    def test_listAccounts(self):
        results, status = self.account.listAccounts()
        self.assertEqual(status, requests.codes.ok)
        self.assertEqual(results[0]['email'], 'support@mycustomercloud.com')
        self.assertEqual(results[0]['signup'], '2010-01-30')

    def test_showAccount(self):
        results, status = self.account.showAccount("3f3eea93-73a4-45b8-a011-52deea0947eb")
        #results, status = self.account.showAccount(1085)
        self.assertEqual(status, requests.codes.ok)
        self.assertEqual(results['email'], 'support@mycustomercloud.com')
        self.assertEqual(results['signup'], '2010-01-30')

if __name__ == "__main__":
    unittest.main()

    
