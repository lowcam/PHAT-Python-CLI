#-------------------------------------------------------------------------------
# PHAT  - Password Hashing Algorithm Tool
# CLI Python Version
# v 0.4
#
# The purpose of this tool is to let an individual enter text and have a hashed
# output to use as the password to the site or program. Initially the program
# will hash the input in SHA 256 and output in hexadecimal. THe plans for this
# program are to allow the selection of three different SHA lengths (256, 384,
# and 512). Also, the output numbering system will be selectable between
# hexadecimal, base64, and base58. Also, the number of digits in the ouput
# will be selectable in case a site can only have a certain number of digits
# in a password. THe last step will be for the output to be copied to the
# clipboard so if can be pasted into the program or site.
#
# Required to use:
# Python3
# Python3-tk
# Use pip3 to install base58
#
# (C) 2019 Lorne Cammack, USA
# Released under GNU Public License (GPL) v3
# email lowcam.socailvideo@gmail.com
#-------------------------------------------------------------------------------


import codecs
import hashlib
import base58


# This section has the user choose between 3 SHA lengths: 256, 384, and 512
def selectSHA():
    i = 1
    while (i == 1):
        shainput = input ('What SHA value would you like? (256, 384, or 512)')
        global valuesha
        try:
            testVal = int(shainput)
        except ValueError:
            print("Incorrect value entered. Please try again.")
            i=1
        else:
            valuesha = int(shainput)
            if valuesha == 256:
                i = 2
            elif valuesha == 384:
                i = 2
            elif valuesha == 512:
                i = 2
            else:
                print ("Incorrect value entered. Please try again.")
                i=1

# This section deals with selecting an output number system between
# Hexidecimal, Base 64, and Base 58.
def OutputNumberSystem():
    i=1
    while (i==1):
        numsysvalue = input ('Choose output number system: 1. Hex; 2. Base64; 3. Base58  ')
        global valuenumsys
        try:
            testVal = int(numsysvalue)
        except:
            print("Incorrect value entered. Please try again.")
            i=1
        else:
            valuenumsys = int(numsysvalue)
            if valuenumsys == 1:
                i = 2
            elif valuenumsys == 2:
                i = 2
            elif valuenumsys == 3:
                i = 2
            else:
                print ("Incorrect value entered. Please try again.")
                i=1

# This section lets a user decide how many digits they want in the final output
def numdigfinal():
    i = 1
    while (i == 1):
        global finaldig
        digfinalyn = input ('Would you like to restrict the number of digits in the output? (Y/N) ')
        if digfinalyn == 'Y' or digfinalyn == 'y':
            digfinal = input ('How many digits would you like? (1-128) ')
            try:
                val = int(digfinal)
            except:
                print("Incorrect value entered. Please try again.")
                i=1
            else:
                finaldig = int(digfinal)
                if finaldig < 1 or finaldig > 128:
                    print ("This value is not acceptable")
                    i=1
                else:
                    i=2
        elif digfinalyn == 'N' or digfinalyn == 'n':
            finaldig = 0
            i=2
        else:
            print ("That is an incorrect selection.")
            i = 1

# This section gets the values ready to print. For Base64 and Base58 it
# decodes the output from Hex, which it is in when it is sent, and then
# reencodes it into the numbering system choosen in OutputNumberSystem().
def outputPrint(hexhashvalue):
    global printreturn
    printreturn=0
    if valuenumsys == 1:
        printreturn = hexhashvalue
    elif valuenumsys == 2:
        printreturn = codecs.encode(codecs.decode(hexhashvalue, 'hex'), 'base64').decode()
    else:
        printreturn = base58.b58encode(codecs.decode(hexhashvalue, 'hex'))

# This section gets everything ready for the output
def finalprint (hexhashvalue):

    lenhash = len(hexhashvalue)
    if finaldig == 0 or finaldig >= lenhash:
        if valuenumsys == 1:
            #printreturn = hexhashvalue
            print ("SHA", valuesha, "sum in hex: ")
            print (printreturn)
        elif valuenumsys == 2:
            #printreturn = codecs.encode(codecs.decode(hexhashvalue, 'hex'), 'base64').decode()
            print ("SHA", valuesha, "sum in base64: ")
            print (printreturn)
        else:
            #printreturn = base58.b58encode(codecs.decode(hexhashvalue, 'hex'))
            print ("SHA", valuesha, "sum in base58: ")
            print (printreturn)
    else:
        if valuenumsys == 1:
            #printreturn = hexhashvalue
            print ("SHA", valuesha, "sum in hex: ")
            print (printreturn[:finaldig])
        elif valuenumsys == 2:
            #printreturn = codecs.encode(codecs.decode(hexhashvalue, 'hex'), 'base64').decode()
            print ("SHA", valuesha, "sum in base64: ")
            print (printreturn[:finaldig])
        else:
            #printreturn = base58.b58encode(codecs.decode(hexhashvalue, 'hex'))
            print ("SHA", valuesha, "sum in base58: ")
            print (printreturn[:finaldig])

selectSHA()
OutputNumberSystem()
numdigfinal()
# Input from user.
inputText = input ('Enter value: ')
# Take the input text and convert it into byte format.
hashText = bytes(inputText, "ascii")

# This next section hashes the hashText into the correct SHA type as selected
# above
outputText = 0
if valuesha == 256:
    outputText = hashlib.sha256 (hashText).hexdigest()
elif valuesha == 384:
    outputText = hashlib.sha384 (hashText).hexdigest()
else:
    outputText = hashlib.sha512 (hashText).hexdigest()

outputPrint(outputText)
finalprint(outputText)

exitText = input ('Press a key to continue')
