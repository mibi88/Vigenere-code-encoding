import ipywidgets as widgets
from IPython.display import display

text1 = widgets.Textarea(
    value='Texte à encoder/décoder',
    placeholder='Entrez le texte à encoder/décoder',
    description='À encoder/décoder',
    disabled=False
)
text2 = widgets.Textarea(
    value='',
    placeholder='Texte encodé/décodé',
    description='Encodé/décodé',
    disabled=True
)
key_e = widgets.Text(
    value='',
    placeholder='Clé',
    description='',
    disabled=False
)
charmap_e = widgets.Text(
    value='ABCDEFGHIJKLMNOPQRSTUVWXYZ',
    placeholder='Table de charactères',
    description='',
    disabled=False
)
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
def enc_f(b):
    string = text1.value
    key = key_e.value
    chars = charmap_e.value
    charlist = []
    for letter in chars:
        charlist.append(letter)
    badkey = False
    for letter in key:
        if letter in charlist:
            pass
        else:
            badkey = True
    if badkey == True:
        text2.value = "Error : Bad key."
    else:
        text = encode(string, key, chars)
        text2.value = text
def dec_f(b):
    string = text1.value
    key = key_e.value
    chars = charmap_e.value
    charlist = []
    for letter in chars:
        charlist.append(letter)
    badkey = False
    for letter in key:
        if letter in charlist:
            pass
        else:
            badkey = True
    if badkey == True:
        text2.value = "Bad key"
    else:
        text = decode(string, key, chars)
        text2.value = text
encb = widgets.Button(
    description='Encoder',
    disabled=False,
    button_style='success',
    tooltip='Encoder',
    icon='key'
)
decb = widgets.Button(
    description='Décoder',
    disabled=False,
    button_style='success',
    tooltip='Décoder',
    icon='key'
)
display(text1)
display(text2)
display(key_e)
display(charmap_e)
display(encb)
display(decb)
encb.on_click(enc_f)
decb.on_click(dec_f)