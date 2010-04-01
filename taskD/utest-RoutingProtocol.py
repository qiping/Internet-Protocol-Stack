#!/usr/bin/python2.5

# CPE 701: Internet Protocol Design, Spring 2010
# Project - Emulation of a Reliable Transport Protocol
#
# Authors: Jeffrey Naruchitparames, Qiping Yan
# University of Nevada, Reno
# Department of Computer Science and Engineering
#
# File: utest-RoutingProtocol.py (from Task D: The routing protocol)


import errno      # For errors!
import sys        # Basic system functionality.
import unittest   # For testing, yay!'

sys.path.append('../taskA')
sys.path.append('../taskB')

import Node
import LinkLayer
import RoutingProtocol


class TestNodeFunctions (unittest.TestCase):
  def test_DVRP__init__ (self):
    node = Node.ConfigInitialNetworkTopology('itc_test.txt', 1)
    dvrp = RoutingProtocol.DVRP(node)
    

if __name__ == '__main__':
  suite = unittest.TestLoader().loadTestsFromTestCase(TestNodeFunctions)
  unittest.TextTestRunner(verbosity=2).run(suite)
  