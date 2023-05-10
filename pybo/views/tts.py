from flask import Flask, render_template, request, jsonify, Blueprint
from gtts import gTTS
import os
import pygame
import uuid

bp = Blueprint('tts', __name__, url_prefix = '/diary')


MAX_MP3_FILES = 3  # 최대 유지할 mp3 파일 수
MP3_FOLDER = 'static'  # mp3 파일이 저장될 폴더 이름

app = Flask(__name__)
# pygame.mixer.init()

@app.route('/create/', methods=['POST'])
def tts():
    data = request.get_json()
    text = data['text']
    lang = data.get('lang', 'en')
    filename = f'{MP3_FOLDER}/temp_{uuid.uuid4()}.mp3'

    tts = gTTS(text=text, lang=lang)
    tts.save(filename)

    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


    # mp3_folder 에서 MAX_MP3_FILES = 3 개가 넘으면 파일을 삭제하는 코드
    # 폴더 경량화를 위해
    mp3_files = sorted(os.listdir(MP3_FOLDER), key=lambda f: os.path.getctime(os.path.join(MP3_FOLDER, f)))
    if len(mp3_files) > MAX_MP3_FILES:
        for file in mp3_files[:len(mp3_files) - MAX_MP3_FILES]:
            if file.endswith('.mp3'):
                os.remove(os.path.join(MP3_FOLDER, file))

    # Return success status
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True)