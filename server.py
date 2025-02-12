from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    return render_template('index.html')

@app.route("/emotionDetector")
def sent_analyzer():
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)
    dominant_emotion = response.pop("dominant_emotion", None)

    return "For the given statement, the system response is {} The dominant emotion is {}.".format(response, dominant_emotion)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)