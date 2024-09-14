# Qu'est ce que hosterNetPython ?

#### hosterNetPython est un package pour héberger toutes les fonctions du net dans python, que ce sois pour les db ou pour les socketDict. Les fonctions de socket, http.server, socketserver, vidstream seront dans les modules

## Pourquoi utiliser hosterNetPython ?

#### Utiliser hosterNetPython permet de créer ou d'éxécuter des scripts préfait mais très important comme :
    les serveurs http
    les serveurs avec une base de donnée pour avec fonctions de connexions
    les serveurs de chat

## Les fonctions principales
### 1. socketChat (La fonction serveur)
#### SocketChat permet d'héberger des chats avec la librairie socket 
#### Cette fonction peut vous servir à créer des chats en 3 ligne de code


```bash
    from hosterNetPython.socketServer.chat import socketChat

    server = socketChat(host: str, port: int)
    server.startChat()

```

## 2. SocketDb
```bash
    from hosterNetPython.socketServer.db import socketDb

    server = socketDb(host: str, port: int, db_name: str)
    server.startDb()

```
