import datetime
import random
import json

from helpers.generateUrl import generateUrl
from helpers.getVerseTextFromUrl import getVerseTextFromUrl
from helpers.createSolutionObject import createSolutionObject

from reference_lists.referenceList import referenceList
from reference_lists.newSolutionsList import newSolutionsList

def generateSolutionsFromFile():
    updatedList = []

    for reference in newSolutionsList:
        url = generateUrl(reference)
        verseText = getVerseTextFromUrl(url)
        solution = createSolutionObject(reference, url, verseText)
        updatedList.append(solution)

    # Uncomment to randomly shuffle order of final solution list
    # random.shuffle(updatedList)

    now = datetime.datetime.now()
    time = str(now).replace(" ", "-")
    fileName = f"newReferenceList-{time}.json"
    
    with open(fileName, 'w') as final:
        json.dump(updatedList, final)
    
    return fileName

def generateSingleSolution(reference):
    url = generateUrl(reference)
    verseText = getVerseTextFromUrl(url)
    return createSolutionObject(reference, url, verseText)

if __name__ == "__main__":
    isFinished = False

    while isFinished != True:
        isSingleSolution = input("Create a single solution? (Y/N):\n")

        if isSingleSolution == "Y":
            reference = input("Enter a Bible reference:\n")            
            solution = generateSingleSolution(reference)
            print(solution)
            isFinished = True
        
        if isSingleSolution == "N":
            fileName = generateSolutionsFromFile()
            print(f"Done! Open {fileName} to see the results!")
            isFinished = True
        
        if isFinished != True:
            print("Please enter Y or N!")