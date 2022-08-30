import os
import random
from tabnanny import filename_only

def main():

    print("\n Atomic Shrimp: Chance Cube Cuisine Challenge\n ============================================\n")

    dirFiles = []
    maxLenOfFilename = 0

    for file in os.listdir('.'):

        filename, fileExtension = os.path.splitext(file)

        if fileExtension == '.txt':

            dirFiles.append(file)

            lenOfFilename = len(filename)

            if lenOfFilename > maxLenOfFilename:

                maxLenOfFilename = lenOfFilename

    if len(dirFiles) > 0:

        for file in dirFiles:

            filename, fileExtension = os.path.splitext(file)

            with open(file) as f:

                fileContentList = f.readlines()

            firstListItem = fileContentList[0].strip('\n')

            choiceList = []

            if firstListItem.isdigit():

                requiredChoiceCount = int(firstListItem)

                if requiredChoiceCount <= len(fileContentList):

                    while len(choiceList) < requiredChoiceCount:

                        randomChoice = random.choices(fileContentList)[0].strip('\n')

                        if randomChoice != firstListItem and randomChoice not in choiceList:

                            choiceList.append(randomChoice)

                else:

                    choiceList.append(" Error: Required Choice Count ({0}) > Choices ({1})".format(requiredChoiceCount, len(fileContentList)))

            else:

                choiceList.append(random.choices(fileContentList)[0].strip('\n'))

            print(" {0:}{1} : {2}".format(filename, (maxLenOfFilename - len(filename)) * ' ', ', '.join(choiceList)))

    else:

        print(" Error: No choice files available...")
            
    print()

if __name__ == "__main__":

    main()
