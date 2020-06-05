import socket
import time


class ClientError(Exception):
    def __init__(self,text):
        self.text = text



class Client:
    def __init__(self, ip, port, timeout=None):
        self.ip = str(ip)
        self.port = int(port)
        self.timeout = timeout or None
        try:
            self.sock = socket.create_connection((self.ip, self.port), self.timeout)
        except:
            raise ClientError('Server is not running')

    def put(self, metric, value, timestamp=None):
        self.timestamp = timestamp or int(time.time())
        b_data_map = bytes(f'put {metric} {value} {self.timestamp}\n', 'utf8')
        try:
            self.sock.sendall(b_data_map)
        except:
            raise ClientError('No connection to server')

    def get(self):
        pass


client = Client('127.0.0.1', 8888, timeout=30)
client.put('palm.cpu', 23.7, 1150864247)
client.put("palm.cpu", 0.5, timestamp=1150864248)
client.put("eardrum.memory", 4200000)
