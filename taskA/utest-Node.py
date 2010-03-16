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
import os         # OS-related functions.
import shutil     # High-level file operations.
import sys        # Basic system functionality.
import unittest   # For testing, yay!'

import Node


class TestNodeFunctions (unittest.TestCase):
  def TestUpdateAllLinks (self):
    pass
    
  
  def TestUpdateLink (self):
    pass
    
    
  def TestAddLink (self):
    pass
    
    
  def TestRemoveLink (self):
    pass
    

if __name__ == '__main__':
  suite = unittest.TestLoader().loadTestsFromTestCase(TestNodeFunctions)
  unittest.TextTestRunner(verbosity=2).run(suite)
  