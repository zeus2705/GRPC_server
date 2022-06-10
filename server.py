
import grpc
import functionplusone_pb2
import functionplusone_pb2_grpc
from concurrent import futures
import sys, getopt


class QuickMath(functionplusone_pb2_grpc.QuickMath):
    def Plusone(self, request, context):
        print("\nPlusone was call with argument : ",str(request.x))
        return functionplusone_pb2.plusonereply(reply = request.x + 1)


server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

def start():
    try:
        keyfile = ''
        chainfile = ''
        port = 26597
        if keyfile or chainfile:
            print("Starting the server with SSL/TLS on port " + str(port))
            with open(keyfile, 'rb') as f:
                private_key = f.read()
            with open(sys.argv[2], 'rb') as f:
                certificate_chain = f.read()
            server_credentials = grpc.ssl_server_credentials( ( (private_key, certificate_chain) ) )
            server.add_secure_port('127.0.0.1:' + str(port) , server_credentials)
        else:
            print("Starting the server without SSL/TLS on port " + str(port))
            server.add_insecure_port('127.0.0.1:'+ str(port))

        functionplusone_pb2_grpc.add_QuickMathServicer_to_server(QuickMath(), server)
        server.start()
        while True:
            print("Server is running type exit to stop the server :", end='')
            if input() == "exit":
                break
    except Exception as inst:
        print(inst)

start()
    