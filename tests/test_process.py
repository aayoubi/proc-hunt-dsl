from context import *
from process_metrics import *
from process_utils import *

import unittest
import sys
import os

class ProcessTestSuite(unittest.TestCase):

    def test_retrieval_of_cpu(self):
        output = Fetcher.metric(CPU).of(os.getpid()).on('localhost').retrieve().value()
        self.assertRegexpMatches(output, r"[0-9]{2}?:[0-9]{2}:[0-9]{2}")

    def test_retrieval_of_pmap(self):
        output = Fetcher.metric(PMAP).of(os.getpid()).on('localhost').retrieve().value()
        self.assertIsNotNone(output)

    def test_echo_before_retrieve(self):
        self.assertRaises(FetchException, Fetcher.metric(CPU).echo_to, sys.stdout)

    def test_retrieval_of_cpu_of_remote_process(self):
        output = Fetcher.metric(CPU).of(25864).on('dell624srv').retrieve().value()
        self.assertIsNotNone(output)

    def test_retrieval_of_pmap_of_remote_process(self):
        output = Fetcher.metric(PMAP).of(25864).on('dell624srv').retrieve().value()
        self.assertIsNotNone(output)

    def test_retrieval_of_nonexistant_remote_process(self):
        self.assertRaises(RemoteExecutionException, Fetcher.metric(CPU).of(150000000).on('dell624srv').retrieve)


if __name__ == '__main__':
    unittest.main()

