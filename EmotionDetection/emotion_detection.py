import requests
import json

def emotion_detector(text):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text } }
    response = requests.post(url, headers=headers, json=myobj)

    formatted_response = json.loads(response.text)
    emotion_path = formatted_response['emotionPredictions'][0]['emotion']

    max_key = max(emotion_path, key=emotion_path.get)

    result = {
        'anger': emotion_path['anger'],
        'disgust': emotion_path['disgust'],
        'fear': emotion_path['fear'],
        'joy': emotion_path['joy'],
        'sadness': emotion_path['sadness'],
        'dominant_emotion': max_key
    }

    return result

print(emotion_detector("I am so happy I am doing this"))