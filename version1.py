mport socket
import os

def create_response(response_code, response_body):
    response_headers = {
        'Content-Type': 'text/html; charset=utf-8',
        'Content-Length': str(len(response_body)),
        'Connection': 'close',
    }

    response_headers_raw = ''.join(f'{k}: {v}\r\n' for k, v in response_headers.items())

    response = f'HTTP/1.1 {response_code}\r\n{response_headers_raw}\r\n{response_body}'
    return response.encode()

def handle_request(request):
    # parse request
    request_lines = request.split('\r\n')
    request_method, request_path, request_protocol = request_lines[0].split(' ')

    # handle file request
    if request_method == 'GET':
        file_path = request_path.strip('/')
        if not os.path.exists(file_path):
            response_body = '404 Not Found'
            return create_response('404 Not Found', response_body)
        else:
            with open(file_path, 'rb') as file:
                response_body = file.read()
            return create_response('200 OK', response_body)

    # handle invalid request
    response_body = 'Invalid request'
    return create_response('400 Bad Request', response_body)

def start_server():
    # create socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # bind socket to port
    server_socket.bind(('localhost', 8000))

    # listen for incoming connections
    server_socket.listen()

    print('Server started at http://localhost:8000/')

    while True:
        # accept incoming connection
        client_socket, client_address = server_socket.accept()

        # receive request
        request = ''
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            request += data.decode('utf-8')

        # handle request and send response
        response = handle_request(request)
        client_socket.sendall(response)

        # close connection
        client_socket.close()

if __name__ == '__main__':
    start_server()
