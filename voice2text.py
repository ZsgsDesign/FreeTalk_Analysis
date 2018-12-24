import azure.cognitiveservices.speech as speechsdk
import time 
from subscription_key import speech_key

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