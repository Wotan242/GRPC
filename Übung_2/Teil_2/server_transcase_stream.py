# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter server."""

from concurrent import futures
import logging

import grpc

import transcase_stream_pb2
import transcase_stream_pb2_grpc




class Trans(transcase_stream_pb2_grpc.SetCaseServicer):

    

    def UpperCase(self, request_iterator, context):
        for word in <****>:
            result = word.text_in.upper()
            print(result)
            <****> transcase_stream_pb2.Output(text_out = result)

    def LowerCase(self, request_iterator, context):
        for word in <****>:
            result = word.text_in.lower()
            print(result)
            <****> transcase_stream_pb2.Output(text_out = result)

        



def serve():
    print("Server launched. Waiting for RPCs.")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    
    transcase_stream_pb2_grpc.add_SetCaseServicer_to_server(Trans(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
