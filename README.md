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
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd game-lobby-system
   ```
3. Install the required Python packages:
   ```
   pip install Flask Flask-SocketIO
   ```
4. Run the Flask application:
   ```
   flask run
   ```
   Or, if you prefer using `python` command:
   ```
   python app.py
   ```

## Interacting with the System

### Creating a Lobby
- Enter your player ID in the designated input field and click the "Create Lobby" button. A new lobby will be created, and you will automatically join as the first member.

### Joining a Lobby
- Click on any lobby from the list of available lobbies to select it. Then, enter your player ID and click the "Join Lobby" button to join.

### Leaving a Lobby
- To leave a lobby, simply click the "Leave Lobby" button while you are in a lobby.

### Starting a Game
- If you are in a full lobby (4 players), a "Start Game" button will appear. Clicking this button will start the game and remove the lobby.

### Real-time Notifications
- Real-time notifications appear at the bottom right of the screen, informing you when other players join or leave the lobby you are in.

### API Endpoints and WebSocket Events
- The system primarily interacts through WebSocket events for joining, leaving, and updating lobbies.
- HTTP GET `/lobbies` is available to fetch the current list of lobbies and their statuses.

For detailed interaction flows and additional functionalities, refer to the source code documentation within `app.py` and `index.html`.
