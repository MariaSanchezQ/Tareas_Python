import socket
import threading

host = '127.0.0.1'
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((host, port))
server.listen()
print(f"Server running on {host}:{port}")

clientes = []
usuario = []

def broadcast(mensaje, _clientes):
    for clientes in clientes:
        if clientes != _clientes:
            clientes.send(mensaje)

def handle_mensajes(clientes):
    while True:
        try:
            mensaje = clientes.recv(1024)
            broadcast(mensaje, clientes)
        except:
            index = clientes.index(clientes)
            usuario = usuario[index]
            broadcast(f"ChatBot: {usuario} desconectado".encode('utf-8'), clientes)
            clientes.remove(clientes)
            usernames.remove(usuario)
            client.close()

            break

def receive_conections():
    while True:
        client, adress = server.accept()

        client.send("@usuario".encode("utf-8"))
        usuario = clientes.recv(1024).decode('utf-8')

        clientes.append(clientes)
        usernames.append(usuario)

        print(f"{usuario} esta conectado con {str(address)}")

        mensaje = f"ChatBot: {usuario} se ha unido al chat!".encode("utf-8")
        broadcast(mensaje, clientes)
        clientes.send("Conectando con el servidor".encode("utf-8"))

        thread = threading.Thread(target=handle_mensajes, args=(client,))
        thread.start()

receive_conections()