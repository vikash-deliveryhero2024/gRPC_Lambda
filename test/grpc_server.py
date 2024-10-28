import grpc
from concurrent import futures
import time
import proto.your_service_pb2 as your_service_pb2
import proto.your_service_pb2_grpc as your_service_pb2_grpc

# Define the gRPC service class, inheriting from the generated class
class YourServiceServicer(your_service_pb2_grpc.YourServiceServicer):
    def YourRpcMethod(self, request, context):
        # Define the response message
        return your_service_pb2.YourResponse(message=f"Hello, {request.name}")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    your_service_pb2_grpc.add_YourServiceServicer_to_server(YourServiceServicer(), server)
    server.add_insecure_port('[::]:50051')  # Listening on port 50051
    server.start()
    print("gRPC server running on port 50051...")
    try:
        while True:
            time.sleep(86400)  # Keep server running
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == "__main__":
    serve()