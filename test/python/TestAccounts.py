import requests

import sys
sys.path.append('../../src/main/python/')

from Accounts import Accounts
from Lh3Test  import Lh3Test

class TestAccounts(Lh3Test):

    def setUp(self):
        super(TestAccounts, self).setUp()
        self.accounts = Accounts(self.host, self.username, self.passwd)

    def test_init(self):
        accounts = Accounts(self.host, self.username, self.passwd)

    def test_listAccounts(self):
        results, status = self.accounts.listAccounts()
        self.assertEqual(status, requests.codes.ok)
        self.assertEqual(results[0]['email'], 'support@mycustomercloud.com')
        self.assertEqual(results[0]['signup'], '2010-01-30')

    def test_showAccount(self):
        results, status = self.accounts.showAccount("3f3eea93-73a4-45b8-a011-52deea0947eb")
        self.assertEqual(status, requests.codes.ok)
        self.assertEqual(results['email'], 'support@mycustomercloud.com')
        self.assertEqual(results['signup'], '2010-01-30')

if __name__ == "__main__":
    import unittest
    unittest.main()
