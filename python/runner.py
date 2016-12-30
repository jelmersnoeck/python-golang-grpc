"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function

import grpc
import time

import message_pb2
import message_pb2_grpc


def run():
  channel = grpc.insecure_channel('golang:5001')
  stub = message_pb2_grpc.GreeterStub(channel)
  time.sleep(5)

  while True:
      response = stub.Fetch(message_pb2.Request(name='you'))
      print("Greeter client received: " + response.message)
      time.sleep(3)


if __name__ == '__main__':
  run()
