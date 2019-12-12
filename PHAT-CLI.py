#-------------------------------------------------------------------------------
# PHAT  - Password Hashing Algorithm Tool
# CLI Python Version
# v 0.1
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
# Python-tk
# Use pip3 to install base58
#
# (C) 2019 Lorne Cammack, USA
# Released under GNU Public License (GPL)
# email lowcam.socailvideo@gmail.com
#-------------------------------------------------------------------------------


import codecs
import hashlib

#This section has the user choose between 3 SHA lengths: 256, 384, and 512
i = 1
while (i == 1):
    shainput = input ('What SHA value would you like? (256, 384, or 512)')
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

# Input from user.
inputText = input ('Enter value: ')
# Take the input text and convert it into byte format.
hashText = bytes(inputText, "ascii")

# This next section hashes the hashText into the correct SHA type as selected
# above
outputText = 0
if valuesha == 256:
    outputText = hashlib.sha256 (hashText).hexdigest()
    print ("SHA 256 sum: ", outputText)
elif valuesha == 384:
    outputText = hashlib.sha384 (hashText).hexdigest()
    print ("SHA 384 sum: ", outputText)
else:
    outputText = hashlib.sha512 (hashText).hexdigest()
    print ("SHA 512 sum: ", outputText)

exitText = input ('Press a key to continue')
