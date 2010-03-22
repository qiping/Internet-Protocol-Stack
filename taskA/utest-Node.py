#!/usr/bin/python2.5

# CPE 701: Internet Protocol Design, Spring 2010
# Project - Emulation of a Reliable Transport Protocol
#
# Authors: Jeffrey Naruchitparames
# University of Nevada, Reno
# Department of Computer Science and Engineering
#
# File: utest-Node.py (from Task A: Emulated network topology)


import errno      # For errors!
import sys        # Basic system functionality.
import unittest   # For testing, yay!'

import Node


class TestNodeFunctions (unittest.TestCase):
  def test_ConfigNetwork (self):
    global node
    node = Node.ConfigInitialNetworkTopology('itc.txt', 1)
    
    
  def test_UpdateAllLinks (self):
    pass
    
  
  def test_UpdateLinkStatus (self):
    node.UpdateLinkStatus((2, 1))
    node.PrintContents()
    
    
  def test_AddLink (self):
    pass
    
    
  def test_RemoveLink (self):
    pass
    

if __name__ == '__main__':
  suite = unittest.TestLoader().loadTestsFromTestCase(TestNodeFunctions)
  unittest.TextTestRunner(verbosity=2).run(suite)
  