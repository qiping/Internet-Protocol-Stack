#!/usr/bin/python2.5

# CPE 701: Internet Protocol Design, Spring 2010
# Project - Emulation of a Reliable Transport Protocol
#
# Authors: Jeffrey Naruchitparames
# University of Nevada, Reno
# Department of Computer Science and Engineering
#
# File: LinkLayer.py (from Task B: Emulation of point-to-point links)
# This is our "Layer 2" of our protocol stack. "Layer 1" can be visualized as 
# the UDP communications.


import errno      # For errors!
import Queue      # This is BIG for threads: mostly for locking semantics.
import re         # Regular expressions.
import socket     # Low-level networking interface.
import sys        # Basic system functionality.
import threading  # Higher-level threading interface.


class Frame (object):
  """
  something
  """
  pass
  