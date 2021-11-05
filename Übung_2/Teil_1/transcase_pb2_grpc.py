# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import transcase_pb2 as transcase__pb2


class SetCaseStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.UpperCase = channel.unary_unary(
                '/SetCase/UpperCase',
                request_serializer=transcase__pb2.Input.SerializeToString,
                response_deserializer=transcase__pb2.Output.FromString,
                )
        self.LowerCase = channel.unary_unary(
                '/SetCase/LowerCase',
                request_serializer=transcase__pb2.Input.SerializeToString,
                response_deserializer=transcase__pb2.Output.FromString,
                )


class SetCaseServicer(object):
    """Missing associated documentation comment in .proto file."""

    def UpperCase(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LowerCase(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SetCaseServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'UpperCase': grpc.unary_unary_rpc_method_handler(
                    servicer.UpperCase,
                    request_deserializer=transcase__pb2.Input.FromString,
                    response_serializer=transcase__pb2.Output.SerializeToString,
            ),
            'LowerCase': grpc.unary_unary_rpc_method_handler(
                    servicer.LowerCase,
                    request_deserializer=transcase__pb2.Input.FromString,
                    response_serializer=transcase__pb2.Output.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'SetCase', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SetCase(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def UpperCase(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SetCase/UpperCase',
            transcase__pb2.Input.SerializeToString,
            transcase__pb2.Output.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LowerCase(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SetCase/LowerCase',
            transcase__pb2.Input.SerializeToString,
            transcase__pb2.Output.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
