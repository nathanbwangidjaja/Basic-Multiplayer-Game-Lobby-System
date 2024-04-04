from flask import Flask, render_template, jsonify, request
from flask_socketio import SocketIO, join_room, leave_room, emit
import uuid

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

# Dictionary to store lobbies and their details
lobbies = {}

# Serve the main page
@app.route('/')
def home():
    return render_template('index.html')

# Handle the creation of a new lobby
@socketio.on('create_lobby')
def handle_create_lobby(data):
    # Generate a unique ID for the new lobby
    lobby_id = str(uuid.uuid4())
    # Initialize the lobby with the player who created it
    lobbies[lobby_id] = {'players': [data['playerId']], 'status': 'waiting'}
    # Add the player to the lobby's room for Socket.IO communication
    join_room(lobby_id)
    # Notify the player that the lobby has been created
    emit('lobby_created', {'lobbyId': lobby_id}, room=lobby_id)

# Handle a player's request to join a lobby
@socketio.on('join_lobby')
def handle_join_lobby(data):
    lobby_id = data['lobbyId']
    player_id = data['playerId']
    
    if lobby_id in lobbies:
        lobby = lobbies[lobby_id]
        # Check if the player is already in the lobby
        if player_id in lobby['players']:
            emit('join_error', {'message': "You are already in this lobby."}, to=request.sid)
        elif len(lobby['players']) < 4:
            # Add the player to the lobby and update its status
            lobby['players'].append(player_id)
            join_room(lobby_id)
            isFull = len(lobby['players']) == 4
            lobby['isFull'] = isFull
            # Notify all players in the lobby about the update
            emit('lobby_update', {'lobbyId': lobby_id, 'isFull': isFull, 'players': lobby['players']}, room=lobby_id)
            # Immediately notify the player that they have joined the lobby
            emit('player_action', {'message': f"Player {player_id} has joined the lobby."}, to=request.sid)
        else:
            # Notify the player if the lobby is full
            emit('lobby_full', {'message': "Lobby is full."}, to=request.sid)
    else:
        # Notify the player if the lobby does not exist
        emit('lobby_not_found', {'message': "Lobby does not exist."}, to=request.sid)

# Endpoint to start a game in a lobby
@app.route('/startGame', methods=['POST'])
def start_game():
    data = request.json
    lobby_id = data.get('lobbyId')
    if lobby_id in lobbies:
        # Notify all players in the lobby that the game has started
        socketio.emit('game_started', {'lobbyId': lobby_id}, room=lobby_id)
        # Remove the lobby after the game starts
        del lobbies[lobby_id]
        return jsonify({"message": "Game started."}), 200
    return jsonify({"message": "Lobby does not exist."}), 400

# Handle a player leaving a lobby
@socketio.on('leave_lobby')
def handle_leave_lobby(data):
    lobby_id = data['lobbyId']
    player_id = data['playerId']
    # Notify the player that they have left the lobby
    if lobby_id in lobbies and player_id in lobbies[lobby_id]['players']:
        # Remove the player from the lobby and update its status
        emit('player_action', {'message': f"Player {player_id} has left the lobby."}, to=request.sid)
        lobbies[lobby_id]['players'].remove(player_id)
        leave_room(lobby_id)
        isFull = len(lobbies[lobby_id]['players']) == 4
        # Notify all remaining players in the lobby about the update
        emit('lobby_update', {'lobbyId': lobby_id, 'players': lobbies[lobby_id]['players'], 'isFull': isFull}, room=lobby_id)
        # Remove the lobby if it's empty
        if not lobbies[lobby_id]['players']:
            del lobbies[lobby_id]

# Endpoint to list all lobbies
@app.route('/lobbies', methods=['GET'])
def list_lobbies():
    # Compile a list of available lobbies
    available_lobbies = {
        lobbyId: {
            "playerCount": len(lobby["players"]),
            "players": lobby["players"],
            "isFull": lobby.get('isFull', False)
        }
        for lobbyId, lobby in lobbies.items() if lobby['status'] == 'waiting'
    }
    return jsonify(available_lobbies)

if __name__ == '__main__':
    socketio.run(app, debug=True)
