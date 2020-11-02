from flask import Flask, redirect, url_for, render_template, request, send_file, jsonify
from datetime import datetime
import translate, sentiment, synthesize

app = Flask(__name__)
app.config['JSON_ASCII'] = False

@app.route('/')
def home():
    return render_template("home.html",  content='there', Year=datetime.now().year)

@app.route('/admin/')
def admin():
    return redirect(url_for("user", name='jmo.py'))

@app.route('/ts&a/')
def index():
    return render_template('ts&a.html')

@app.route('/translate-text/', methods=['POST'])
def translate_text():
    data = request.get_json()
    text_input = data['text']
    translation_output = data['to']
    response = translate.get_translation(text_input, translation_output)
    return jsonify(response)

@app.route('/sentiment-analysis/', methods=['POST'])
def sentiment_analysis():
    data = request.get_json()
    input_text = data['inputText']
    input_lang = data['inputLanguage']
    output_text = data['outputText']
    output_lang =  data['outputLanguage']
    response = sentiment.get_sentiment(input_text, input_lang, output_text, output_lang)
    return jsonify(response)

@app.route('/text-to-speech', methods=['POST'])
def text_to_speech():
    data = request.get_json()
    text_input = data['text']
    voice_font = data['voice']
    tts = synthesize.TextToSpeech(text_input, voice_font)
    tts.get_token()
    audio_response = tts.save_audio()
    return audio_response

@app.route('/<name>/')
def user(name):
    return render_template("home.html", content=name)



if __name__ == '__main__':
    app.run(debug=True)
