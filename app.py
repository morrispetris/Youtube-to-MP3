from __future__ import unicode_literals
import youtube_dl
from flask import Flask, render_template, request, url_for, redirect, flash

app = Flask(__name__)
app.secret_key = "1234abcd"

#def downloadYT(link):
async def downloadYT(link):
    information = {
         #'format': 'bestaudio/best',
        'format': 'worst',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '64',
        }],
    }
    with youtube_dl.YoutubeDL(information) as music:
        music.download([link])

@app.route("/", methods=['POST', 'GET'])
def index():

    if request.method == "POST":

        try:
            #downloadYT(request.form['link'])
            downloadYT(request.form['link'])
            flash('COMPLETED!', 'done')
        except:
            flash('FAILED!', 'error')
        
        return redirect(url_for("index"))

    else:
        return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
