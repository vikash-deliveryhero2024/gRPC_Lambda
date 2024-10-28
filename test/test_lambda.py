# test_lambda.py
import os
import test.test_lambda_function as test_lambda_function

# Define a sample event that mimics the structure Lambda would use
test_event = {
    "name": "Vikash Sharma"
}

# Optional: Define a mock context (not used in this example, so it can be None)
test_context = None
# Set environment variables if they are used in lambda_function
os.environ["GRPC_SERVER_URL"] = "localhost:50051" 
# Call the lambda_handler function with the test event and context
response = test_lambda_function.lambda_handler(test_event, test_context)

# Print the response to verify the output
print("Response from lambda_handler:", response)
