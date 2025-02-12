"""
    server.py -A simple web server made with Flask
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    """
    Renders the index.html template
    """
    return render_template('index.html')

@app.route("/emotionDetector")
def sent_analyzer():
    """
    The text analyzing action!
    """
    text_to_analyze = request.args.get('textToAnalyze')

    res = emotion_detector(text_to_analyze)
    dom_e = res.pop("dominant_emotion", None)

    return f"For the given statement, the system response is {res} The dominant emotion is {dom_e}."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
