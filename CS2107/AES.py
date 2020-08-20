from Crypto.Cipher import AES
import hashlib
from string import ascii_lowercase

import base64

word='apple'
passwords=['napier','test','password','foxtrot','123456','qwerty']
password='napier'
passw=''

plaintext=''

def isprintable(s, codec='utf8'):
    try: s.decode(codec)
    except UnicodeDecodeError: return False
    else: return True

def encrypt(plaintext, key, mode):
    encobj = AES.new(key, mode)
    return(encobj.encrypt(plaintext))

def decrypt(ciphertext,key, mode):
    encobj = AES.new(key, mode)
    return(encobj.decrypt(ciphertext))


ciphertext='Tn+vFmDJqIuKH9Dy1yKHMcDUqoCFkQJR3kWC1wYu2xdFpa8eMb5xtD88xkEcfZQd'
ciphertext=base64.b64decode(ciphertext)

f = open("test.txt", "w+")

all = set()
for l1 in ascii_lowercase:
    for l2 in ascii_lowercase:
        for l3 in ascii_lowercase:
            for l4 in ascii_lowercase:
                for l5 in ascii_lowercase:
                    temp = l1 + l2 + l3 + l4 + l5
                    key = hashlib.sha256(temp.encode()).digest()

                    try:
                        plaintext = decrypt(ciphertext, key[0:16], AES.MODE_ECB)
                        if isprintable(plaintext, codec='utf8'):
                            print('Plain text is ', plaintext.decode('utf8'), ' and password is ', temp)
                            f.write(plaintext.decode('utf8'))
                            f.flush()
                        else:
                            print(temp)
                    except:
                        continue


# encodestr = base64.b64encode('abcr34r344r'.encode('utf-8'))

text = base64.b64decode(ciphertext)