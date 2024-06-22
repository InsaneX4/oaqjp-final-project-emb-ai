"""
Functions:
• em_detector: Analyse client request text for emotions.
• render_index_page: Render the homepage template.

Objects:
• app: A Flask which is an Emotion Detector application.
"""
#Task 6: 1. Create the server.py file from scratch.
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

#Task 6:
#2. Make sure that the Flask decorator for the application calling function is \emotionDetector.
@app.route("/emotionDetector")
def em_detector():
    """Analyse client request text for emotions
    and return a string including emotion scores and the dominant emotion."""
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    #Task 6: 3. Display the output in the specified format.
    #Task 7: 3. Incorporate error handling when the dominant_emotion is None.
    #In this scenario, the response should display a message Invalid text! Please try again!.
    dominant_emotion = response["dominant_emotion"]

    if dominant_emotion is None:
        output = "Invalid text! Please try again!"
    else:
        anger = response["anger"]
        disgust = response["disgust"]
        fear = response["fear"]
        joy = response["joy"]
        sadness = response["sadness"]

        output = "For the given statement, the system response is "
        output += f"'anger': {anger}, "
        output += f"'disgust': {disgust}, "
        output += f"'fear': {fear}, "
        output += f"'joy': {joy} and "
        output += f"'sadness': {sadness}. "
        output += f"The dominant emotion is {dominant_emotion}."
    return output

@app.route("/")
def render_index_page():
    """Render the homepage template and return a string which is its HTML."""
    return render_template('index.html')

#Task 6: 4. Application needs to be deployed on localhost:5000
if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000)