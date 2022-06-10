import grpc
import functionplusone_pb2
import functionplusone_pb2_grpc
import sys, getopt

#ouvre une client en connection avec le server GRPC
with grpc.insecure_channel('127.0.0.1:' + '3266') as channel:

    #connecte le client au fonction QuickMath
    stub = functionplusone_pb2_grpc.QuickMathStub(channel)
    while True:
        print('Type a number or exit to exit : ',end='')
        userinput = input()
        if userinput == 'exit':
            break
        number = 0
        try:
            number = int(userinput)
        except:
            print('Please type a valid number')
            continue
        
        #Utilise la fonction avec l'entre utilisateur
        response = stub.Plusone(functionplusone_pb2.number(x = number))

        print("Plusone server responded : " + str(response.reply))