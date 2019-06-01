from app.common.server.base import ServerBase

from app.http.handlers.test import test_handler

class HttpServer(ServerBase):

    def __init__(self, host, port):
        ServerBase.__init__(self, host, port)

    def register_handles(self):
        route = [
            (r'/REQ_TEST',test_handler),
        ]
        # route.extend(self.register_handles_test())

        return route