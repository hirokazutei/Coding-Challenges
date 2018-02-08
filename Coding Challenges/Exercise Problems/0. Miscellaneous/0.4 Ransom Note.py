# A ransom note can be formed by cutting words out of a magazine to form a new sentece.
# How would you figure out if a ransom note (represented as a string) can be formed from a given magazine (string)?

magazine = "I met a traveler from an antique land Who said: Two vast and trunkless legs of stoneStand in the desert . . . Near them, on the sand, Half sunk, a shattered visage lies, whose frown,And wrinkled lip, and sneer of cold command,Tell that its sculptor well those passions readWhich yet survive, stamped on these lifeless things,The hand that mocked them, and the heart that fed:And on the pedestal these words appear:‘My name is Ozymandias, king of kings:Look on my works, ye Mighty, and despair!’Nothing beside remains. Round the decayOf that colossal wreck, boundless and bareThe lone and level sands stretch far away.”"
ransomnote = "Can I make a ransom with the poem?"

def makeRansom(magazine, ransomnote):
    wordtable = [0] * 10000
    biggest = 0;
    thechar = ''
    for char in magazine:
        wordtable[ord(char)] = wordtable[ord(char)] + 1
        if (ord(char) > biggest):

    for char in ransomnote:
        wordtable[ord(char)] = wordtable[ord(char)] - 1
        if (wordtable[ord(char)] < 0):
            print ("Ransom Note CANNOT Be made!")
            return 0
    print ("Ransom Note CAN Be Made!")


makeRansom(magazine, ransomnote)
