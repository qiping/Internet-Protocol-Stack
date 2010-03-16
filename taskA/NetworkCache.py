#!/usr/bin/python2.5

# CPE 701: Internet Protocol Design, Spring 2010
# Project - Emulation of a Reliable Transport Protocol
#
# Authors: Jeffrey Naruchitparames, Paul Brower, Qiping Yan
# University of Nevada, Reno
# Department of Computer Science and Engineering
#
# File: NetworkCache.py (from Task A: Emulated network topology)


import errno      # For errors!
import os         # OS-related functions.
import Queue      # This is BIG for threads: mostly for locking semantics.
import re         # Regular expressions.
import shutil     # High-level file operations.
import socket     # Low-level networking interface.
import string     # Compliant strings.
import sys        # Basic system functionality.
import threading  # Higher-level threading interface.

import Node       # Our defined node class.


class NetworkCache():
  """
  This class defines all the various caches that will be used within our network 
  topology. This is essential when dealing with speed and scalability of our 
  network. By utilizing caching mechanisms, we can allow our code to search in O(1) 
  time in some instances. The members are listed as follows:
  
    [1] nid_cache = dictionary of recently removed NIDs.
      This is a dictionary of recently removed NIDs and their TTL in the form
      
      key:value -> {integer : integer} where we have {NID : TTL}.
      
      The TTL will determine whether or not to reuse the NID yet (for a new node 
      entering the network). If the TTL is not up, that means the disconnected node 
      still has time left to reconnect to the network and reuse its NID.
      NIDs may be remove for various reasons including: temporary disconnect, 
      complete disconnect, or a network error.
      
    [2] link_cache_ = dictionary of recently removed links.
  """
  def __init__ (self):
    self.nid_cache_ = {}
    self.link_cache_ = {}
    