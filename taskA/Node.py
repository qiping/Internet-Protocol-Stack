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
import Queue      # This is BIG for threads: mostly for locking semantics.
import re         # Regular expressions.
import socket     # Low-level networking interface.
import sys        # Basic system functionality.
import threading  # Higher-level threading interface.


def ConfigInitialNetworkTopology (script, nid):
  node = Node(nid)
  itc_script = open(script)
  
  # Read the entire file, store each line as a string into a list.
  list = itc_script.readlines()
  # This 'hostnames' list is a list of hostnames pertaining to the NIDs.
  # Note the 'off-by-one' issue here. We must account for this by doing -1.
  # This list is necessary to attribute NIDs to hostnames in the self._links.
  hostnames = []
  
  # This is necessary to create our association of NIDs -> host names for 
  # every single node. This will be needed for NID -> hostname -> IP resolution.
  for entry in list:
    temp = entry.split(' ')
    hostnames.append(temp[1])

  for entry in list:
    temp = entry.split(' ')
    # Temporarily assuming we only have 2 links.
    node.SetGlobalLinkTable(temp[0], (temp[3], temp[4]))

    if node.GetNID() == int(temp[0]):
      node.SetHostName(temp[1])
      node.SetPort(int(temp[2]))
      # Figure out how many nodes this thing is connected to by subtract 4 from 
      # the length because 4 = nid, host, port, and MTU.
      number_of_nodes = len(temp) - 4
      # Now we set the index: +3, beacuse 0 = nid, 1 = host, 2 = port, 3 = where we are.
      index = 3
      
      # Reminder: range goes from [0... n]
      for i in range(number_of_nodes):
        # i.e., (NID, host name, flag) -> (2, localhost, 1).
        corresponding_hostname = hostnames[int(temp[index+i])-1]
        node.AddLink((int(temp[index+i]), corresponding_hostname, 1))
      
      # Get the last item in the list, strip out the newline character, and BAM!
      node.SetMTU(int(temp[-1].strip()))

  #node.PrintContents()
  itc_script.close()
  
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
      
    [4] _links = list of tuples (integer, string, boolean).
      This contains a list of the links this node is has links for. The flag 
      is necessary to determine the link's status (up or down). Note that this list 
      is not static in that more nodes can link to this node. With this, nodes are 
      implicitly linked together. The string is the hostname.
      
    [5] _mtu = integer (casted to byte)
      This is a link's maximum transmission unit in bytes. Apparently, each node will 
      have the same MTU for all of its links. When connected to another node, we will 
      have to consider the different MTUs from both ends. In this case, we would take the 
      smallest MTU.
    [6] _shutdown = boolean
      If true, then that means the node is exiting cleanly.
      
    [7] _global_link_table = dictionary
      This is a dictionary of {key:value} where we have {source NID: (neighbor NIDs)}.
  """
  def __init__ (self, nid=0, host_name=None, udp_port=0, links=[], mtu=0, global_link_table={}):
    self._nid = nid
    self._host_name = host_name
    self._udp_port = udp_port
    # I like this statement. It sounds SOOO street lol.
    if links is not None:
      self._links = list(links)    # Deep copy the list.
    self._mtu = mtu
    self._shutdown = 0
    self._global_link_table = {}
    
    
  def GetNID (self):
    return self._nid
    
  
  def GetHostName (self):
    return self._host_name
  
  
  def GetPort (self):
    return self._udp_port
  
  
  def GetLinks (self):
    return self._links
  
  
  def GetMTU (self):
    return self._mtu
  
  
  def GetShutdownStatus (self):
    return self._shutdown
    
  
  def GetGlobalLinkTable (self):
    return self._global_link_table
    
    
  def SetNID (self, nid):
    self._nid = nid
    
  
  def SetHostName (self, host_name):
    self._host_name = host_name
    
    
  def SetPort (self, udp_port):
    self._udp_port = udp_port
    
    
  def UpdateAllLinks (self, links):
    self._links = list(links)    # Deep copy the list.
    
    
  def UpdateLinkStatus (self, individual_link):
    # Dealing with flags up in here.
    self._links.remove(individual_link)
    self._links.append((individual_link[0], individual_link[1], abs(individual_link[2]-1)))
  
  
  def AddLink (self, individual_link):
    self._links.append(individual_link)
    
  
  def RemoveLink (self, individual_link):
    self._links.remove(individual_link)
    
    
  def SetMTU (self, mtu):
    self._mtu = mtu
  
  
  def SetShutdownStatus (self, shutdown_status):
    self._shutdown = shutdown_status
    
    
  def SetGlobalLinkTable (self, source_nid, neighbor_nid):
    self._global_link_table[source_nid] = neighbor_nid
    pass
    
  
  def PrintContents(self):
    print(self._nid)
    print(self._host_name)
    print(self._udp_port)
    print(self._links)
    print(self._mtu)
    print(self._shutdown)
