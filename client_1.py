import socket
 
def Main():
        host = '127.0.0.1'      # the server IP
        port = 5000

        SIZE = 1024

        # Creat the socket and connect to server
        mySocket = socket.socket()
        mySocket.connect((host,port))

        message = input("Input message: ")

        while message != 'q':
                mySocket.send(message.encode())
                data = mySocket.recv(SIZE).decode()

                print ('->Received from server: ' + data)
                print ('-------------------------------')

                message = input("Input message: ")

        mySocket.close()
 
if __name__ == '__main__':
    Main()