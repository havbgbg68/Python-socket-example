import socket
# 看範例加點東西
def Main():
    host = "127.0.0.1"  # 127.0.0.1 means localhost
    port = 5000 # port can be set to any number, it's better to set >1024

    SIZE = 1024

    # creat socket and bind
    mySocket = socket.socket()
    mySocket.bind((host,port))
    
    # listen for client to connect, 1 means allow 1 client to connect
    mySocket.listen(1)
    conn, addr = mySocket.accept()

    print("waiting for connection...")
    print("Connection from: " + str(host) + ":" + str(port))
    while True:
            data = conn.recv(SIZE).decode()
            if not data:
                break
            print ("from connected  user: " + str(data))

            data = str(data)
            print ("sending: " + str(data))
            conn.send(data.encode())

    conn.close()

if __name__ == '__main__':
    Main()