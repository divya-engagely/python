import azure.cognitiveservices.speech as speechsdk

TESTCASES = [
  {
    'filename': 'audio.wav',
    'encoding': 'LINEAR16',
    'lang': 'en-US'
  }
]

AZURE_SPEECH_KEY = 'f8e041adcbb54410b492e093dc4b21d1'
AZURE_SERVICE_REGION = 'centralindia'

def azure_batch_stt(filename, lang, encoding):
    speech_config = speechsdk.SpeechConfig(
        subscription=AZURE_SPEECH_KEY,
        region=AZURE_SERVICE_REGION
    )
    audio_input = speechsdk.AudioConfig(filename=filename)
    speech_recognizer = speechsdk.SpeechRecognizer(
        speech_config=speech_config,
        audio_config=audio_input
    )
    result = speech_recognizer.recognize_once()

    return result.text if result.reason == speechsdk.ResultReason.RecognizedSpeech else None

# Run tests
for t in TESTCASES:
    execut = azure_batch_stt(t['filename'], t['lang'], t['encoding'])
    print(execut)
    



