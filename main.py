import requests
from pprint import pprint
from IPython.display import HTML
from colorama import Fore, Back, Style
from subscription_key import text_analytics_key
import azure.cognitiveservices.speech as speechsdk
import time 
import MySQLdb
from subscription_key import speech_key

# Speech2Text

assert speech_key

audio_config = speechsdk.audio.AudioConfig(use_default_microphone=False,filename="freetalks/week 1/Q17010217.wav")
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region="eastasia")
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config,audio_config=audio_config)

proc=True
dots=1
ans=""

def recog(e):
    global dots
    str_temp="Proceeding"
    for num in range(1,dots):
        str_temp+="."
    print(str_temp)
    dots+=1

def recoged(e):
    global dots,ans
    print("[Finished Sentence] " + e.result.text)
    dots=1
    ans+=e.result.text.strip()+" "

def session_started_func(e):
    print("Session started event.")

def session_stopped_func(e):
    global proc
    print("Session ended event.")
    proc=False
    speech_recognizer.stop_continuous_recognition()
    print("[Finished] " + ans)

def failed(e):
    print("[Canceled]")

speech_recognizer.recognized.connect(recoged)
speech_recognizer.recognizing.connect(recog)
speech_recognizer.canceled.connect(failed)
speech_recognizer.session_started.connect(session_started_func)
speech_recognizer.session_stopped.connect(session_stopped_func)

speech_recognizer.start_continuous_recognition()

while proc:
    time.sleep(1)
    continue

print("")

# Text-Anal

subscription_key = text_analytics_key
assert subscription_key
text_analytics_base_url = "https://eastasia.api.cognitive.microsoft.com/text/analytics/v2.0/"

sentiment_api_url = text_analytics_base_url + "sentiment"
keyphrases_api_url = text_analytics_base_url + "keyPhrases"

documents = {
    'documents': [
        {
            'id': '1',
            'language': 'en',
            'text': ans
        }
    ]
}

headers   = {"Ocp-Apim-Subscription-Key": subscription_key}
sentiment_response  = requests.post(sentiment_api_url, headers=headers, json=documents)
keyphrases_response  = requests.post(keyphrases_api_url, headers=headers, json=documents)
sentiment_json = sentiment_response.json()
keyphrases_json = keyphrases_response.json()

sentiment_score  = sentiment_json["documents"][0]["score"]
keyphrases_array  = keyphrases_json["documents"][0]["keyPhrases"]
print("[Emotion: {score:.2f}]".format(score=sentiment_score))

for key_item in keyphrases_array:
    print(key_item)