from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

# Connect to local MongoDB
client = MongoClient("mongodb://localhost:27017/")
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
