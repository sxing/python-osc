"""Small example OSC client

This program sends 10 random values between 0.0 and 1.0 to the /filter address,
waiting for 1 seconds between each value.
"""
import argparse
import random
import time

from pythonosc import osc_message_builder
from pythonosc import udp_client


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip", default="127.0.0.1",
      help="The ip of the OSC server")
  parser.add_argument("--port", type=int, default=5005,
      help="The port the OSC server is listening on")
  parser.add_argument("--ifaceip", default="127.0.0.1",
      help="The ip of the interface to send on if multicast")
  parser.add_argument("--ttl", type=int, default="1",
      help="TTL if multicast")
  args = parser.parse_args()

  client = udp_client.UDPClient(args.ip, args.port, args.ttl, args.ifaceip)

  for x in range(100):
    msg = osc_message_builder.OscMessageBuilder(address="/filter")
    msg.add_arg(random.random())
    msg = msg.build()
    print("Sending", msg.dgram)
    client.send(msg)
    time.sleep(1)
