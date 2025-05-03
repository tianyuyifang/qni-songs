from flask import Flask, render_template, request
from utils.helpers import load_song_data, pinyin_filter
import copy
import pandas as pd
from pypinyin import pinyin, Style

app = Flask(__name__)

app.template_filter('pinyin')(pinyin_filter)


@app.route('/')
def search_page():
    songs = load_song_data()
    artists = sorted({song['artist'] for song in songs})
    return render_template('search.html', artists=artists)


@app.route('/songs')
def songs_list():
    artist = request.args.get('artist', '').lower()
    songs = load_song_data()

    if artist:
        filtered_songs = [copy.deepcopy(song) for song in songs if artist in song['artist'].lower()]
    else:
        filtered_songs = songs

    return render_template('songs.html',
                           songs=filtered_songs,
                           page_title=f"{artist}的歌P")


if __name__ == '__main__':
    app.run(debug=True)