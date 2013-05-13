import unittest

from TestAccounts import TestAccounts
from TestUsers    import TestUsers

def suite():
    return unittest.TestSuite((unittest.makeSuite(TestAccounts),
                               unittest.makeSuite(TestUsers)))

if __name__ == "__main__":
    unittest.main()
