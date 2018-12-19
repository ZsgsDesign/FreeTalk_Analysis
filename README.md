# FreeTalk_Analysis
This project is meant to analyze weekly free talks' topic and emotions based on Microsoft Cognitive Services.

## Install

modify `subscription_key.py` and add your own key, if you don't wanna track this file, simply type 

```
git update-index --skip-worktree .\subscription_key.py
```

in the console.

Also, the Speech To Text function require `azure-cognitiveservices-speech` to be installed, to do so, simply run command

```
python -m pip install azure-cognitiveservices-speech
```

or the appropriate command for your system.