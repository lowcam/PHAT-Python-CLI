import codecs
import hashlib


inputText = input ('Enter value: ') #Input from user
hashText = bytes(inputText, "ascii") #Take the input text and convert it into byte format
print ('SHA 256 sum: ', hashlib.sha256 (hashText).hexdigest()) #Output the hashed output. Hexdigest puts it into hex number system
exitText = input ('Press a key to continue')
