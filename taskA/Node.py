#!/usr/bin/python2.5

# CPE 701: Internet Protocol Design, Spring 2010
# Project - Emulation of a Reliable Transport Protocol
#
# Authors: Jeffrey Naruchitparames
# University of Nevada, Reno
# Department of Computer Science and Engineering
#
# File: Node.py (from Task A: Emulated network topology)


import errno      # For errors!
import os         # OS-related functions.
import Queue      # This is BIG for threads: mostly for locking semantics.
import re         # Regular expressions.
import shutil     # High-level file operations.
import socket     # Low-level networking interface.
import sys        # Basic system functionality.
import threading  # Higher-level threading interface.


def ConfigInitialNetworkTopology (itc_script):
  return node


class Node(object):
  """
  This class defines our node structures, which are end-systems, within the network.
  The class members are as follow:
  
    [1] _nid = integer
      This is a unique number starting with 1.
      
    [2] _host_name = string
      This is the name of the machine. For example, u-02.ecc.unr.edu
      
    [3] _udp_port = integer
      This is used for all communications to/from the node.
      
    [4] _links = list of tuples (integer, boolean).
      This contains a list of the links this node is has links for. The flag 
      is necessary to determine the link's status (up or down). Note that this list 
      is not static in that more nodes can link to this node. With this, nodes are 
      implicitly linked together.
      
    [5] _mtu = integer (casted to byte)
      This is a link's maximum transmission unit in bytes. Apparently, each node will 
      have the same MTU for all of its links. When connected to another node, we will 
      have to consider the different MTUs from both ends. In this case, we would take the 
      smallest MTU.
    [6] _shutdown = boolean
      If true, then that means the node is exiting cleanly.
  """
  def __init__ (self, nid=0, host_name=None, udp_port=0, links=None, mtu=0):
    self._nid = nid
    self._host_name = host_name
    self._udp_port = udp_port
    self._links = list(links)    # Deep copy the list.
    self._mtu = mtu
    self._shutdown = 0
    
    
  def GetNID ():
    return self._nid
    
  
  def GetHostName ():
    return self._host_name
  
  
  def GetPort ():
    return self._udp_port
  
  
  def GetLinks ():
    return self._links
  
  
  def GetMTU ():
    return self._mtu
  
  
  def GetShutdownStatus ():
    return self._shutdown
    
    
  def SetNID (nid):
    self._nid = nid
    
  
  def SetHostName (host_name):
    self._host_name = host_name
    
    
  def SetPort (udp_port):
    self._udp_port = udp_port
    
    
  def UpdateAllLinks (links):
    self._links = list(links)    # Deep copy the list.
    
    
  def UpdateLink (individual_link):
    # Dealing with flags up in here.
    pass
  
  
  def AddLink (individual_link):
    pass
    
  
  def RemoveLink (individual_link):
    pass
    
    
  def SetMTU (mtu):
    self._mtu = mtu
  
  
  def SetShutdownStatus (shutdown_status):
    self._shutdown = shutdown_status
