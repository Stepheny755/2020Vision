#Checks for match between the correct answer and the answer given by the user
def checkMatch(correctAnswer, uri):
    from stream_recognise import recogniseLetter

    givenAnswer = recogniseLetter(uri)

    if givenAnswer == correctAnswer:
        return true
    else:
        return false

#Score dependent on what index of the tests the user fails at
def determineScore(letterIndex):
    if letterIndex == 0:
        return 0.0
    else if letterIndex > 0 and letterIndex < 3:
        return 0.1
    else if letterIndex >= 3 and letterIndex <6:
        return 0.2
    else if letterIndex >=6 and letterIndex < 10:
        return 0.28
    else if letterIndex >= 10 and letterIndex < 15:
        return 0.4
    else if letterIndex >= 15 and letterIndex < 21:
        return 0.5
    else if letterIndex >= 21 and letterIndex < 28:
        return 0.66
    else if letterIndex >= 28 and letterIndex < 36:
        return 0.8
    else if letterIndex >= 36 and letterIndex < 44:
        return 1.00
    else if letterIndex >= 44 and letterIndex < 52:
        return 1.33
    else if letterIndex >= 52 and letterIndex <61:
        return 1.54
    else:
        return 2.00
