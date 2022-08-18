import os
import random

def main():

	for file in os.listdir('.'):

		filename, fileExtension = os.path.splitext(file)

		if fileExtension == '.txt':

			with open(file) as f:
				fileContentList = f.readlines()

			firstListItem = fileContentList[0].strip('\n')

			choiceList = []

			if firstListItem.isdigit():

				requiredChoiceCount = int(firstListItem)

				while len(choiceList) < requiredChoiceCount:

					randomChoice = random.choices(fileContentList)[0].strip('\n')

					if randomChoice != firstListItem and randomChoice not in choiceList:

						choiceList.append(randomChoice)
	
			else:

				choiceList.append(random.choices(fileContentList)[0].strip('\n'))

			print("{0}: {1}".format(filename, ', '.join(choiceList)))

if __name__ == "__main__":

	main()
