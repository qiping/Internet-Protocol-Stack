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


def Announce ():
  """
  NOTE: Parameters are not yet defined.
  
  This function is supposed to send an update to all nodes using l2_send from the 
  LinkLayer module. The message it is sending is to notify all nodes that a link 
  has gone up or down. We need to know that so we can update our routing tables, 
  Node structures, and compute a new Shortest Path to converge our network.
  """
  pass
  
  
def ComputeShortestPath ():
  """
  NOTE: Parameters are not yet defined.
  """
  
  
def Converge ():
   """
   NOTE: Parameters are not yet defined.
   
   This function will be used in conjunction with the ComputerShortestPath() function.
   """
   

# Distance Vector Routing Protocol
class DVRP (object):
  """
  This class will maintain the a routing table for each node. That is, every instance 
  of our application will have ONE and only ONE routing table. The members are as follow:
  
    [1] _routing_table = dictionary
      This is a dictionary where we have a {key:value} pair of {node:link cost}.
      We build our initial routing table by accessing the Node structure. In that 
      structure, we access Node._links because _links has all the physical links 
      associated with THIS node already. However, we have to DEFINE default 
      LINK COSTS by ourselves to associate with these physical links.
      
    [2] _shortest_path = <we have to define this data structure.
      Pretty much, this variable will have a listing of all the shortest paths from 
      THIS node (locally) to all other nodes. It will be another table maybe.
    
  This Task D is not really a layer in itself. It will be used in Task C (our Layer 3).
  """
  def __init__ (self, routing_table=None, shortest_path=None):
    # An example routing table would be: {1:10, 2:5, 3:8}. This means that 
    # THIS node is connected to nodes 1, 2, and 3 with link costs of 10, 5, and 8
    # respectively.
    self._routing_table = routing_table
    self._shortest_path = shortest_path
    
    
  def GetRoutingTable (self):
    return self._routing_table
    
  
  def GetShortestPath (self):
    return self._shortest_path
