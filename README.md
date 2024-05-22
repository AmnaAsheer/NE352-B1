### Project Title
*News Aggregator and Distribution Server*

### Project Description
This project involves the development of a multi-threaded server application that aggregates news from various sources using the News API and distributes the fetched news data to connected clients upon request. The server listens for incoming client connections on a specified host and port, managing each client connection in a separate thread to handle multiple clients simultaneously

### Semester
2nd

### Group 
Group B1

### Table of Contents

### Requirements
1. User need to install python
2. Local envioronment is required to run this application steps to which are provided in How to section

### How to

1. Create a virtual environment if not available - `python -m venv venv`
2. Activate the virtual environment - `.\venv\Scripts\activate`
3. Install all dependencies - `pip install requests`
4. Now run your server - `python server.py`
5. Now open another terminal and run - `python client.py`
   
All Set! app is running now

### The scripts
1. `client.py` - this script have the code for all the functionalities at client side
2. `server.py` - this file represents the server configuration and settings

### Acknowledgments
We want to thank our professor Dr. Mohammed Almeer for his continuing support during this project and available documentations online regarding this project
