from proto_out.interface_pb2_grpc import MessageServerServicer, add_MessageServerServicer_to_server
from proto_out.interface_pb2 import ConfigurationStatus

import grpc
import logging
from concurrent import futures

class MessageServer(MessageServerServicer):
    def ConfigureFrequency(self, _request, _context):
        return ConfigurationStatus(status="success")

    def ConfigureMessage(self, _request, _context):
        return ConfigurationStatus(status="success")


def serve():
    port = '50500'
    grpc_server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    add_MessageServerServicer_to_server(MessageServer(), grpc_server)
    grpc_server.add_insecure_port('[::]:' + port)
    grpc_server.start()
    print("Server started, listening on " + port)
    grpc_server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()