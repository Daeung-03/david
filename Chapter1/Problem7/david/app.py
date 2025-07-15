from flask import Flask, request, Response, render_template
import os
from io import BytesIO
from gtts import gTTS
from langdetect import detect
import base64

DEFAULT_LANG = 'ko'
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')
    

@app.route("/useruse", methods = ['GET', 'POST'])
def ask():
    error = None
    audio = None
    download_url = None
    if request.method == "GET":
        return render_template('index.html', error=error, audio = None, download_url = None)
    else:
        user_text = request.form['input_text']
        user_lang = request.form['lang']
        audio_path = os.path.join('static', 'audio')
        file_name = "generated_audio.mp3"
        file_path = '/home/eodnd74/Documents/working_daeung03/Codyssey/Chapter1/Problem7/david/static/audio/' + file_name


        try:
            detected_lang = detect(user_text)
            if user_lang != detected_lang:
                raise Exception("사용한 언어가 일치하지 않습니다.")
            
            fp = BytesIO()
            tts = gTTS(user_text, "com", user_lang)
            tts.write_to_fp(fp)
            tts.save(file_path)
            download_url = '/static/audio/' + file_name

            audio_data = fp.getvalue()
            audio = base64.b64encode(audio_data).decode('utf-8')
        
            return render_template('index.html', error=error, audio = audio, download_url = download_url)
        
        except Exception as e:
            error = f"오류 발생: {e}"
            return render_template('index.html', error=error, audio = None, download_url = download_url)

if __name__ == '__main__':
    app.run('0.0.0.0', 5000, debug = True)
