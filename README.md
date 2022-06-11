# GRPC_server
Création d’un serveur grpc qui implémente la méthode x --> x+1


# Dependance
python3 -m pip install -r requirements.txt


# generate proto
python3 -m grpc_tools.protoc -I./ --python_out=. --grpc_python_out=. ./functionplusone.proto

# start server
```
python3 server.py -h
Usage: python3 server.py (-h|--help) (-p|--port=)<port> (-k|--keyfile=)<PathToKey> (-c|certfile=)<PathToCertificate>
```

# start client
```
python3 client.py -h
Usage: python3 client.py (-h|--help) (-p|--port=)<port> (-c|--certfile=)<PathToCertificate>")
```
