import azure.cognitiveservices.speech as speechsdk
import time 
from subscription_key import speech_key

assert speech_key

audio_config = speechsdk.audio.AudioConfig(use_default_microphone=False,filename="freetalks/week 1/Q17010217.wav")

speech_config = speechsdk.SpeechConfig(subscription=speech_key, region="eastasia")

speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config,audio_config=audio_config)

# print("Say something...")

# Performs recognition. recognize_once() returns when the first utterance has been recognized,
# so it is suitable only for single shot recognition like command or query. For long-running
# recognition, use start_continuous_recognition() instead, or if you want to run recognition in a
# non-blocking manner, use recognize_once_async().

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
    ans+=e.result.text

def session_started_func(e):
    print("Session started event.")

def session_stopped_func(e):
    global proc
    print("Session ended event.")
    proc=False
    speech_recognizer.stop_continuous_recognition()
    print("[Finished] " + ans)

speech_recognizer.recognized.connect(recoged)
speech_recognizer.recognizing.connect(recog)
# speech_recognizer.canceled.connect(recog)
speech_recognizer.session_started.connect(session_started_func)
speech_recognizer.session_stopped.connect(session_stopped_func)

speech_recognizer.start_continuous_recognition()

while proc:
    time.sleep(1)
    continue

# ret=speechsdk.SpeechRecognitionResult.text.getter(ret)

# print(result)

# if result.reason == speechsdk.ResultReason.RecognizedSpeech:
#     print("Recognized: {}".format(result.text))
# elif result.reason == speechsdk.ResultReason.NoMatch:
#     print("No speech could be recognized: {}".format(result.no_match_details))
# elif result.reason == speechsdk.ResultReason.Canceled:
#     cancellation_details = result.cancellation_details
#     print("Speech Recognition canceled: {}".format(cancellation_details.reason))
#     if cancellation_details.reason == speechsdk.CancellationReason.Error:
#         print("Error details: {}".format(cancellation_details.error_details))