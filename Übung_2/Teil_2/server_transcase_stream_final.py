from concurrent import futures
import logging

import grpc

import transcase_stream_pb2
import transcase_stream_pb2_grpc




class Trans(transcase_stream_pb2_grpc.SetCaseServicer):

    

    def UpperCase(self, request_iterator, context):
        for word in request_iterator:
            result = word.text_in.upper()
            print(result)
            yield transcase_stream_pb2.Output(text_out = result)

    def LowerCase(self, request_iterator, context):
        for word in request_iterator:
            result = word.text_in.lower()
            print(result)
            yield transcase_stream_pb2.Output(text_out = result)

        



def serve():
    print("Server launched. Waiting for RPCs")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    
    transcase_stream_pb2_grpc.add_SetCaseServicer_to_server(Trans(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
