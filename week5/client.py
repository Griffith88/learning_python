import socket
import time
import operator

class ClientError(Exception):
    def __init__(self, text):
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
        b_answer = bytes('', 'utf8')
        try:
            while not b_answer.endswith(bytes('\n\n', 'utf8')):
                b_answer += self.sock.recv(1024)
        except:
            raise ClientError('Can\'t recieve data')
        if not b_answer.startswith(bytes('ok', 'utf8')):
            raise ClientError('Invalid Answer')
        answer = b_answer.decode('utf-8')
        return answer

    def get(self, key):
        b_request = bytes(f'get {key}\n', 'utf8')
        try:
            self.sock.sendall(b_request)
        except:
            raise ClientError('No connection to server')
        b_answer = bytes('', 'utf8')
        try:
            while not b_answer.endswith(bytes('\n\n', 'utf8')):
                b_answer += self.sock.recv(1024)
        except:
            raise ClientError('Can\'t recieve data')
        if not b_answer.startswith(bytes('ok\n', 'utf8')):
            raise ClientError('Invalid Answer')
        # elif b_answer.startswith(bytes('error\n', 'utf8')):
        #     raise ClientError('Error Requesting')
        answer = b_answer.decode('utf-8')
        try:
            status, data_answer = answer.split('\n', 1)
        except:
            raise ClientError('Invalid extract')
        if status == 'error':
            raise ClientError('Error requesting')
        data_answer = data_answer.strip()
        data_dict = {}
        if data_answer == '':
            return data_dict
        for row in data_answer.split('\n'):
            try:
                key, value, timestamp = row.split()
            except:
                raise ClientError('Error extract')
            if key not in data_dict:
                data_dict[key] = []
            try:
                data_dict[key].append((int(timestamp), float(value)))
            except:
                raise ClientError('Invalid values')
        # s_data_dict = sorted(data_dict.items(), key=lambda x: x[1][0], reverse=False)
        s_data_dict = {item[0]: sorted(item[1]) for item in data_dict.items()}
        return dict(s_data_dict)

# client = Client('127.0.0.1', 8888, timeout=30)
# print(client.get('*'))
