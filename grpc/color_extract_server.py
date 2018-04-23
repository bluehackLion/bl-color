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

from concurrent import futures
import time
import os

import grpc

from color_extract import ExtractColor
import color_extract_pb2
import color_extract_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

GRPC_PORT = os.environ['GRPC_PORT']

class Extract(color_extract_pb2_grpc.ExtractServicer):
  def __init__(self):
    self.fe = ExtractColor()

  def GetColor(self, request, context):
    color_code, color_score = self.fe.extract_color(request.file_data)
    return color_extract_pb2.ColorReply(color_code=color_code, color_score=color_score)


def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=50))
  color_extract_pb2_grpc.add_ExtractServicer_to_server(Extract(), server)
  server.add_insecure_port('[::]:' + GRPC_PORT)
  server.start()
  try:
    while True:
      time.sleep(_ONE_DAY_IN_SECONDS)
  except KeyboardInterrupt:
    server.stop(0)

if __name__ == '__main__':
  serve()
