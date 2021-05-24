def encode(string, key, chars):
    charlist = []
    for letter in chars:
        print(letter)
        charlist.append(letter)
    print(charlist)
    lenght = len(string)
    keystr = buildkey(key, lenght, string, chars)
    genstring = ""
    i = 0
    for letter in string:
        keyletter = keystr[i:i + 1]
        genstring += getletter1(letter, keyletter, charlist, chars)
    return genstring
def buildkey(key, lenght, orgstring, chars):
    i = 0
    i_a = 0
    i_a_max = len(key)
    string = ""
    while i != lenght:
        #print(i)
        if i_a == i_a_max:
            i_a = 0
        letter = orgstring[i:i + 1]
        if not letter in chars:
            string += letter
        else:
            string += key[i_a:i_a + 1]
            i_a += 1
        i += 1
    print(string)
    return string
def getletter1(stringletter, keyletter, charlist, chars):
    #if stringletter in chars:
    try:
        startpos = charlist.index(stringletter)
        i = 0
        i_a = startpos
        lenght = len(charlist)
        result = ""
        maxi = lenght - startpos
        while i != lenght:
            if i == maxi:
                i_a = 0
            result += charlist[i_a]
            i += 1
            i_a += 1
        print(result)
        resultlist = []
        for letter in result:
            resultlist.append(letter)
        letteritem = charlist.index(keyletter)
        char = resultlist[letteritem]
        print(char)
    except ValueError:
        char = stringletter
    return char
#print(encode(string = "MA STRING QUI ME PASSIONNE !!! VIVE VIGENERE !!!", key = "GRANDMISTERE", chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
def decode(string, key, chars):
    charlist = []
    for letter in chars:
        print(letter)
        charlist.append(letter)
    print(charlist)
    lenght = len(string)
    keystr = buildkey(key, lenght, string, chars)
    genstring = ""
    i = 0
    for letter in string:
        keyletter = keystr[i:i + 1]
        genstring += getletter2(letter, keyletter, charlist, chars)
    return genstring
def getletter2(stringletter, keyletter, charlist, chars):
    #if stringletter in chars:
    try:
        startpos = charlist.index(keyletter)
        i = 0
        i_a = startpos
        lenght = len(charlist)
        result = ""
        maxi = lenght - startpos
        while i != lenght:
            if i == maxi:
                i_a = 0
            result += charlist[i_a]
            i += 1
            i_a += 1
        print(result)
        resultlist = []
        for letter in result:
            resultlist.append(letter)
        letteritem = resultlist.index(stringletter)
        char = charlist[letteritem]
        print(char)
    except ValueError:
        char = stringletter
    return char
#print(decode(string = "SG YZXOTM WAO SK VGYYOUTTK !!! BOBK BOMKTKXK !!!", key = "GRANDMISTERE", chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"))