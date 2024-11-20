import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = {"raw_document": {"text": text_to_analyse}}
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    response = requests.post(url, json=myobj, headers=header)
    formatted_response = json.loads(response.text)

    if response.status_code == 200:
        return formatted_response
    elif response.status_code == 400:
        formatted_response = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None,
        }
        return formatted_response

def emotion_predictor(detected_text):
    if isinstance(detected_text, dict) and all(value is None for value in detected_text.values()):
        return detected_text

    if 'emotionPredictions' in detected_text and detected_text['emotionPredictions']:
        emotions = detected_text['emotionPredictions'][0]['emotion']
        anger = emotions['anger']
        disgust = emotions['disgust']
        fear = emotions['fear']
        joy = emotions['joy']
        sadness = emotions['sadness']
        max_emotion = max(emotions, key=emotions.get)

        formatted_dict_emotions = {
            'anger': anger,
            'disgust': disgust,
            'fear': fear,
            'joy': joy,
            'sadness': sadness,
            'dominant_emotion': max_emotion,
        }
        return formatted_dict_emotions

    return {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}

# Input statement
text = "I hate working long hours"

# Step 1: Detect emotions
detected_text = emotion_detector(text)

# Step 2: Predict emotions
predicted_emotions = emotion_predictor(detected_text)

# Step 3: Verify if the dominant emotion is 'joy'
#if predicted_emotions.get('dominant_emotion') == 'joy':
    #print("'joy'")
#else:
    #print(f"The dominant emotion is '{predicted_emotions.get('dominant_emotion')}'.")

# Step 4: Output the emotion details
#print(predicted_emotions)
