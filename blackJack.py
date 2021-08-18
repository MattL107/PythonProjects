# blackJack.py

# this program builds upon blackJackSingle.py by looping the majority of the program
# to allow the user to play multiple games
# we will save their points total to a separate file and read the file in so they
# can pick up where they left off. Or, alternatively, they can choose to start
# a new game, with the point total reset to its default value.
# maybe add a savedGames folder so that the user can load old saves, or overwrite
# stuff (bit of a tangent, but would be nice to practice)

import random
import re
import time
import os
import shelve
import copy

os.chdir('C:\\Users\\matti\\Documents\\Work\\Computing\\Fun_projects\\playingCards\\blackJack')

# creating list of card numbers and suits

suits = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
numbers = [2,3,4,5,6,7,8,9,10, 'Jack', 'Queen', 'King', 'Ace']
deck = []


# creating the 4 lists of suits and the overall deck

for suit in suits:
    for number in numbers:
        deck.append(str(number) + ' of ' + suit)
        

# defining functions to check score of hand and whether someone is bust

def bustChecker(hand):
    handScore = 0
    for card in hand:
        for picture in ['Jack', 'Queen', 'King']:
            if picture in card:
                handScore += 10
        if 'Ace' in card:
            handScore += 1
        cardRegex = re.compile(r"\d+")
        numberCard = cardRegex.findall(card)
        if len(numberCard) == 1:
            handScore += int(numberCard[0])
    if handScore >= 22:
        bust = True
    else:
        bust = False
    handScore = 0
    return bust

def HandScore(hand):
    handscore = 0
    for card in hand:
        for picture in ['Jack', 'Queen', 'King']:
            if picture in card:
                handscore += 10
        if 'Ace' in card:
            handscore += 1
        cardRegex = re.compile(r"\d+")
        numberCard = cardRegex.findall(card)
        if len(numberCard) == 1:
            handscore += int(numberCard[0])
    for card in hand:
        if handscore <= 11 and 'Ace' in card:
            handscore += 10
    return handscore

# block of code for handling saveGames and userPoints courtesy of gameLoader.py

def naturalSort(List):
    numberRegex = re.compile(r'\d+')
    misorderedNumberList = []
    for filename in List:
        numberString = numberRegex.findall(f"{filename}")
        misorderedNumberList.append(numberString[0])
    for i in range(len(misorderedNumberList)):
        misorderedNumberList[i] = int(misorderedNumberList[i])
    copiedNumberList = copy.deepcopy(misorderedNumberList)
    copiedNumberList.sort()
    orderedList = [0]*len(copiedNumberList)
    for number in misorderedNumberList:
        correctIndex = copiedNumberList.index(number)
        orderedList[correctIndex] = f"points{number}.txt"
    return orderedList

def printSaveFiles():
    pointScores = []
    fileNames = naturalSort(os.listdir('points')) # make a list of the filenames
    for filename in fileNames: # make a list of the pointscore associated with each file
        fileInfo = open(f"points\\{filename}")
        pointScore = fileInfo.read()
        fileInfo.close()
        pointScores.append(pointScore)
    leftwidth = len(fileNames[len(fileNames)-1]) # remember that the .txt is missing
    leftwidth = max([leftwidth, len('File Name:')+3])
    lengthsListR = []
    for score in pointScores:
        lenScore = len(score)
        lengthsListR.append(lenScore)
    rightwidth = max(lengthsListR) + 3
    rightwidth = max([rightwidth, len('Points:')])
    print('Save Files'.center(leftwidth + rightwidth, '-'))
    print('File Name:'.ljust(leftwidth) + 'Points:'.rjust(rightwidth))
    for i in range(len(fileNames)):
        print(fileNames[i][:len(fileNames[i])-4].ljust(leftwidth) + pointScores[i].rjust(rightwidth))

pointScores = []
fileNames = naturalSort(os.listdir('points')) # make a list of the filenames
for filename in fileNames: # make a list of the pointscore associated with each file
    fileInfo = open(f"points\\{filename}")
    pointScore = fileInfo.read()
    fileInfo.close()
    pointScores.append(pointScore)

while True:
    userI = input('Press n to start a new game. Press s to load up an old save: ')
    time.sleep(1)
    if userI == 'n':
        #numFiles = len(os.listdir('points'))
        checkList = list(range(1,len(os.listdir('points'))+2))
        numberRegex = re.compile(r'\d+')
        misorderedNumberList = []
        for filename in os.listdir('points'):
            numberString = numberRegex.findall(f"{filename}")
            misorderedNumberList.append(numberString[0])
        for i in range(len(misorderedNumberList)):
            misorderedNumberList[i] = int(misorderedNumberList[i])
        for i in misorderedNumberList:
            if i in checkList:
                checkList.remove(i)
        #
        pointsFile = open(f"points\\points{checkList[0]}.txt", 'w')
        pointsFile.write('100')
        pointsFile.close()
        print('New game: points = 100')
        ActiveFile = f"points{checkList[0]}.txt"
        break
    elif userI == 's':
        printSaveFiles()
        time.sleep(1)
        while True:
            userI = input('Enter the name of a Save File to select it: ')
            time.sleep(1)
            fileNames = naturalSort(os.listdir('points'))
            displayedFileNames = copy.deepcopy(fileNames)
            for i in range(len(displayedFileNames)):
                displayedFileNames[i] = displayedFileNames[i][:len(displayedFileNames[i])-4]
            if userI in displayedFileNames:
                print(f"Loading saved game: {userI}. Points = {pointScores[displayedFileNames.index(userI)]}")
                ActiveFile = f"{userI}.txt"
                break
            else:
                print('File does not exist.')
                time.sleep(1)
        break
    else:
        print('Invalid input')
        time.sleep(1)
        continue

