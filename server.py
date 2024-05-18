import socket
import json
import threading
#import requests
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
    # Add more sample sources up to 15
]

def send_list_and_details(socketC, data_list, list_keys, detail_keys):
    # Send list of items
    for idx, item in enumerate(data_list[:15]):
        item_summary = {key: item[key] for key in item if key in list_keys}
        socketC.sendall(json.dumps({"index": idx, **item_summary}).encode("utf-8"))
        ack = socketC.recv(65535).decode("utf-8")  # Receive acknowledgment
        if ack != "ACK":
            break

    # Signal the end of list
    socketC.sendall(b"END_OF_LIST")

    # Wait for item selection
    selected_idx = int(socketC.recv(65535).decode("utf-8"))

    if 0 <= selected_idx < len(data_list):
        selected_item = data_list[selected_idx]
        detail = {key: selected_item[key] for key in selected_item if key in detail_keys}
        socketC.sendall(json.dumps(detail).encode("utf-8"))



def Chandel(SocketC,cname):
 print(f"Accepted connection from {cname}")
 while True:
  request=SocketC.recv(65535).decode("utf-8")
  main_menu = "Main Menu:\n1. Search Headlines\n2. List Sources\n3. Quit\nEnter your choice: "
  SocketC.send(main_menu.encode("utf-8"))
  choice = SocketC.recv(65535).decode("utf-8").strip()
  if not request:
   break
  if choice == "1":  # Search Headlines
   while True:
            search_headlines_menu = "Search Headlines Menu:\n1. Search for Keywords\n2. Search by Category\n3. Search by Country\n4. List All News Headlines\n5. Back to Main Menu\nEnter your choice: "
            SocketC.send(search_headlines_menu.encode("utf-8"))
            search_choice = SocketC.recv(65535).decode("utf-8").strip()
            if search_choice == "1":
                # Handle searching for keywords
                pass
 
            elif search_choice == "2":
                # Handle searching by category
                category_menu = "Select a Category:\n"
                for key, value in categories.items():
                    category_menu += f"{key}: {value}\n"
                category_menu += "Enter the category: "
                SocketC.send(category_menu.encode("utf-8"))
                category_choice = SocketC.recv(65535).decode("utf-8").strip()

            elif search_choice == "3":
                # Handle searching by country
                country_menu = "Select a Country:\n"
                for key, value in countries.items():
                    country_menu += f"{key}: {value}\n"
                country_menu += "Enter the country: "
                SocketC.send(country_menu.encode("utf-8"))
                country_choice =SocketC.recv(65535).decode("utf-8").strip()

            elif search_choice == "4":
                # Handle listing all news headlines
                pass

            elif search_choice == "5":
            # Go back to the main menu
               continue
          
  elif choice == "2":  # List Sources
              sources_menu = "Sources Menu:\n1. Search by Category\n2. Search by Country\n3. Search by Language\n4. List All Sources\n5. Back to Main Menu\nEnter your choice: "
              SocketC.send(sources_menu.encode("utf-8"))
              source_choice =SocketC.recv(65535).decode("utf-8").strip()

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
                continue  # Go back to the main menu
              
  elif choice == "3":  # Quit
            break  # Terminate the connection and client  
  

    
def main():

 SocketS = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 SocketS.bind(("127.0.0.1", 6677))
 SocketS.listen(4)
 print("server listening for conections..")
 while True:
  socketC, add = SocketS.accept()
  cname=socketC.recv(65535).decode("utf-8")
  cthread=threading.Thread(target=Chandel,args=(socketC,cname))
  cthread.start()



if __name__ == "__main__":
    main()