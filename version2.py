import socket

def handle_request(request):
    headers = request.split('\n')
    filename = headers[0].split()[1]
    if filename == '/':
        filename = '/index.html'
    try:
        with open('htdocs' + filename, 'rb') as f:
            content = f.read()
        response = 'HTTP/1.0 200 OK\n\n'.encode() + content
    except FileNotFoundError:
        response = 'HTTP/1.0 404 NOT FOUND\n\nFile Not Found'.encode()
    return response

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8080))
    server_socket.listen(1)
    print('Listening on port 8080...')
    while True:
        client_socket, client_address = server_socket.accept()
        request = client_socket.recv(1024).decode()
        response = handle_request(request)
        client_socket.sendall(response)
        client_socket.close()

if __name__ == '__main__':
    main()
