from audioop import add
import socket

host = ''
port = 53

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen(port)
    conn, addr = s.accept()
    with conn:
        print('Connected By : ', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
