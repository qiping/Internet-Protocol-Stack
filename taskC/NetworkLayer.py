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
import socket     # Low-level networking interface.
import sys        # Basic system functionality.
import threading  # Higher-level threading interface.

sys.path.append('../taskA')
sys.path.append('../taskB')
sys.path.append('../taskD')

import Node
import LinkLayer
import RoutingProtocol


def ResolveNID (nid=None, node=None):
  """
  This function takes in two parameters, a nid and Node respectively. From there, 
  it creates a temporary copy of all the links associated with this node (we are 
  on localhost). After that, we iterate through all the links where each element of 
  this 'links' variable is a tuple consisting of (nid, hostname, flag). The flag 
  determines if the link is up or down. If our nid matches an nid in the 'links' 
  list variable, then we return the host name. This is necessary for resolving the 
  host name so we can use an ip address to send Frames over the wire.
  """
  links = node.GetLinks()
  
  for entry in links:
    if nid == entry[0]:
      return entry[1]


def l3_sendto (client_socket=None, nid=None, datagram=None):
  """
  This function will be used in Layer 4, the Transport layer. Nowhere in this Layer 3
  is this function used--rather, this layer purely uses l2_sendto from 
  the LinkLayer module.
  """
  pass
  

def l3_recvfrom (client_socket=None):
  """
  This function will be used in Layer 4, the Transport layer. Nowhere in this Layer 3
  is this function used--rather, this layer purely uses l2_recvfrom from 
  the LinkLayer module.
  """
  pass


# We are not using inheritance beacuse inheritance does not meet our goals.
# The idea is that, the payload of this class will be the Frame. The string that
# will be passed will be put in the Frame.
class Datagram (object):
  """
  Notes: We need to include the MTU (for fragmentation and reassembly), TTL,
    payload = Frame. The TTL will be decremented after each hop.
  """
  def __init__ (self, mtu=0, ttl=5, payload=None):
    self._mtu = mtu
    self._ttl = ttl
    self._payload = payload
  
  
  def GetMTU (self):
    return self._mtu
    
    
  def GetTTL (self):
    return self._ttl
    
    
  # WE MIGHT NEED TO CHANGE THIS DRASTICALLY.
  # Idea: We get a string -> set headers for this layer -> build Frame. GO.
  def GetPayload (self):
    return self._payload
    
    
  def SetMTU (self, mtu):
    self._mtu = mtu
    
    
  def SetTTL (self, ttl):
    self._ttl = ttl
    
  
  # WE MIGHT NEED TO CHANGE THIS DRASTICALLY.
  def SetPayload (self, payload):
    self._payload = payload
