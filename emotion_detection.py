import requests

def emotion_detector(text_to_analyse):
    url= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    obj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = obj, headers=header)
    return response.text

#from emotion_detection import emotion_detecto
#emotion_detector("I love this new technology.")