# GRPC_server
Création d’un serveur grpc qui implémente la méthode x --> x+1


# Installation des dépendances Python

```
python3 -m pip install -r requirements.txt
```

ou 

```
pip install -r requirements.txt
```


# Générer la fonction proto
```
python3 -m grpc_tools.protoc -I./ --python_out=. --grpc_python_out=. ./functionplusone.proto
```

---

## Pour notre usage, nous avons décidé d'utiliser le serveur en écoute par défaut sur `127.0.0.1` sur le port `26597` 

# Démarrer le serveur
```
python3 server.py -h
Usage: python3 server.py (-h|--help) (-p|--port=)<port> (-k|--keyfile=)<PathToKey> (-c|certfile=)<PathToCertificate>
```

# Démarrer le client
```
python3 client.py -h
Usage: python3 client.py (-h|--help) (-p|--port=)<port> (-c|--certfile=)<PathToCertificate>")
```
