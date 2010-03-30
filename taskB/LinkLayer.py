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
import re         # Regular expressions.
import socket     # Low-level networking interface.
import sys        # Basic system functionality.
import threading  # Higher-level threading interface.


def InitializeSocket (node=None):
  ip = node.GetHostName()
  ip = socket.gethostbyname(ip)
  port = node.GetPort()
  
  client_address = (ip, port)
  # Create client's socket. We are using UDP.
  client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
  # Set any socket options pertaining to multicast.
  client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  
  return client_address, client_socket
  

def l2_send (nid=None, hostname=None, frame=None):
  pass
  
  
def l2_sendto (nid=None, hostname=None, frame=None):
  pass


def l2_sendall (nid=None, hostname=None, frame=None):
  pass
  
  
def l2_recv (nid=None, hostname=None):
  pass
  

def l2_recvfrom (nid=None, hostname=None):
  pass


class Frame (object):
  """
  This class defines our layer 2 unit, the frame. In this class, we include the 
  header and the payload of our frame. The header consists of the following:
  
    [1] _source_ip = string
      This is the 32-bit IP address of the host.
      
    [2] _source_port = integer
    
    [3] _dest_ip = string
      This is the 32-bit IP address of where we are sending our information.
    
    [4] _dest_port = integer
      
    [5] _length = integer
      This is the length of the payload.
      
    [6] _payload = string
      This is the message we are sending.
  """
  def __init__ (self, source_ip='localhost', source_port=5555, 
                dest_ip='localhost', dest_port=5556, length=0, payload=None):
    self._source_ip = source_ip
    self._source_port = source_port
    self._dest_ip = dest_ip
    self._dest_port = dest_port
    self._length = length
    self._payload = payload
    
  
  def GetSourceIP (self):
    return self._source_ip
    
    
  def GetSourcePort (self):
    return self._source_port
    
    
  def GetDestIP (self):
    return self._dest_ip
    
    
  def GetDestPort (self):
    return self._dest_port
    
    
  def GetLength (self):
    return self._length
    
  
  def GetPayload (self):
    return self._payload
    
    
  def SetSourceIP (self, source_ip):
    self._source_ip = source_ip
    
    
  def SetSourcePort (self, source_port):
    self._source_port = source_port
    
    
  def SetDestIP (self, dest_ip):
    self._dest_ip = dest_ip
    
    
  def SetDestPort (self, dest_port):
    self._dest_port = dest_port
    
    
  def SetPayload (self, payload):
    self._payload = payload
    self._length = len(payload)


  def PrintContents (self):
    print(self._source_ip)
    print(self._source_port)
    print(self._dest_ip)
    print(self._dest_port)
    print(self._length)
    print(self._payload)
  