# This skeleton is valid for both Python 2.7 and Python 3.
# You should be aware of your additional code for compatibility of the Python version of your choice.

# Import socket module
from socket import *

# Create a TCP server socket
# (AF_INET is used for IPv4 protocols)
# (SOCK_STREAM is used for TCP)
serverSocket = socket(AF_INET, SOCK_STREAM)


# Prepare a server socket.
host = '127.0.0.1'
serverPort = '6789'

# Bind the socket to server address and server port
# A TCP based echo server

echoSocket = socket.socket()
echoSocket.bind((host, serverPort))

# Listen to at most 1 connection at a time (max. number of threads in the connection queue)

echoSocket.listen(1)

# FILL IN END

# Server should be up and running and listening to the incoming connections
while True:
    print('Ready to serve...')

    # Set up a new connection from the client
    connectionSocket, addr = serverSocket.accept()

    # If an exception occurs during the execution of try clause
    # the rest of the clause is skipped
    # If the exception type matches the word after except
    # the except clause is executed
    try:
        # Receives the request message from the client
        message = connectionSocket.recv(1024).decode()

        # Extract the path of the requested object from the message
        # The path is the second part of HTTP header, identified by [1]
        filepath = message.split()[1]
        # filepath variable now contains the path to the requested object
        # e.g. /HelloWorld.html
        # Remember that the requested file must be in the same folder as the server code.

        # Because the extracted path of the HTTP request includes
        # a character '\', we read the path from the second character
        f = open(filepath[1:])
        # f variable now contains the file specified by the filepath

        # Read the file "f" and store the entire content of the requested file in a temporary buffer
        outputdata = f.read()
        # outputdata variable now contains the html code that the server is to send to the requesting client

        # FILL IN START

        # Sending the HTTP response header line to the connection socket
        # The response should be in the following format: "HTTP/1.1 *code-for-successful-request*\r\n\r\n"
        connectionSocket.send(bytes('HTTP/1.1 200 OK\r\n\r\n', 'UTF-8'))

        # FILL IN END

        # Send the content of the requested file to the connection socket
        response = outputdata + "\r\n"
        # connectionSocket.send(response) #Python 2.7
        connectionSocket.send(response.encode())  # Python 3

        # Close the client connection socket
        connectionSocket.close()

    except (IOError, IndexError):
        # FILL IN START
        connectionSocket.send(bytes('HTTP/1.1 404 Not Found\r\n\r\n', 'UTF-8'))

        # FILL IN END
        connectionSocket.send(
            "<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n")

    # FILL IN START
    # Close the client connection socket

    # FILL IN END

serverSocket.close()
