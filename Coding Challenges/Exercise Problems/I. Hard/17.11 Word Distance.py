# 17.11 Word Distance
"""
You have a large text file containing words.
Given any two words, find the shortest distance (in terms of number of words) between them in the file.
If the operation will be repeated many times for the same file (but different pairs of words), can you optimize your solution?
"""

class Tries:
    def __init__(self):
        self.start = []
        for char in range(26):
            node = self.Node(chr(char + 97))
            self.start.append(node)

    class Node:
        def __init__(self, char):
            self.char = char
            self.node = []

    class EndNode:
        def __init__(self, position):
            self.char = '*'
            self.position = [position]

    def sortWordDoc(self, text):
        word = ''
        count = 0
        for char in text:
            if char.isalpha():
                word += char
            elif len(word) != 0:
                self.triesIt(word, count)
                count += 1
                word = ''
        if len(word) != 0:
            self.triesIt(word, count)

    def triesIt(self, word, position):
        node = self.start[ord(word[0].lower()) - 97]
        for char in range(1, len(word)):
            isin = False
            if len(node.node) > 0:
                for item in range(len(node.node)):
                    if node.node[item].char == word[char]:
                        node = node.node[item]
                        isin = True
                        break
            if isin is False:
                newNode = self.Node(word[char])
                node.node.append(newNode)
                node = node.node[-1]
        isin = False
        if len(node.node) > 0:
            if node.node[0].char == '*':
                node = node.node[0]
                isin = True
                node.position.append(position)
        if isin is False:
            newEnd = self.EndNode(position)
            node.node.insert(0, newEnd)

    def getPosition(self, word):
        node = self.start[ord(word[0].lower()) - 97]
        for char in range(1, len(word)):
            isin = False
            for item in range(len(node.node)):
                if node.node[item].char == word[char]:
                    node = node.node[item]
                    isin = True
                    break
            if isin is False:
                return False
        if len(node.node) > 0:
            if node.node[0].char == '*':
                node = node.node[0]
                return node.position
        return False

    def findProximity(self, wordA, wordB):
        if wordA is wordB:
            print ("Same Word!")
            return False
        positionA = self.getPosition(wordA)
        positionB = self.getPosition(wordB)
        A = 0
        B = 0
        lenA = len(positionA) - 1
        lenB = len(positionB) - 1
        min_dif = abs(positionA[A] - positionB[B])
        record_position = (positionA[A], positionB[B])
        while True:
            if positionA[A] > positionB[B] and B < lenB:
                B += 1
            elif positionA[A] < positionB[B] and A < lenA:
                A += 1
            else:
                print("""The minimum distance between the word "{}" and "{}" is {} at position {} and {} of the document."""\
                      .format(wordA.upper(), wordB.upper(), min_dif, record_position[0], record_position[1]))
                return min_dif, record_position
            if min_dif > abs(positionA[A] - positionB[B]):
                min_dif = abs(positionA[A] - positionB[B])
                record_position = (positionA[A], positionB[B])


word = Tries()
word.sortWordDoc("""
The Second Coming 
BY WILLIAM BUTLER YEATS
Turning and turning in the widening gyre   
The falcon cannot hear the falconer; 
Things fall apart; the centre cannot hold; 
Mere anarchy is loosed upon the world, 
The blood-dimmed tide is loosed, and everywhere   
The ceremony of innocence is drowned; 
The best lack all conviction, while the worst   
Are full of passionate intensity. 

Surely some revelation is at hand; 
Surely the Second Coming is at hand.   
The Second Coming! Hardly are those words out   
When a vast image out of Spiritus Mundi 
Troubles my sight: somewhere in sands of the desert   
A shape with lion body and the head of a man,   
A gaze blank and pitiless as the sun,   
Is moving its slow thighs, while all about it   
Reel shadows of the indignant desert birds.   
The darkness drops again; but now I know   
That twenty centuries of stony sleep 
Were vexed to nightmare by a rocking cradle,   
And what rough beast, its hour come round at last,   
Slouches towards Bethlehem to be born?
""")

word.findProximity('anarchy', 'mundi')


