from __future__ import print_function
import logging
import sys

import grpc

import transcase_stream_pb2
import transcase_stream_pb2_grpc




def upper(eingabe):
    
    with grpc.insecure_channel('localhost:50051') as channel:
        
        stub1 = transcase_stream_pb2_grpc.SetCaseStub(channel)
        eingabe_list = eingabe.split(" ")        
        response_iterator = stub1.UpperCase(generate_message(eingabe_list))  
        for word in response_iterator:    
            print(word.text_out)

def lower(eingabe):
    
    with grpc.insecure_channel('localhost:50051') as channel:
        
        stub1 = transcase_stream_pb2_grpc.SetCaseStub(channel)
        eingabe_list = eingabe.split(" ")
        response_iterator = stub1.LowerCase(generate_message(eingabe_list))  
        for word in response_iterator:    
            print(word.text_out)

def generate_message(in_list):
            for word in in_list:
                message_input = transcase_stream_pb2.Input(text_in = word)
                yield message_input
        


if __name__ == '__main__':
    input_list = sys.argv[1:]
    text_in = " ".join(input_list)

    upper(text_in)
    lower(text_in)
    
