import grpc
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities

import message_pb2 as message__pb2
import message_pb2 as message__pb2


class GreeterStub(object):

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Fetch = channel.unary_unary(
        '/protos.Greeter/Fetch',
        request_serializer=message__pb2.Request.SerializeToString,
        response_deserializer=message__pb2.Response.FromString,
        )


class GreeterServicer(object):

  def Fetch(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_GreeterServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Fetch': grpc.unary_unary_rpc_method_handler(
          servicer.Fetch,
          request_deserializer=message__pb2.Request.FromString,
          response_serializer=message__pb2.Response.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'protos.Greeter', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
