from tkinter import *
from tkinter.scrolledtext import *
from tkinter.messagebox import *

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
mainw = Tk()
#===
text_lf = LabelFrame(mainw, text="Text ...")
text_lf.pack(fill="both", expand="no")
#===
to_translate_lf = LabelFrame(text_lf, text="Text to translate")
to_translate_lf.pack(fill="both", expand="yes", side=LEFT)
#---
translated_lf = LabelFrame(text_lf, text="Translated text")
translated_lf.pack(fill="both", expand="yes", side=RIGHT)
#===
to_translate = ScrolledText(to_translate_lf, wrap="word")
translated = ScrolledText(translated_lf, wrap="word", state="disabled")
#---
infos1 = Label(to_translate_lf, text="Type your text to translate here :")
infos2 = Label(translated_lf, text="See the translated text :")
infos1.pack()
infos2.pack()
to_translate.pack()
translated.pack()
data = Frame(mainw)
info1_data = Label(data, text = "Key :").pack(side = LEFT)
key_e = Entry(data)
key_e.pack(side = LEFT, fill = "both", expand = True)
info2_data = Label(data, text = "Character map :").pack(side = LEFT)
charmap_e = Entry(data)
charmap_e.pack(side = LEFT, fill = "both", expand = True)
data.pack(fill = "both", expand = True)
commands = Frame(mainw)
def enc_f():
    translated.configure(state="normal")
    string = to_translate.get(1.0, END)
    key = key_e.get()
    chars = charmap_e.get()
    charlist = []
    for letter in chars:
        charlist.append(letter)
    badkey = False
    for letter in key:
        if letter in charlist:
            pass
        else:
            badkey = True
    translated.delete(1.0, END)
    if badkey == True:
        translated.insert(1.0, "Error : Bad key.")
    else:
        text = encode(string, key, chars)
        translated.insert(1.0, text)
        translated.configure(state="disabled")
def dec_f():
    translated.configure(state="normal")
    string = to_translate.get(1.0, END)
    key = key_e.get()
    chars = charmap_e.get()
    charlist = []
    for letter in chars:
        charlist.append(letter)
    badkey = False
    for letter in key:
        if letter in charlist:
            pass
        else:
            badkey = True
    translated.delete(1.0, END)
    if badkey == True:
        translated.insert(1.0, "Bad key")
    else:
        text = decode(string, key, chars)
        translated.insert(1.0, text)
        translated.configure(state="disabled")
enc=Button(commands, text="Encode", command=enc_f)
enc.pack(side=LEFT)
dec=Button(commands, text="Decode", command=dec_f)
dec.pack(side=LEFT)
commands.pack()