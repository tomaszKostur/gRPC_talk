import logging
import grpc
from proto_out.interface_pb2_grpc import MessageServerStub
from proto_out.interface_pb2 import FrequencyInfo, MessageInfo

def run():
    with grpc.insecure_channel('localhost:50500') as channel:
        message_server = MessageServerStub(channel)
        frequency_config_response = message_server.ConfigureFrequency(FrequencyInfo(freq=2))
        print(frequency_config_response)
        message_config_response = message_server.ConfigureMessage(MessageInfo(message='modified message'))
        print(message_config_response)

if __name__ == '__main__':
    logging.basicConfig()
    run()