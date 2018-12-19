import azure.cognitiveservices.speech as speechsdk
from subscription_key import speech_key 

assert speech_key

speech_config = speechsdk.SpeechConfig(subscription=speech_key, region="eastasia")

speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

print("Say something...")

# Performs recognition. recognize_once() returns when the first utterance has been recognized,
# so it is suitable only for single shot recognition like command or query. For long-running
# recognition, use start_continuous_recognition() instead, or if you want to run recognition in a
# non-blocking manner, use recognize_once_async().
result = speech_recognizer.recognize_once()

if result.reason == speechsdk.ResultReason.RecognizedSpeech:
    print("Recognized: {}".format(result.text))
elif result.reason == speechsdk.ResultReason.NoMatch:
    print("No speech could be recognized: {}".format(result.no_match_details))
elif result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = result.cancellation_details
    print("Speech Recognition canceled: {}".format(cancellation_details.reason))
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        print("Error details: {}".format(cancellation_details.error_details))