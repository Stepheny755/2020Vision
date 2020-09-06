#Checks for match between the correct answer and the answer given by the user
def checkMatch(correctAnswer, name):
    from stream_recognise import recogniseLetter
    uri = "gs://letter-clips/" + name

    givenAnswer = recogniseLetter(uri).upper()

    if givenAnswer == correctAnswer:
        return True
    else:
        return False

#Score dependent on what index of the tests the user fails at
def determineScore(letterIndex):
    if letterIndex == 0:
        return 0.0
    elif letterIndex > 0 and letterIndex < 3:
        return 0.1
    elif letterIndex >= 3 and letterIndex <6:
        return 0.2
    elif letterIndex >=6 and letterIndex < 10:
        return 0.28
    elif letterIndex >= 10 and letterIndex < 15:
        return 0.4
    elif letterIndex >= 15 and letterIndex < 21:
        return 0.5
    elif letterIndex >= 21 and letterIndex < 28:
        return 0.66
    elif letterIndex >= 28 and letterIndex < 36:
        return 0.8
    elif letterIndex >= 36 and letterIndex < 44:
        return 1.00
    elif letterIndex >= 44 and letterIndex < 52:
        return 1.33
    elif letterIndex >= 52 and letterIndex <61:
        return 1.54
    else:
        return 2.00

#Retuns names of all MP3 files currently in the bucket in an arrya 
def findItems():
    from google.cloud import storage
    
    itemList = []
    storageClient = storage.Client()
    blobs = storageClient.list_blobs("letter-clips")

    for blob in blobs:
        itemList.append(blob.name)

    return itemList


def runScoring():
    from google.cloud import storage


    itemList = findItems()
    testLetters = ["E", "F", "P", "T", "O", "Z", "L", "P", "E", "D", "P", "E", "C", "F", "D", "E", "D", "F", "C", "Z", "P",
                    "F", "E", "L", "O", "P", "Z", "D", "D", "E", "F", "P", "O", "T", "E", "C", "L", "E", "F", "O", "D", "P", "C", "T",
                    "F", "D", "P", "L", "T", "C", "E", "O", "P", "E", "Z", "O", "L", "C", "F", "T", "D"]

    currentIndex = 0
    maxIndex = 60
    itemNum = len(itemList)
    print("Itemnum: " + str(itemNum))

    for item in itemList:
        print("Current index is: " + str(currentIndex))
        if currentIndex == itemNum and currentIndex < maxIndex:
            break
        else:
            print("Item being checked: " + str(item))
            isMatch = checkMatch(testLetters[currentIndex], item)
            if isMatch:
                print("In continue")
                currentIndex = currentIndex+1
                continue
            else:
                print("In break")
                break

    return determineScore(currentIndex)



