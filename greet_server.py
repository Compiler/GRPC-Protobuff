


import greet_pb2, greet_pb2_grpc


class GreetServicer(greet_pb2_grpc.GreeterServicer):

    def SayHello(self, request, context):
        return super().SayHello(request, context)

    def ParrotSaysHello(self, request, context):
        return super().ParrotSaysHello(request, context)

    def ChattyClientSaysHello(self, request_iterator, context):
        return super().ChattyClientSaysHello(request_iterator, context)

    def InteractingHello(self, request_iterator, context):
        return super().InteractingHello(request_iterator, context)
        