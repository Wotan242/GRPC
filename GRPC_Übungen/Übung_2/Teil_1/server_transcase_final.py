from concurrent import futures
import logging

import grpc

import transcase_pb2
import transcase_pb2_grpc




class Trans(transcase_pb2_grpc.SetCaseServicer):

    

    def UpperCase(self, request, context):

        result = request.text_in.upper()
        print(result)
        return transcase_pb2.Output(text_out = result)

    def LowerCase(self, request, context):

        result = request.text_in.lower()
        print(result)
        return transcase_pb2.Output(text_out = result)



def serve():
    print("Server launched. Waiting for RPCs.")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    
    transcase_pb2_grpc.add_SetCaseServicer_to_server(Trans(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
