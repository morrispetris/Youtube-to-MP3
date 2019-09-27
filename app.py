from __future__ import unicode_literals
import youtube_dl
from flask import Flask, render_template, request, url_for, redirect, flash

app = Flask(__name__)
app.secret_key = "1234abcd"

def downloadYT(link):
    information = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(information) as music:
        music.download([link])

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)