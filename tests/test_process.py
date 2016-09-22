from context import *
from process_metrics import *

import unittest
import sys
import os

class ProcessTestSuite(unittest.TestCase):

    def test_retrieval_of_cpu(self):
        output = Fetcher.metric(CPU).of(os.getpid()).on('localhost').retrieve().value()
        self.assertEqual(os.times(), output, "CPU does not match")

    def test_retrieval_of_pmap(self):
        output = Fetcher.metric(PMAP) .of(os.getpid()) .on('localhost') .retrieve() .value()
        self.assertEqual(0, output, "CPU does not match")

    def test_echo_before_retrieve(self):
        self.assertRaises(FetchException, Fetcher.metric(CPU).echo_to, sys.stdout)

    def test_echo_after_retrieve(self):
        # output = Fetcher.metric(PMAP) .of(os.getpid()) .on('localhost') .retrieve() .echo_to(sys.stdout) .value()
        # self.assertEqual(, Fetcher.metric(CPU).echo_to, sys.stdout)
        pass

#     def test_paramiko(self):
#         from paramiko import SSHClient
#         client = SSHClient()
#         client.load_system_host_keys()
#         client.connect("hostname", username="user")
#         stdin, stdout, stderr = client.exec_command('echo "test"')
#         print "stderr: ", stderr.readlines()
#         print "pwd: ", stdout.readlines()


if __name__ == '__main__':
    unittest.main()

