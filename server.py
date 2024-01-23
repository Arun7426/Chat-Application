import socket
import threading

def handle_client(client_socket, address):
    while True:
        message = client_socket.recv(1024).decode('utf-8')
        if not message:
            break
        print(f"Received from {address}: {message}")
        client_socket.send("Message received".encode('utf-8'))
    client_socket.close()
    print(f"Connection with {address} closed.")

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 12345))
    server.listen(5)

    print("Server listening on port 12345...")

    while True:
        client_socket, address = server.accept()
        print(f"Accepted connection from {address}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket, address))
        client_handler.start()

if __name__ == "__main__":
    start_server()
