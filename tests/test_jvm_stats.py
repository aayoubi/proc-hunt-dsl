from context import *
from process_metrics import *

import unittest
import os

class JVMTestSuite(unittest.TestCase):

    def test_retrieval_of_gct(self):
        output = Fetcher.fetch(GCT).of(27393).on('dell624srv').retrieve().value()
        self.assertIsNotNone(output)

    def test_retrieval_of_ygc(self):
        output = Fetcher.fetch(YGC).of(27393).on('dell624srv').retrieve().value()
        self.assertIsNotNone(output)

    def test_retrieval_of_ou(self):
        output = Fetcher.fetch(OU).of(27393).on('dell624srv').retrieve().value()
        self.assertIsNotNone(output)

if __name__ == '__main__':
    unittest.main()
