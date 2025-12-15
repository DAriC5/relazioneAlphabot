
import socket
from prova import AlphaBot
import time

Ab = AlphaBot()

# Imposta il server UDP
SERVER_IP = "0.0.0.0"   # Ascolta su tutti gli IP locali
SERVER_PORT = 10000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((SERVER_IP, SERVER_PORT))

print(f"Server in ascolto su {SERVER_PORT}...")

try:
    while True:
        data, addr = sock.recvfrom(1024)
        comando = data.decode().strip().lower()
        print(f"Comando ricevuto da {addr}: {comando}")

        if comando == "av":
            Ab.forward()
        elif comando == "in":
            Ab.backward()
        elif comando == "si":
            Ab.left()
        elif comando == "de":
            Ab.right()
        elif comando == "s":
            Ab.stop()
        elif comando == "90r":
            Ab.r90()
        elif comando == "90l":
            Ab.l90()
        elif comando == "esci":
            print("Chiusura server...")
            break
        else:
            print("Comando non riconosciuto.")
        time.sleep(0.2)

except KeyboardInterrupt:
    print("Server interrotto manualmente.")
finally:
    Ab.stop()
    sock.close()
