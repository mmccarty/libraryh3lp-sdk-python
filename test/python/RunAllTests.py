import unittest

from TestAccounts import TestAccounts
from TestChats    import TestChats
from TestQueues   import TestQueues
from TestUsers    import TestUsers

def suite():
    return unittest.TestSuite((unittest.makeSuite(TestAccounts),
                               unittest.makeSuite(TestChats),
                               unittest.makeSuite(TestQueues),
                               unittest.makeSuite(TestUsers)))

if __name__ == "__main__":
    unittest.main()
