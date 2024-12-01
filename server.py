"""
Final Project
"""
from flask import Flask, render_template, request
from EmotionDetection import emotion_detector
app = Flask("Emotion Detection")
@app.route("/emotionDetector")
def detect_emotion():
    """
    Emotion detection function
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    label = response['dominant_emotion']
    if label is None:
        return "Invalid text! Please try again!."
    score = response[label]
    return f"The given text has been identified as {label} with a score of {score}."

@app.route("/")
def render_index_page():
    """
    Root function
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
