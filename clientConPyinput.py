import socket
from pynput import keyboard

SERVER_IP = "192.168.1.122"  
SERVER_PORT = 10000           

def tasto():
    def on_press(key):
        print(key)
        if key.char == 'w':
            invia('av')
        elif key.char == 'd':
            invia('de')
        elif key.char == 'a':
            invia('si')
        elif key.char == 's':
            invia('in')
        
    def on_release(key):
        print(f"rel = {key}")
        if key.char == 'a' or key.char == 's' or key.char == 'd' or key.char == 'w':
            invia('s')

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

    listener = keyboard.Listener(on_press=on_press,on_release=on_release)
    listener.start()

def invia(dato):
    print(f"comando = {dato}")

    client_socket.sendto(dato.encode(), (SERVER_IP, SERVER_PORT))
    print(f"Comando '{dato}' inviato a {SERVER_IP}:{SERVER_PORT}")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    tasto()
