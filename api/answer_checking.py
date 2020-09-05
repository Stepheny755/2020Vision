def checkMatch(correctAnswer, uri):
    from stream_recognise import recogniseLetter

    givenAnswer = recogniseLetter(uri)

    if givenAnswer == correctAnswer:
        return true
    else:
        return false

