from flask import Flask, request, Response, render_template
import os
from io import BytesIO
from gtts import gTTS
from langdetect import detect
import base64

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
        return render_template('index.html', error=error, audio = None, download_url = None) #get요청에 의한 폼 페이지
    else:
        user_text = request.form['input_text']
        user_lang = request.form['lang']
        file_name = "generated_audio.mp3"
        file_path = '/home/eodnd74/Documents/working_daeung03/Codyssey/Chapter1/Problem7/david/static/audio/' + file_name #동적인 변수들 설정

        try:
            detected_lang = detect(user_text)
            if user_lang != detected_lang:
                raise Exception("사용한 언어가 일치하지 않습니다.") #gTTS에서 억양만 바꿔서 출력하는 경우 예외처리
            
            
            tts = gTTS(user_text, "com", user_lang)
            tts.save(file_path)
            download_url = '/static/audio/' + file_name #서버에 파일저장, 다운로드 url 생성

            fp = BytesIO()
            tts.write_to_fp(fp)
            audio_data = fp.getvalue()
            audio = base64.b64encode(audio_data).decode('utf-8') #출력할 audio 변수 생성
        
            return render_template('index.html', error=error, audio = audio, download_url = download_url) #페이지 출력
        
        except Exception as e:
            error = f"오류 발생: {e}"
            return render_template('index.html', error=error, audio = None, download_url = download_url) #오류 발생 페이지 출력

if __name__ == '__main__':
    app.run('0.0.0.0', 5000, debug = True)
