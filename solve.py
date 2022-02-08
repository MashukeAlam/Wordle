from collections import Counter
import string

def loadWords():
    alls = ""
    allPossible = []
#this fives.txt is the actual dictionary that's used in wordle... copied from an article
    with open("fives.txt", "r", newline='') as f:
        for word in f:
            word = word.lower().strip()
            if len(word) == 5 and word.isalpha():
                allPossible.append(word)
                alls += word
    return allPossible, alls

# print(loadWords())
allPossible, hugeAssWord = loadWords()

def determineFrequency():
    priority = Counter(hugeAssWord)
    rough = list(priority.most_common())
    return [l[0] for l in rough]

# print(determineFrequency())
priority = determineFrequency()

notHere = set()
isHere = set()
isHereBut = set()
notHereD = {}
isHereD = {}
isHereButD = {}
fff = ['.', '.', '.', '.', '.']
xxx = ['.', '.', '.', '.', '.']

for l in string.ascii_lowercase:
    notHereD[l] = -1
    isHereD[l] = -1
    isHereButD[l] = -1

def guess(first=False, mask="", prevList=[]):
    global fff, notHere, isHere, isHereBut, isHereD, notHereD, isHereButD
    if mask == 'ggggg':
        print("Great!")
        return
    wordRank = []
    if first:
        for word in allPossible:
            score = 0
            isHere = set()
            for letter in word:
                if letter not in isHere:
                    score += len(priority) - priority.index(letter)
                    isHere.add(letter)
            wordRank.append((score, word))
        # print(wordRank)
        return wordRank
    else:
        probableList = []
        
        
        prev = prevList[-1]
        # print(prev)
        for i in range(5):
            if mask[i] == 'a':
                notHereD[prev[i]] = i
                notHere.add(prev[i])
            elif mask[i] == 'g':
                isHereD[prev[i]] = i
                isHere.add(prev[i])
                fff[i] = prev[i]
            else:
                isHereButD[prev[i]] = i
                isHereBut.add(prev[i])
                xxx[i] = prev[i]
        
        for word in allPossible:
            if word not in prevList:
                for i in range(5):
                    if word[i] in notHere:
                        
                        allPossible.remove(word)
                        # print(word)
                        break
        greenList, yellowList = [], []

        
        for word in allPossible:
            if regex(fff, word):
                # print(word)
                greenList.append(word)
        # print(probableList)
        

        for word in allPossible:
            if regex(xxx, word, positionMatch=False):
                # print(word)
                yellowList.append(word)

        

        if len(greenList) > 0 and len(greenList) < len(yellowList):
            return greenList
        elif len(yellowList) > 0:
            return yellowList


        return allPossible

def regex(fff, word, positionMatch=True):
    if positionMatch:
        joined = ''.join(fff)
        for i in range(5):
            if joined[i] == '.': continue
            if joined[i] not in word:
                return False
            if joined[i] != word[i]:
                return False
        return True

    else:
        joined = ''.join(fff)
        for i in range(5):
            if joined[i] == '.': continue
            if  joined[i] not in word:
                return False
            if joined[i] == word[i]:
                return False
        return True

def ranking(wordList):
    print(f"{len(wordList)} words remaining")
    wordRank = []
    for word in wordList:
        score = 0
        isHere = set()
        for letter in word:

            if letter not in isHere:
                score += len(priority) - priority.index(letter)
                isHere.add(letter)
        wordRank.append((score, word))
        return wordRank

first = True
prev = ""
prevList = []
print('''For masking:
put 5 letter word
a for Ash
y for Yellow
g for Green
''')
while True:
    # print(prevList)
    if first:
        wordRank = guess(first=True)
        wordRank.sort(reverse=True)
        prev = wordRank[0][1]
        prevList.append(prev)
        print(f"How about : {prev}")
        first = False
    else:
        mask = input("Mask? ")
        prob = guess(mask=mask, prevList=prevList)
        # print(prob)
        wordRank = ranking(prob)
        wordRank.sort(reverse=True)
        prev = wordRank[0][1]
        prevList.append(prev)
        print(f"How about : {prev}")
    allPossible.remove(prev)



