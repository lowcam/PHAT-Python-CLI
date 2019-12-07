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
# (C) 2019 Lorne Cammack, USA
# Released under GNU Public License (GPL)
# email lowcam.socailvideo@gmail.com
#-------------------------------------------------------------------------------


import codecs
import hashlib

# Input from user.
inputText = input ('Enter value: ')
# Take the input text and convert it into byte format.
hashText = bytes(inputText, "ascii")
# Output the hashed output. Hexdigest puts it into hex number system.
print ('SHA 256 sum: ', hashlib.sha256 (hashText).hexdigest())
# Wait for the user to press a key before exiting.
exitText = input ('Press a key to continue')
