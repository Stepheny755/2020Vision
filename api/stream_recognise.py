
def recogniseLetter(uri):

    from google.cloud import speech_v1p1beta1
    from google.cloud.speech_v1p1beta1 import enums

    client = speech_v1p1beta1.SpeechClient()
    storageURI = uri
    storageURI='gs://letter-clips/PMP3.mp3'


    encoding = enums.RecognitionConfig.AudioEncoding.MP3
    languageCode = "en-US"
    sampleRate = 48000
    speechContexts = [{"phrases": ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
                                   "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"],
                        "boost": 15}]
    config = {
       "speech_contexts": speechContexts,
       "sample_rate_hertz": sampleRate,
       "language_code": languageCode,
       "encoding": encoding,
        }

    audio = {"uri": storageURI}

    response = client.recognize(config=config, audio=audio)


    for result in response.results:
        alternative = result.alternatives[0]
        return alternative.transcript
