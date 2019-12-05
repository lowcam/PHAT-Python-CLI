import codecs
import hashlib


walkingtaco = input ('Enter value: ')
tacowalking = bytes(walkingtaco, "ascii")
print ('SHA 256 sum: ', hashlib.sha256 (tacowalking).hexdigest())
roofshingles = input ('Press a key to continue')