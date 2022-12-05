from proto_out.interface_pb2_grpc import MessageServerServicer, add_MessageServerServicer_to_server
from proto_out.interface_pb2 import ConfigurationStatus

import grpc
import logging
import asyncio

class MessageServer(MessageServerServicer):
    def __init__(self, work_handler) -> None:
        self.work_handler = work_handler

    async def ConfigureFrequency(self, request, _context):
        await self.work_handler.change_freq(request.freq)
        return ConfigurationStatus(status="success")

    async def ConfigureMessage(self, request, _context):
        await self.work_handler.change_message(request.message)
        return ConfigurationStatus(status="success")

class Worker:
    def __init__(self) -> None:
        self.freq = 1
        self.message = "python server"
        print("worker created")

    async def change_freq(self, freq):
        self.freq = freq

    async def change_message(self, message):
        self.message = message

    async def work_loop(self):
        while True:
            print(self.message)
            await asyncio.sleep(1/self.freq)

async def serve():
    port = '50500'
    grpc_server = grpc.aio.server()
    worker = Worker()
    message_server = MessageServer(worker)
    add_MessageServerServicer_to_server(message_server, grpc_server)
    grpc_server.add_insecure_port('[::]:' + port)
    await asyncio.gather(worker.work_loop(), grpc_server.start())
    print("Server started, listening on " + port)
    await grpc_server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    asyncio.run(serve())