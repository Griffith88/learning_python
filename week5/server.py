import asyncio

METRIC = []


class ServerProtocol(asyncio.Protocol):
    def __init__(self):
        self.transport = None

    def connection_made(self, transport: asyncio.Transport):
        self.transport = transport

    def data_received(self, data: bytes):
        req = data.decode()[:-1].split(' ')
        method = req[0]
        query = req[1:]
        if method == 'get':
            res = self._get(query)
        elif method == 'put':
            res = self._put(query)
        else:
            res = 'error\nwrong command\n\n'
        self.transport.write(res.encode())

    @staticmethod
    def _get(query):
        if len(query) != 1:
            return 'error\nwrong command\n\n'

        if query[0] == '*':
            data = METRIC
        else:
            data = [info for info in METRIC if info[0] == query[0]]

        data = [f'{info[0]} {info[1]} {info[2]}' for info in data]

        res = '\n'.join(['ok'] + data)

        return f'{res}\n\n'

    @staticmethod
    def _put(query):
        if len(query) != 3:
            return 'error\nwrong command\n\n'

        try:
            float(query[1])
        except:
            return 'error\nwrong command\n\n'

        try:
            int(query[2])
        except:
            return 'error\nwrong command\n\n'

        # query: ['test_key', '12.0', '1503319740']
        # if any([lambda info: info[0] == query[0] and info[2] == query[2] for info in METRIC]):

        data = [query[0], float(query[1]), int(query[2])]

        for i, info in enumerate(METRIC):
            if info[0] == data[0] and info[2] == data[2]:
                METRIC[i] = query

        if query not in METRIC:
            METRIC.append(data)

        return 'ok\n\n'


def run_server(host='127.0.0.1', port=8888):
    loop = asyncio.get_event_loop()
    coroutine = loop.create_server(ServerProtocol, host, int(port))

    server = loop.run_until_complete(coroutine)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()


if __name__ == '__main__':
    run_server()