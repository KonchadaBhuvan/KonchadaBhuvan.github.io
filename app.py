from flask import Flask, render_template, request
from pymongo import MongoClient
import os
app = Flask(__name__)

# Connect to local MongoDB
uri = "mongodb+srv://konchadabhuvan22csm:<root>@cluster0.to0pp1g.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(os.environ.get("MONGODB_URI"))
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
    app.run(debug=True)
