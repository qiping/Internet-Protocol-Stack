#!/usr/bin/python2.5

# CPE 701: Internet Protocol Design, Spring 2010
# Project - Emulation of a Reliable Transport Protocol
#
# Authors: Jeffrey Naruchitparames, Qiping Yan
# University of Nevada, Reno
# Department of Computer Science and Engineering
#
# File: NetworkLayer.py (from Task C: The network layer)


import errno      # For errors!
import sys        # Basic system functionality.
import unittest   # For testing, yay!'

sys.path.append('../taskA')
sys.path.append('../taskB')
sys.path.append('../taskD')

import Node
import LinkLayer
import RoutingProtocol
import NetworkLayer


class TestNodeFunctions (unittest.TestCase):
  pass
    

if __name__ == '__main__':
  suite = unittest.TestLoader().loadTestsFromTestCase(TestNodeFunctions)
  unittest.TextTestRunner(verbosity=2).run(suite)
  