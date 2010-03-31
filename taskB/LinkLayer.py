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

sys.path.append('../taskA')
import Node


def InitializeSocket (node=None):
  ip = node.GetHostName()
  ip = socket.gethostbyname(ip)
  port = node.GetPort()
  
  client_address = (ip, port)
  # Create client's socket. We are using UDP.
  client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
  # Set any socket options pertaining to multicast.
  client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  # Make this a non-blocking socket. If a recv() call doesn't find any data, then 
  # an exception is raised. If send() doesn't immediately have any data to send, 
  # then an exception is also raised.
  client_socket.setblocking(0)
  
  return client_address, client_socket
  

def ResolveNID (nid=None, node=None):
  """
  THIS WILL BE FOR LAYER 3.
  
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
  

# Deal with MTUs, NID -> IP resolution.
def l2_send (hostname=None, frame=None):
  pass
  
  
def l2_sendto (client_socket=None, hostname=None, frame=None):
  # TODO(Jeff): I have no considered MTUs.
  if hostname is not None:
    # Resolve host name by doing host name -> ip address. Then include the port.
    # Unless the destination port was previous explicitly changed, it will use the 
    # default of port # 5556.
    dest_address = (socket.gethostbyname(hostname), frame.GetDestPort())
    # Make sure it is the same as the Frame.
    frame.SetDestIP(dest_address[0])
    # Prepare our string to send over the wire.
    payload = frame.GetPayload()
    payload += '\r\n'
    frame.SetPayload(payload)
    # Now send it over the wire. Don't forget to encode to a byte string.
    client_socket.sendto(frame.GetPayload().encode(), dest_address)
  else:
    print('No host name specified for l2_sendto.')


def l2_sendall (hostname=None, frame=None):
  pass
  
  
def l2_recv (hostname=None):
  pass
  

def l2_recvfrom (client_socket=None, node=None):
  data = ''.encode()
  buffer = ''.encode()
  mtu = node.GetMTU()
  
  # Read a bunch of bytes up to the MTU.
  while len(data) < mtu:
    buffer, external_address = client_socket.recvfrom(mtu-len(data))
    if buffer:
      data += buffer
      
    # This is our protocol. Stop reading when we see \r\n.
    if '\r\n'.encode() in buffer:
      print('\r\n byte in bufer')
      break
  
  # Here, the source is coming from an external address, meaning we are receiving a packet.
  # Notice we are using node.GetSourceIP and node.GetSourcePort. These are relating 
  # to the localhost (our machine), which in this case is the destination address of this 
  # particular frame.
  frame = Frame.Frame(external_address[0], external_address[1], node.GetSourceIP(), 
                      node.GetSourcePort(), len(buffer), buffer)
  return frame, external_address


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
      
  NOTE: Layer 3 will reference NIDs instead of IPs.
  """
  def __init__ (self, source_ip='localhost', source_port=5555, 
                dest_ip='localhost', dest_port=5556, payload=None):
    self._source_ip = source_ip
    self._source_port = source_port
    self._dest_ip = dest_ip
    self._dest_port = dest_port
    if payload is not None:
      self._length = len(payload)
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
  