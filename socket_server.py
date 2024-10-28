import socket
from des_ecb import ecb_encrypt, ecb_decrypt

def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        decrypt_msg = ecb_decrypt(data,"12345678")
        print("from connected user: " + decrypt_msg)
        data = input(' -> ')
        encrypt_msg = ecb_encrypt(data,"12345678")
        conn.send(encrypt_msg.encode())  # send data to the client

    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()