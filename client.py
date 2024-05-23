import socket
import json

def mainrequest(SocketC, request):
    SocketC.send(request.encode('utf-8'))
    response_length_str = SocketC.recv(10).decode('utf-8').strip()
    print(f"Received response length string: '{response_length_str}'")
    response_length = int(response_length_str)
    print(f"Received response length: {response_length}")
    response_data = b""
    while len(response_data) < response_length:
        part = SocketC.recv(response_length - len(response_data))
        response_data += part
    return json.loads(response_data.decode('utf-8'))