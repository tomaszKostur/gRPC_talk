1. Write proto file
2. python -m pip install grpcio grpcio-tools
3. python -m grpc_tools.protoc -I. --python_out=./proto_out --pyi_out=./proto_out --grpc_python_out=./proto_out interface.proto