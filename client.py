import grpc
import functionplusone_pb2
import functionplusone_pb2_grpc
import sys, getopt

def testconnection(stub):
    try:
        return stub.Plusone(functionplusone_pb2.number(x = 5000)).reply == 5001
    except:
        return False
    




def start():
    try:
        certfile = ''
        port = 26597
        opts, args = getopt.getopt(sys.argv[1:],"hc:p:",["certfile=","port=","help"])
        for opt, arg in opts:
            if opt == '-h' or opt == "help":
                print("Usage : python3 client.py (-h|--help) (-p|--port=)<port> (-c|--certfile=)<PathToCertificat>")
                exit(1)
            elif opt == '-c' or opt == "--certfile":
                certfile = arg
            elif opt == '-p' or opt == "--port":
                port = int(arg)
        if certfile:
            with open(certfile, 'rb') as f:
                creds = grpc.ssl_channel_credentials(f.read())
            with grpc.secure_channel('127.0.0.1:' + str(port), creds) as channel:
                stub = functionplusone_pb2.QuickMathStub(channel)
                if testconnection(stub):
                    print("Connected with the server")
                else:
                    print("Could not connect to the server. Check the port or the certificate")
                    exit(1)
                while True:
                    print('Type a number or \'exit\' to exit : ',end='')
                    userinput = input()
                    if userinput == 'exit':
                        break
                    number = 0
                    try:
                        number = int(userinput)
                    except:
                        print('Please type a valid number')
                        continue
                    response = stub.Plusone(functionplusone_pb2.number(x = number))
                    print("Server responded : " + str(response.reply))
        else:
            with grpc.insecure_channel('127.0.0.1:' + str(port)) as channel:
                stub = functionplusone_pb2_grpc.QuickMathStub(channel)
                if testconnection(stub):
                    print("Connected with the server")
                else:
                    print("Could not connect to the server. Check the port")
                    exit(1)
                while True:
                    print('Type a number or \'exit\' to exit : ',end='')
                    userinput = input()
                    if userinput == 'exit':
                        break
                    number = 0
                    try:
                        number = int(userinput)
                    except:
                        print('Please type a valid number')
                        continue
                    response = stub.Plusone(functionplusone_pb2.number(x = number))
                    print("Server responded : " + str(response.reply))
    except Exception as inst:
        print(inst)
        print("Usage : python3 client.py (-h|--help) (-p|--port=)<port> (-c|--certfile=)<PathToCertificat>")

start()