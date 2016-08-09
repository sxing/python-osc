from pythonosc import dispatcher
from pythonosc import osc_server

dispatch = dispatcher.Dispatcher()
dispatch.map("/*", print)

address = ("239.255.0.76", 10076)
interface_addr = "192.168.0.120"

server = osc_server.ThreadingOSCUDPServer(address, dispatch, interface_addr)
#server = osc_server.ThreadingOSCUDPServer(("239.255.0.76", 10076), dispatch)

print("Listening to {} through {}".format(address, interface_addr))
server.serve_forever()
