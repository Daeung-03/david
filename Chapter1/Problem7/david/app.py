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
    if request.method == "GET":
        return render_template('index.html', error=error, audio = None)
    else:
        user_text = request.form['input_text']
        user_lang = request.form['lang']

        try:
            detected_lang = detect(user_text)
            if user_lang != detected_lang:
                raise Exception("사용한 언어가 일치하지 않습니다.")
            
            fp = BytesIO()
            gTTS(user_text, "com", user_lang).write_to_fp(fp)

            audio_data = fp.getvalue()
            audio = base64.b64encode(audio_data).decode('utf-8')
    
            return render_template('index.html', error=error, audio = audio)
        except Exception as e:
            error = f"오류 발생: {e}"
            return render_template('index.html', error=error, audio = audio)

if __name__ == '__main__':
    app.run('0.0.0.0', 5000, debug = True)
