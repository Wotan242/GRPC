# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import transcase_stream_pb2 as transcase__stream__pb2


class SetCaseStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.UpperCase = channel.stream_stream(
                '/SetCase/UpperCase',
                request_serializer=transcase__stream__pb2.Input.SerializeToString,
                response_deserializer=transcase__stream__pb2.Output.FromString,
                )
        self.LowerCase = channel.stream_stream(
                '/SetCase/LowerCase',
                request_serializer=transcase__stream__pb2.Input.SerializeToString,
                response_deserializer=transcase__stream__pb2.Output.FromString,
                )


class SetCaseServicer(object):
    """Missing associated documentation comment in .proto file."""

    def UpperCase(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LowerCase(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SetCaseServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'UpperCase': grpc.stream_stream_rpc_method_handler(
                    servicer.UpperCase,
                    request_deserializer=transcase__stream__pb2.Input.FromString,
                    response_serializer=transcase__stream__pb2.Output.SerializeToString,
            ),
            'LowerCase': grpc.stream_stream_rpc_method_handler(
                    servicer.LowerCase,
                    request_deserializer=transcase__stream__pb2.Input.FromString,
                    response_serializer=transcase__stream__pb2.Output.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'SetCase', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SetCase(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def UpperCase(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/SetCase/UpperCase',
            transcase__stream__pb2.Input.SerializeToString,
            transcase__stream__pb2.Output.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LowerCase(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/SetCase/LowerCase',
            transcase__stream__pb2.Input.SerializeToString,
            transcase__stream__pb2.Output.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
