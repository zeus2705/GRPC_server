import grpc
import functionplusone_pb2
import functionplusone_pb2_grpc
from concurrent import futures
import sys, getopt


#class contenant la fonction RPC
class QuickMath(functionplusone_pb2_grpc.QuickMath):

    #La function + 1
    def Plusone(self, request, context):
        print("\nPlusone was call with argument : ",str(request.x))
        return functionplusone_pb2.plusonereply(reply = request.x + 1)

#Le variable du serveur
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))


#Bind le server au port 
server.add_insecure_port('127.0.0.1:'+ '3266')

#Bind la fonction RPC au server
functionplusone_pb2_grpc.add_QuickMathServicer_to_server(QuickMath(), server)

#Start le server
server.start()

while True:
    print("Server is running type exit to stop the server :", end='')
    if input() == "exit":
        break
