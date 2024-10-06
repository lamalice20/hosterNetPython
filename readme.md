# What is hosterNetPython?

#### hosterNetPython is a package to host all net functions in python, whether for db or socketDict. Socket, http.server, socketserver, vidstream functions will be in modules

## Why use hosterNetPython?

#### Using hosterNetPython allows you to create or execute pre-made but very important scripts like:
    http servers
    servers with a database for connection functions
    chat servers

## Main functions
### 1. socketChat (The server function)
#### SocketChat allows you to host chats with the socket library 
#### This function can be used to create chats in 3 lines of code

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