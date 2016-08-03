"""Client to send OSC datagrams to an OSC server via UDP."""

import ipaddress
import socket

class UDPClient(object):
  """OSC client to send OscMessages or OscBundles via UDP."""

  def __init__(self, address, port, ttl_hops=1, interface=None):
    """Initialize the client.

    As this is UDP it will not actually make any attempt to connect to the
    given server at ip:port until the send() method is called.
    """
    self._sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    if (ipaddress.ip_address(address).is_multicast):
      self._sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl_hops)
      if (interface != None):
        self._sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_IF, socket.inet_aton(interface))

    self._sock.setblocking(0)
    self._address = address
    self._port = port

  def send(self, content):
    """Sends an OscBundle or OscMessage to the server."""
    self._sock.sendto(content.dgram, (self._address, self._port))
