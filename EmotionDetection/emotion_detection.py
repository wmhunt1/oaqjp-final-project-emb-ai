import json
import requests  # Import the requests library to handle HTTP requests

def emotion_detector(text_to_analyse):  # Define a function emotion_detector that takes a string input (text_to_analyse)
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }  # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers

    
    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
        disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
        fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
        joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
        sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']

        emotions =   {'anger':anger_score,
        'disgust':disgust_score,
        'fear':fear_score,
        "joy":joy_score,
        "sadness":sadness_score,
        }
        highest_emotion = max(emotions, key=emotions.get)
    
    elif response.status_code == 400:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        highest_emotion = None

  

    results =   {'anger':anger_score,
    'disgust':disgust_score,
     'fear':fear_score,
     "joy":joy_score,
     "sadness":sadness_score,
     "dominant_emotion":highest_emotion
     }
    return results
  
