from helpers.getVerseTextFromUrl import getVerseTextFromUrl

def createSolutionObject(reference, url, verseText):
    solutionObject = {
        "reference": reference.upper(),
        "referenceURL" : url,
        "verseText": verseText
    }

    return solutionObject