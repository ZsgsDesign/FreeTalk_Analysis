import requests
from pprint import pprint
from IPython.display import HTML
from colorama import Fore, Back, Style
from subscription_key import text_analytics_key 

subscription_key = text_analytics_key
assert subscription_key
text_analytics_base_url = "https://eastasia.api.cognitive.microsoft.com/text/analytics/v2.0/"

sentiment_api_url = text_analytics_base_url + "sentiment"
print(sentiment_api_url)

documents = {
    'documents': [
        {
            'id': '1',
            'language': 'en',
            'text': 'I had a wonderful experience! The rooms were wonderful and the staff was helpful.'
        }
    ]
}

headers   = {"Ocp-Apim-Subscription-Key": subscription_key}
response  = requests.post(sentiment_api_url, headers=headers, json=documents)
languages = response.json()
# pprint(languages)

table = []
for document in languages["documents"]:
    text  = next(filter(lambda d: d["id"] == document["id"], documents["documents"]))["text"]
    score  = document["score"]
    print("[Emotion: {score:.2f}] {text}".format(score=score,text=text))

