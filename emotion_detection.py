import requests
import json

def emotion_detector(text_to_analyse):
    url= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    obj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = obj, headers=header)
    return json.loads(response.text)

#from emotion_detection import emotion_detector
#emotion_detector("I love this new technology.")