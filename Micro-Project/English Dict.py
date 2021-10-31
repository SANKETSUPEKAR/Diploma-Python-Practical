def setIntro():
    print("Python Micro-Project".center(screenWidth))
    print("English Dictionary Application".center(screenWidth))
    print("- Name Of Students".rjust(screenWidth))
    print("1. Sanket Supekar".rjust(screenWidth))
    print("2. Swayam Borude ".rjust(screenWidth))
    print("3. Akash Bhagwat ".rjust(screenWidth))
    print("4. Dhiraj Kadam ".rjust(screenWidth))



def setOperation():
    print(" Types Of Operations -")
    print(" 1. Show Dictionary")
    print(" 2. Find Meaning Of Word")
    print(" 3. Add Word And Its Meaning ")
    print(" 4. Update Word OR Its Meaning")
    print(" 5. Delete Word And Its Meaning")
    print(" 6. Print List Of Word And Its Meaning")
    print(" 7. Exit")


def showDict():
    print("Available Word In Dictionary - \n")
    print("\n".join(list(dictData.keys())))


def findWord():
    inputWord = input("Enter Word :")
    word = inputWord.lower().capitalize()
    if word in dictData.keys():
        print("Meaning Of {0} : {1}".format(word, dictData.get(word)))
    else:
        print("Word Not Found In Dictionary")


def addWord():
    inputWord = input("Enter Word :")
    word = inputWord.lower().capitalize()
    inputMean = input("Enter Meaning Of Word : ")
    if word.isalpha():
        dictData[word] = inputMean
        print("Word Added Into Dictionary...")
    else:
        print("Invalid Word Please Enter Again")


def updateWord():
    inputWord = input("Enter Word Which You Want To Update :")
    word = inputWord.lower().capitalize()
    if word in dictData.keys():
        print("Meaning Of {0} : {1}".format(word, dictData.get(word)))
        print("Enter 0 For Update Word... \nEnter 1 For Update Its Meaning... ")
        num = int(input("Enter Choice : "))
        if num == 1 or num == 0:
            if num == 0:
                inputWordUpdate = input("Enter Word :")
                wordUpdate = inputWordUpdate.lower().capitalize()
                if wordUpdate.isalpha():
                    temp = dictData[word]
                    del dictData[word]
                    dictData[wordUpdate] = temp
                    print("Word Updated Into Dictionary...")
                else:
                    print("Invalid Word Please Enter Again")
            elif num == 1:
                inputMeanUpdate = input("Enter Meaning :")
                dictData[word] = inputMeanUpdate
                print("Meaning Updated Into Dictionary...")
    else:
        print("Word Not Found In Dictionary")


def deleteWord():
    inputWord = input("Enter Word Which You Want To Delete :")
    word = inputWord.lower().capitalize()
    if word in dictData.keys():
        print("Meaning Of {0} : {1}".format(word, dictData.get(word)))
        del dictData[word]
        print("Word Deleted From Dictionary")
    else:
        print("Word Not Found In Dictionary")


def printDict():
    print("Print Dictionary \n")
    for x, y in dictData.items():
        print(x, " - ", y)


# Start
screenWidth = 100
operationNumber = 0
dictData = {"Entitlements": "Having a right to something",
            "Allegedly": "Something claimed Without any proof.",
            "Exaggerate": "Saying something beyond the limits.",
            "Downpour": "Heavy rain",
            "Possession": "Keeping in hold or control.",
            "Sovereignty": "Power or authority.",
            "Underpin": "Underpin is a verb that means support from the base",
            "Influence": "The capability of putting an effect on something/somewhere.",
            "Revamp": "Rebuild something or repair something.",
            "Liberty": "Liberty is a noun which means personal freedom from oppression"}
setIntro()
setOperation()
while operationNumber != 7:
    try:
        operationNumber = int(input("\nEnter Operation Number : "))
    except Exception as e:
        print(" Invalid Operation Number..\n Please Try Again..")
        continue

    if operationNumber == 1:
        showDict()
    elif operationNumber == 2:
        findWord()
    elif operationNumber == 3:
        addWord()
    elif operationNumber == 4:
        updateWord()
    elif operationNumber == 5:
        deleteWord()
    elif operationNumber == 6:
        printDict()
    elif operationNumber == 7:
        print("Exit..........")
    else:
        print(" Invalid Operation Number..\n Please Try Again..")
