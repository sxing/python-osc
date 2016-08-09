"""Small example OSC server

This program listens to several addresses, and prints some information about
received packets.
"""
import argparse
import math

from pythonosc import dispatcher
from pythonosc import osc_server

def print_volume_handler(unused_addr, args, volume):
  print("[{0}] ~ {1}".format(args[0], volume))

def print_compute_handler(unused_addr, args, volume):
  try:
    print("[{0}] ~ {1}".format(args[0], args[1](volume)))
  except ValueError: pass

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip",
      default="127.0.0.1", help="The ip (multicast or unicast) to listen on")
  parser.add_argument("--port",
      type=int, default=5005, help="The port to listen on")
  parser.add_argument("--ifaceip",
      default="127.0.0.1", help="The ip of the interface to listen on, if multicast")
  args = parser.parse_args()

  dispatcher = dispatcher.Dispatcher()
  dispatcher.map("/*", print)

  address = (args.ip, args.port)
  interface_addr = args.ifaceip

  server = osc_server.ThreadingOSCUDPServer(address, dispatcher, interface_addr)
  
  print("Listening to {} through {}".format(address, interface_addr))
  server.serve_forever()
