
def emotion_detector(text_to_analyse):
    url= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    obj = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, json = obj, headers=header)
    response_json = json.loads(response.text)

    # find dominant emotion
    dominant_emotion = None
    value_prev = 0.0
    emotions = response_json['emotionPredictions'][0]['emotion']
    for emotion, value in emotions.items():
        if value_prev <= value:
            dominant_emotion = emotion
        else:
            pass
        value_prev = value
    emotions["dominant_emotion"] = dominant_emotion

    return emotions

#from emotion_detection import emotion_detector
#emotion_detector("I love this new technology.")