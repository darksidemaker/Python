from flask import Flask, send_file

app = Flask(__name__)

@app.route('/stream_audio')
def stream_audio():
    # Replace 'audio_file_path' with the path to your audio file
    audio_file_path = '/workspaces/Python/YTMusic/mp3file/Daku.mp3'
    return send_file(audio_file_path, mimetype='audio/mp3', as_attachment=False)

if __name__ == '__main__':
    app.run(debug=True)