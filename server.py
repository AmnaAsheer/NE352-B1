import socket
import threading
import requests
import json
import os


countries = {
    "Australia": "au",
    "New Zealand": "nz",
    "Canada": "ca",
    "United Arab Emirates": "ae",
    "Saudi Arabia": "sa",
    "United Kingdom": "gb",
    "United States": "us",
    "Egypt": "eg",
    "Morocco": "ma"
}

languages = {
    "Arabic": "ar",
    "English": "en"
}

categories = {
    "Business": "business",
    "Entertainment": "entertainment",
    "General": "general",
    "Health": "health",
    "Science": "science",
    "Sports": "sports",
    "Technology": "technology"
}

sources = [
    {"name": "Source A", "country": "US", "description": "Description A", "url": "http://example.com/a", "category": "General", "language": "English"},
    {"name": "Source B", "country": "GB", "description": "Description B", "url": "http://example.com/b", "category": "Business", "language": "English"}
]


NEWS_API_KEY = 'd4b3d0b1675f48709625f2ce6cd2aea4'
BASE_URL = 'https://newsapi.org/v2/'
HOST = '127.0.0.1'
PORT = 65432

def get_allnews(endpoint, params):
    params['apiKey'] = NEWS_API_KEY
    response = requests.get(BASE_URL + endpoint, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return {'status': 'error', 'message': 'Unnable to fetch data'}

def Save_userlog(group_id, client_name, option, data):
    filename = f"{group_id}_{client_name}_{option}.json"
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def Chandel(client_socket, addr):
    print(f"Accepted connection from {addr}")
    try:
        client_name = client_socket.recv(1024).decode('utf-8')
        print(f"Client name: {client_name}")
        while True:
            request = client_socket.recv(1024).decode('utf-8')
            if not request:
                break
            print(f"Requester: {client_name}, Request: {request}")
            if request.startswith('get_news'):
                _, endpoint, params_json = request.split('|', 2)
                params = json.loads(params_json)
                news_data = get_allnews(endpoint, params)
                Save_userlog("Group-B1", client_name, "get_news", news_data)
                response = json.dumps(news_data).encode('utf-8')
                response_length = len(response)
                print(f"Sending response length: {response_length}")
                client_socket.sendall(str(response_length).encode('utf-8').ljust(10))
                client_socket.sendall(response)
                print("Response sent")
            else:
                error_response = json.dumps({'status': 'error', 'message': 'Invalid request'}).encode('utf-8')
                client_socket.sendall(str(len(error_response)).encode('utf-8').ljust(10))
                client_socket.sendall(error_response)
    except ConnectionResetError:
        pass
    finally:
        print(f"Client {client_name} disconnected")
        client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print(f'Server listening on {HOST}:{PORT}')

    while True:
        client_socket, addr = server_socket.accept()
        client_handler = threading.Thread(target=Chandel, args=(client_socket, addr))
        client_handler.start()

if __name__ == '__main__':
    main()
