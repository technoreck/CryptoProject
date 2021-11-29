from pyDes import des, CBC, PAD_PKCS5
import binascii

# Secret key
KEY = string(input('enter the key of 8 char length'))

def des_encrypt(s):
    """
         DES encryption
         : Param s: Raw string
         : Return: After encryption, string, 16
    """
    secret_key = KEY
    iv = secret_key
    k = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    en = k.encrypt(s, padmode=PAD_PKCS5)
    return binascii.b2a_hex(en).decode()


def des_descrypt(s):
    """
         DES decryption
         : Param s: Encrypted strings, 16
         : Return: String after decryption
    """
    secret_key = KEY
    iv = secret_key
    k = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    de = k.decrypt(binascii.a2b_hex(s), padmode=PAD_PKCS5)
    return de.decode()
s = 'kKCtFQbVXOg0+Bzy3h1cAQ=='
enc = des_encrypt(s)
print(enc)
des = des_descrypt(enc)
print(des)