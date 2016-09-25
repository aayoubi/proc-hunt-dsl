from context import *
from process_metrics import *
from process_utils import *

import unittest
import sys
import os

class ProcessTestSuite(unittest.TestCase):

    def test_retrieval_of_cpu(self):
        output = Fetcher.metric(CPU).of(os.getpid()).on('localhost').retrieve().value()
        self.assertRegexpMatches()
        self.assertEqual('00:00:00', output, "CPU does not match, got {} instead of {}".format(output, '00:00:00'))

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

    def test_report(self):
        for pid in [25882, 25868, 25884, 25876, 25873, 25871, \
                    25879, 25870, 25872, 25875, 25867, 25877, 25866, 25883,\
                    25878, 25881, 25874, 25865, 25880, 25869]:
            print Fetcher.metric(CPU).of(pid).on('dell624srv').retrieve().value()
            print Fetcher.metric(PMAP).of(pid).on('dell624srv').retrieve().value()


if __name__ == '__main__':
    unittest.main()

