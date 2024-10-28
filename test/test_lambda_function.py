import grpc
import os
import proto.your_service_pb2 as your_service_pb2
import proto.your_service_pb2_grpc as your_service_pb2_grpc

def lambda_handler(event, context):
    # Fetch the gRPC server URL from environment variables
    grpc_server_url = os.getenv("GRPC_SERVER_URL", "localhost:50051")

    # Create a channel and stub to interact with the gRPC service
    channel = grpc.insecure_channel(grpc_server_url)
    stub = your_service_pb2_grpc.YourServiceStub(channel)

    # Construct the request message using event data
    request = your_service_pb2.YourRequest(name=event.get("name", "default"))

    try:
        # Call the gRPC method and get the response
        response = stub.YourRpcMethod(request)
        return {
            "statusCode": 200,
            "body": response.message  # Adjust based on your response fields
        }
    except grpc.RpcError as e:
        # Handle any gRPC errors
        return {
            "statusCode": 500,
            "error": str(e)
        }
