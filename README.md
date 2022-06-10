# GRPC_server
Création d’un serveur grpc qui implémente la méthode x --> x+1


# Dependance
python3 -m pip install -r requirements.txt


# generate proto
python3 -m grpc_tools.protoc -I./ --python_out=. --grpc_python_out=. ./functionplusone.proto

# start server
```Usage : python3 server.py (-h|help) (-p|-port=)<port> (-c|certfile=)<PathToCertificat> (-a|authorityfile=)<PathToTrustedAuthority>"```

# start client
```print("Usage : python3 client.py (-h|--help) (-p|--port=)<port> (-c|--certfile=)<PathToCertificat>")```
