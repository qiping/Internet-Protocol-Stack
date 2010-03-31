#!/usr/bin/python2.5

# CPE 701: Internet Protocol Design, Spring 2010
# Project - Emulation of a Reliable Transport Protocol
#
# Authors: Jeffrey Naruchitparames, Qiping Yan
# University of Nevada, Reno
# Department of Computer Science and Engineering
#
# File: RouteLayer.py (from Task D: The routing protocol)
# This is not really a layer of our protocol stack, but rather part of Layer 3, 
# which is the Network layer (task C).


import errno      # For errors!
import socket     # Low-level networking interface.
import sys        # Basic system functionality.
import threading  # Higher-level threading interface.

sys.path.append('../taskA')
sys.path.append('../taskB')

import Node
import LinkLayer


# Distance Vector Routing Protocol
class DVRP (object):
  """
  This class will maintain the a routing table for each node. That is, every instance 
  of our application will have ONE and only ONE routing table. The members are as follow:
  
    [1] _routing_table = <we must define our data structure we want to use here>
    
  """
  def __init__ (self, routing_table=None):
    self._routing_table = routing_table
    
    
  def GetRoutingTable (self):
    return self._routing_table
    
  pass
