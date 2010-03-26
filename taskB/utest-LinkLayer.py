#!/usr/bin/python2.5

# CPE 701: Internet Protocol Design, Spring 2010
# Project - Emulation of a Reliable Transport Protocol
#
# Authors: Jeffrey Naruchitparames
# University of Nevada, Reno
# Department of Computer Science and Engineering
#
# File: utest-LinkLayer.py (from Task B: Emulation of point-to-point links)


import errno      # For errors!
import sys        # Basic system functionality.
import unittest   # For testing, yay!'

sys.path.append('../taskA')
import Node
import LinkLayer


class TestNodeFunctions (unittest.TestCase):
  def test_InitializeSocket (self):
    node = Node.Node(1, 'localhost', 5555)
    print(node)
    client_address, client_socket = LinkLayer.InitializeSocket(node)
    print(client_socket)
    client_socket.close()
  pass
    

if __name__ == '__main__':
  suite = unittest.TestLoader().loadTestsFromTestCase(TestNodeFunctions)
  unittest.TextTestRunner(verbosity=2).run(suite)
  