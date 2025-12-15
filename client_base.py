import socket

SERVER_IP = "192.168.1.122"  
SERVER_PORT = 10000           


client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    comando = input("Inserisci comando: ").strip().lower()
    
    if comando == "esci":
        print("Chiusura client...")
        break

    client_socket.sendto(comando.encode(), (SERVER_IP, SERVER_PORT))
    print(f"Comando '{comando}' inviato a {SERVER_IP}:{SERVER_PORT}")


client_socket.close()