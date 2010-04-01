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


def Announce (link_from_node, link_to_node, link_change):
  """
  The node only need to tell its neighbors and only when this node's routing table
  changes.
  
  This function is supposed to send an update to all nodes using l2_send from the 
  LinkLayer module. The message it is sending is to notify all nodes that a link 
  has gone up or down. We need to know that so we can update our routing tables, 
  Node structures, and compute a new Shortest Path to converge our network.
  """
  pass
  
  
def ComputeShortestPath (source_NID, destination_NID, via_NID=0):
  """
  Find the shortest path from source_NID to destination_NID based on link_table. 
  Returns a tuple of (via node, cost).
  """

  if destination_NID == source_NID:
    return destination_NID, 10
  elif ComputeShortestPath(self._link_table[source_NID][0], destination_NID, self._link_table[source_NID][0]) >= ComputeShortestPath(link_table[source_NID][1], destination_NID, self._link_table[source_NID][1]):
    return (ComputeShortestPath(self._link_table[source_NID][1], destination_NID, self._link_table[source_NID][1]), 
            ComputeShortestPath(self._link_table[source_NID][1], destination_NID, self._link_table[source_NID][1]))
  else:
    return (ComputeShortestPath(self._link_table[source_NID][0], destination_NID, self._link_table[source_NID][0]), 
            ComputeShortestPath(self._link_table[source_NID][0], destination_NID, self._link_table[source_NID][1] + 1))          
  
  
def Converge (link_from_node, link_to_node, link_change=0):
  """
  link_change = 0: the link from link_from_node to link_to_node went down
                1: the line is back up
  NOTE: Parameters are not yet defined.
  
  This function will be used in conjunction with the ComputerShortestPath() function.
  """
  if link_change == 0:
    if link_to_node not in link_table[link_from_node]: # No change in the link table
      return
    else:
      if link_table[link_from_node][0] == link_to_node:
        link_table[link_from_node][0] = 0
      elif link_table[link_from_node][1] == link_to_node:
        link_table[link_from_node][1] = 0
      routing_table = BuildRoutingTable(link_table)
      Annouce(link_from_node, link_to_node, link_change)
  elif link_change == 1:
    if link_to_node in link_table[link_from_node]: # No change in the link table
      return
    else:
      if link_table[link_from_node][0] == 0:
        link_table[link_from_node][0] = link_to_node
      elif link_table[link_from_node][1] == 0:
        link_table[link_from_node][1] = link_to_node
      routing_table = BuildRoutingTable(link_table)
      Annouce(link_from_node, link_to_node, link_change)


# Distance Vector Routing Protocol
class DVRP (object):
  """
  This class will maintain the a routing table for each node. That is, every instance 
  of our application will have ONE and only ONE routing table. The members are as follow:
  
    [0] _link_table = dictionary
      key: the node NID
      value: a tutple (of 2?) -- NID of the (2) neighbors. 
      It should be more effient to add _link_table to the Node class.
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
  # Might need to add Node() class as a parameter here.
  def __init__ (self, routing_table=None, shortest_path=None):
    # An example routing table would be: {1:10, 2:5, 3:8}. This means that 
    # THIS node is connected to nodes 1, 2, and 3 with link costs of 10, 5, and 8
    # respectively.
    if not self._link_table:
      self._link_table = SetLinkTable()
        
    self._routing_table = {}
    BuildRoutingTable(self._link_table)
    # self._shortest_path = shortest_path


  def SetLinkTable(self):
    # We should define link_table inside node. So we can init it in node __init__. 
    # Then we just call node.link_table here.
    link_table = {}
    itc_script = open('rtc.txt')
  
    list = itc_script.readlines()
    for entry in list:
      temp = entry.split(' ')
      link_table[temp[0]] = (temp[3],temp[4])
    return link_table


  # Might need to add Node() class as a parameter here.
  def BuildRoutingTable(link_table):
    # routing_table = {}
    for key in self._link_table.keys():
      self._routing_table[node.GetNID()] = ComputeShortestPath(node.GetNID(), key)
    # return routing_table
  

  def GetRoutingTable (self):
    return self._routing_table
  
  
  def GetLinkTable (self):
    return self._link_table

  
  def GetShortestPath (self):
    return self._shortest_path
