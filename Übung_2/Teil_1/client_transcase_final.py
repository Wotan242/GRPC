from __future__ import print_function
import logging
import sys

import grpc

import transcase_pb2
import transcase_pb2_grpc




def upper(eingabe):
    
    with grpc.insecure_channel('localhost:50051') as channel:
        
        stub1 = transcase_pb2_grpc.SetCaseStub(channel)
        message_input = transcase_pb2.Input(text_in = eingabe)
        response = stub1.UpperCase(message_input)       
        print(response.text_out)
        return response.text_out

def lower(eingabe):
    
    with grpc.insecure_channel('localhost:50051') as channel:
        
        stub1 = transcase_pb2_grpc.SetCaseStub(channel)
        message_input = transcase_pb2.Input(text_in = eingabe)
        response = stub1.LowerCase(message_input)       
        print(response.text_out)
        return response.text_out

if __name__ == '__main__':

    input_list = sys.argv[1:]
    text_in = " ".join(input_list)

    upper(text_in)
    lower(text_in)
