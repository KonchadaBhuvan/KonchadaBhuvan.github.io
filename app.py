from flask import Flask, render_template, request
from pymongo import MongoClient
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
uri = "mongodb+srv://konchadabhuvan22csm:<root>@cluster0.to0pp1g.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

app = Flask(__name__)

db = client["mood_playlist_db"]
collection = db["playlists"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/playlist', methods=['POST'])
def show_playlist():
    mood = request.form['mood']
    playlist = collection.find_one({'mood': mood})
    songs = playlist['songs'] if playlist else []
    return render_template('playlist.html', mood=mood, songs=songs)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
