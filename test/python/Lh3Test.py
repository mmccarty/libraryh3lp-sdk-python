from ConfigParser import ConfigParser
import unittest

class Lh3Test (unittest.TestCase):

    def setUp(self):

        config = ConfigParser()
        config.read("test.cfg")
        self.host     = config.get("auth", "host")
        self.username = config.get("auth", "username")
        self.passwd   = config.get("auth", "password")
