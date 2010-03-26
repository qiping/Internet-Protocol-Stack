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
  hedaer = MTU, payload, ip source, ip dest, port, length.
  """
  pass
  