# the main loop where the game is played by the user

userContinue = True

while userContinue:

    ActiveFileOpen = open(f"points\\{ActiveFile}")
    points = int(ActiveFileOpen.read())
    ActiveFileOpen.close()

    while True:
        userBet = (input('Place your bet: '))
        try:
            if int(userBet) % 1 == 0 and int(userBet) > 0 and int(userBet) <= points:
                break # the userBet is valid, and we can reference this variable later in the code
            elif int(userBet) % 1 == 0 and int(userBet) > 0 and int(userBet) > points:
                print('You do not have enough points')
        except ValueError:
            print('Invalid input')
    userBet = int(userBet)
    playerHand = []

    time.sleep(0.5)

    playerHand.append(random.choice(deck))
    deck.remove(playerHand[0])
    playerHand.append(random.choice(deck))
    deck.remove(playerHand[1])
    print(f"Your hand is '{playerHand[0]}', '{playerHand[1]}'")
    time.sleep(1.2)

    handScore = 0

    while True:
        userI = input('Press y to draw. Press n to hold: ')
        if userI == 'y':
            time.sleep(1)
            playerHand.append(random.choice(deck))
            deck.remove(playerHand[len(playerHand)-1])
            print(f"You have drawn: {playerHand[len(playerHand)-1]}")
            time.sleep(2.5)
            print('(playerHand: ', end='')
            for i in range(len(playerHand)-1):
                print(f"'{playerHand[i]}', ", end='')
            print(f"'{playerHand[len(playerHand)-1]}')")
        elif userI == 'n':
            print()
            break
            
        else:
            print('Invalid input')
            continue
        bustStatus = bustChecker(playerHand)
        time.sleep(1)
        if bustStatus:
            print('You have gone bust!\n')
            break

    # a loop where the dealer plays, and we show the process to the user

    time.sleep(2)

    print('The dealer is now playing...')

    time.sleep(2)

    dealerHand = []

    dealerHand.append(random.choice(deck))
    deck.remove(dealerHand[0])
    dealerHand.append(random.choice(deck))
    deck.remove(dealerHand[1])
    print(f"The dealer's hand is '{dealerHand[0]}', '{dealerHand[1]}'\n")
    time.sleep(1.2)

    while HandScore(dealerHand) < 17:
        time.sleep(1)
        dealerHand.append(random.choice(deck))
        deck.remove(dealerHand[len(dealerHand)-1])
        print(f"The dealer has drawn: {dealerHand[len(dealerHand)-1]}")
        time.sleep(2.5)
        print('(dealerHand: ', end='')
        for i in range(len(dealerHand)-1):
            print(f"'{dealerHand[i]}', ", end='')
        print(f"'{dealerHand[len(dealerHand)-1]}')")
        bustStatus = bustChecker(dealerHand)
        time.sleep(1)
        if bustStatus:
            print('The dealer has gone bust!\n')
            time.sleep(1)
            break

    playerScore = HandScore(playerHand)
    dealerScore = HandScore(dealerHand)

    if dealerScore <= 21:
        print('The dealer is holding')
        time.sleep(1)
        print(f"The dealer's hand is worth {HandScore(dealerHand)}")
        time.sleep(1)

    if playerScore <= 21:
        print(f"Your hand was worth: {HandScore(playerHand)}")
        time.sleep(1)

    # settlement

    if dealerScore > 21:
        if playerScore <= 21:
            print("You win!")
            points += userBet
        else:
            print("You lose!")
            points -= userBet

    else:
        if playerScore <= 21 and playerScore > dealerScore:
            print("You win!")
            points += userBet
        if playerScore == dealerScore:
            print("It's a tie!")
            points += 0
        if dealerScore > playerScore:
            print("You lose!")
            points -= userBet
        if playerScore > 21:
            print("You lose!")
            points -= userBet

    print(f"You now have {points} points")
    time.sleep(1)

    ActiveFileWrite = open(f"points\\{ActiveFile}", 'w')
    ActiveFileWrite.write(str(points))
    ActiveFileWrite.close()

    if points == 0:
        # code to end the program and delete the save file
        print('Bad luck! You are out of points!')
        os.unlink(f"points\\{ActiveFile}")
        userContinue = False
    else:
        while True:
            userPlaying = input('Press y to play again, press n to save and exit')
            if userPlaying == 'y':
                userContinue = True
                break
            if userPlaying == 'n':
                userContinue = False
                break
            else:
                print('Invalid input.')

########################################################################################
# this blackjack is played with only one player and the house as the computer.
# we could modify this in the following ways:
# 1) make it playable by many players, with the user acting for each player
#    this would require a loop for the 'play' for each player, as well as point scores
#    and hands for each player etc...
# 2) incorporate more formal rules of blackjack e.g. change the order in which
#    card are dealt so we see each player's two cards and one of the dealer's two
#    cards
# 3) if you only want to play with one player but get info about cards for card
#    counting purposes, set up the game so that all players are automated 

### how does blackjack work? ###    ################################################
# we are given two cards. we then have the option to hold or to keep
# going. values are 10 for J,Q,K and 1 or 11 for Ace
# we can hold any number, but if we go over 21 we are bust
# at the end the house plays and holds on 17. house can go bust. if house
# gets same as you then the house wins. if it goes bust or holds lower than
# you (at least 17) then you win
# all of the draws are random. once a card is drawn it disappears from the
# deck. once you have a functioning blackjack program, you can edit the
# way house plays to introduce card counting probabilities, and edit the rule
# of holding at 17 to something more probability favourable
# if we go bust we lose our money regardless of whether the house goes bust
# you can change these 'tie' rules later if you like
#########################################################################################

# edit to develop the more formal rules and additional players
# edit to add better 'UI' for navigating to and from 'main-menu'. Add better time delays
    
