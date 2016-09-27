from context import *
from process_metrics import *
from process_utils import *

import unittest
import sys
import os

class ProcessTestSuite(unittest.TestCase):

    def test_retrieval_of_cpu(self):
        output = Fetcher.fetch(CPU).of(os.getpid()).on('localhost').retrieve().value()
        self.assertRegexpMatches(output, r"[0-9]{2}?:[0-9]{2}:[0-9]{2}")

    def test_retrieval_of_pmap(self):
        output = Fetcher.fetch(PMAP).of(os.getpid()).on('localhost').retrieve().value()
        self.assertIsNotNone(output)

    def test_echo_before_retrieve(self):
        self.assertRaises(FetchException, Fetcher.fetch(CPU).echo_to, sys.stdout)

    def test_retrieval_of_cpu_of_remote_process(self):
        output = Fetcher.fetch(CPU).of(25864).on('dell624srv').retrieve().value()
        self.assertIsNotNone(output)

    def test_retrieval_of_pmap_of_remote_process(self):
        output = Fetcher.fetch(PMAP).of(25864).on('dell624srv').retrieve().value()
        self.assertIsNotNone(output)

    def test_retrieval_of_nonexistant_remote_process(self):
        self.assertRaises(RemoteExecutionException, Fetcher.fetch(CPU).of(150000000).on('dell624srv').retrieve)

    def test_retrieval_of_user_defined_ps_metrics(self):
        output = Fetcher.fetch(USER_DEFINED_PS, "time,rss,vsz").of(25864).on('dell624srv').retrieve().value()
        self.assertIsNotNone(output)


if __name__ == '__main__':
    unittest.main()

