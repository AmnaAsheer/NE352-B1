import socket
import json

def main_menu():
    print("Main Menu:")
    print("1. Search Headlines")
    print("2. List Sources")
    print("3. Quit")

def search_headlines_menu():
    print("Search Headlines Menu:")
    print("1. Search for Keywords")
    print("2. Search by Category")
    print("3. Search by Country")
    print("4. List All News Headlines")
    print("5. Back to Main Menu")

def sources_menu():
    print("Sources Menu:")
    print("1. Search by Category")
    print("2. Search by Country")
    print("3. Search by Language")
    print("4. List All Sources")
    print("5. Back to Main Menu")

def close_socket(SocketC):
    try:
        SocketC.close()
    except Exception as e:
        print(f"Error closing socket: {e}")

def receive_list(SocketC):
    items = []
    while True:
        response = SocketC.recv(65535).decode("utf-8")
        if response == "END_OF_LIST":
            break
        item = json.loads(response)
        items.append(item)
        SocketC.send("ACK".encode("utf-8"))  # Send acknowledgment
    return items

def display_items(items):
    for item in items:
        print(f"{item['index']}. {json.dumps(item, indent=2)}")

def receive_and_print(socket):
    response = socket.recv(65535).decode("utf-8")
    print(response)
    return response

def main():
 username = input("Enter your username: ")

 with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as SocketC:
        SocketC.connect(("127.0.0.1", 6677))
        SocketC.send(username.encode("utf-8"))

 while True:
            main_menu()
            choice = input("Enter your choice: ")
            SocketC.send(choice.encode("utf-8"))

            if choice == "1":  # Search Headlines
                while True:
                    search_headlines_menu()
                    search_choice = input("Enter your choice: ")
                    SocketC.send(search_choice.encode("utf-8"))
                    if search_choice == "1":
                        # Handle searching for keywords
                        pass
                    elif search_choice == "2":
                        # Handle searching by category
                        category_response = receive_and_print(SocketC)
                        category_choice = input("Enter the category: ")
                        SocketC.send(category_choice.encode("utf-8"))
                    elif search_choice == "3":
                        # Handle searching by country
                        country_response = receive_and_print(SocketC)
                        country_choice = input("Enter the country: ")
                        SocketC.send(country_choice.encode("utf-8"))    
                    elif search_choice == "4":
                        # Handle listing all news headlines
                        pass
                    elif search_choice == "5":
                        break  # Go back to the main menu


            elif choice == "2":  # List Sources
                while True:
                    sources_menu()
                    source_choice = input("Enter your choice: ")
                    SocketC.send(source_choice.encode("utf-8"))
                    if source_choice == "1":
                        # Handle searching sources by category
                        pass
                    elif source_choice == "2":
                        # Handle searching sources by country
                        pass
                    elif source_choice == "3":
                        # Handle searching sources by language
                        pass
                    elif source_choice == "4":
                        # Handle listing all sources
                        pass
                    elif source_choice == "5":
                        break  # Go back to the main menu

        
            elif choice == "3":  # Quit
                 print("Quitting...")
                 break  # Terminate the connection and close the client

 SocketC.close()

if __name__ == "__main__":
    main()      