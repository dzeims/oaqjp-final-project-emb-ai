"""
Flask application for emotion detection.

This application provides a web interface for detecting emotions in text
using the EmotionDetection module.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector, emotion_predictor

app = Flask("Emotion Detection")

def run_emotion_detection():
    """Starts the Flask server for the Emotion Detection application."""
    app.run(host="0.0.0.0", port=5000)

@app.route("/emotionDetector")
def sent_detector():
    """
    Handles emotion detection requests.

    Retrieves text from query parameters, runs emotion detection, 
    and returns the formatted emotion response.
    """
    text_to_detect = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_detect)
    formated_response = emotion_predictor(response)
    if formated_response['dominant_emotion'] is None:
        return "Invalid text! Please try again."
    return (
        f"For the given statement, the system response is 'anger': {formated_response['anger']} "
        f"'disgust': {formated_response['disgust']}, 'fear': {formated_response['fear']}, "
        f"'joy': {formated_response['joy']} and 'sadness': {formated_response['sadness']}. "
        f"The dominant emotion is {formated_response['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    """
    Renders the index page for the application.
    """
    return render_template('index.html')

if __name__ == "__main__":
    run_emotion_detection()
