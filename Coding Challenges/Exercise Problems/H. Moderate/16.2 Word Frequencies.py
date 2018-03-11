# 16.2 Word Frequencies
"""
Design a method to find the frequency of occurrences of any given word in a book.
What if we were running this algorithm multiple times?
"""

# Use a hash table (memory inefficient) or a trie (more memory efficient)

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
        def __init__(self):
            self.char = '*'
            self.frequency = 1

    def sortWordDoc(self, text):
        word = ''
        for char in text:
            if char.isalpha():
                word += char
            elif len(word) != 0:
                self.triesIt(word)
                word = ''
        if len(word) != 0:
            self.triesIt(word)

    def triesIt(self, word):
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
                node.frequency += 1
        if isin is False:
            newEnd = self.EndNode()
            node.node.insert(0, newEnd)

    def getFrequency(self, word):
        node = self.start[ord(word[0].lower()) - 97]
        for char in range(1, len(word)):
            isin = False
            for item in range(len(node.node)):
                if node.node[item].char == word[char]:
                    node = node.node[item]
                    isin = True
                    break
            if isin is False:
                print("""The word "{}" is not in the text.""".format(word))
                return 0
        if len(node.node) > 0:
            if node.node[0].char == '*':
                node = node.node[0]
                print ("""The word "{}" appears {} times.""".format(word, node.frequency))
                return node.frequency
        print("""The word "{}" is not in the text.""".format(word))
        return 0


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

word.getFrequency('of')