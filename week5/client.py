import socket
# import time
#
# class Client:
#     def __init__(self, ip, port, timeout=None):
#         self.ip = str(ip)
#         self.port = int(port)
#         self.timeout = timeout or None
#
#         with socket.create_connection((self.ip, self.port)) as sock:
#             self.sock = sock
#             pass
#
#     def put(self, metric, value, timestamp=None):
#         data_map = (metric, value, timestamp)
#         self.sock.sendall('data'.encode('utf8'))
#
#     def get(self):
#         pass

sock = socket.create_connection(("127.0.0.1", 10001))
sock.sendall('daasdasdas'.encode('utf8'))


