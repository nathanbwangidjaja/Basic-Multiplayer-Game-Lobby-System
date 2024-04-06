# Game Lobby System

This project implements a simple game lobby system using Flask and Socket.IO. It allows users to create, join, and leave lobbies. The system features real-time updates to all clients connected to a lobby when players join or leave and provides a basic UI for interaction.

## Design Decisions

### Backend (Flask + Socket.IO)
- **Flask**: Chosen for its simplicity and flexibility in setting up a web server. It's lightweight and easy to integrate with Socket.IO for real-time communication.
- **Socket.IO**: Facilitates real-time bi-directional event-based communication between web clients and the server, perfect for updating all connected clients when the state of a lobby changes.

### Frontend
- **Basic HTML/CSS/JS**: To keep the focus on the functionality of the lobby system, the frontend is kept simple. Socket.IO is used on the client side to communicate with the server in real time.
- **Notification System**: Utilizes custom notifications in the bottom right corner for a non-disruptive user experience when players join or leave lobbies.

## Setup and Running

### Requirements
- Python 3
- Flask
- Flask-SocketIO
- A modern web browser

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/nathanbwangidjaja/Basic-Multiplayer-Game-Lobby-System.git
   ```
2. Navigate to the project directory:
   ```
   cd Basic-Multiplayer-Game-Lobby-System
   ```
3. Install the required Python packages:
   ```
   pip install Flask Flask-SocketIO
   ```
4. Run the Python command:
   ```
   python app.py
   ```

## Using the Game Lobby System

After successfully starting the server with the `python app.py` command, you'll be ready to access and interact with the game lobby system through a web browser. Here's how:

### Accessing the Lobby System

1. **Open your web browser**: Any modern web browser will do (e.g., Chrome, Firefox, Safari).
2. **Navigate to the application**: Enter `http://127.0.0.1:5000/` in your browser's address bar and press `Enter`. This brings you to the main page of the game lobby system.

### Interacting With the System

**Creating a Lobby:**
- **Enter Player ID**: Find the input field labeled for the player ID on the main page. Enter your unique player ID here.
- **Create Lobby**: Click the "Create Lobby" button. A new lobby will be created with you as the first member. Other players can now join this lobby.

**Joining a Lobby:**
- **Select a Lobby**: View the list of available lobbies on the main page. Click on the lobby you wish to join.
- **Join Lobby**: After selecting a lobby, enter your player ID (if you haven't already) and click the "Join Lobby" button to become a member of the selected lobby.

**Leaving a Lobby:**
- **Leave Lobby**: If you wish to leave the lobby for any reason, simply click the "Leave Lobby" button. You will be removed from the current lobby.

**Starting a Game:**
- **Full Lobby**: Once the lobby reaches full capacity (4 players), a "Start Game" button will appear.
- **Start Game**: Clicking the "Start Game" button will initiate the game and remove the lobby, signaling the start of gameplay.

**Lobby Deletion:**
- **Automatic Deletion**: Lobbies will automatically be deleted if they reach below 1 player or after the game starts.

### Real-time Notifications
Keep an eye on the bottom right corner of the screen for real-time notifications. These notifications will inform you about players joining or leaving the lobby you are in, ensuring you're always up-to-date with the lobby status.