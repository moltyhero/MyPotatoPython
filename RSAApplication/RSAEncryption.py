from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


def generate_RSA_key():
    key = RSA.generate(2048)  # generate public and private key

    # The following code generates public key stored in receiver.pem and private key stored in private.pem

    private_key = key.export_key()
    file_out = open("private.pem", "wb")
    file_out.write(private_key)

    public_key = key.publickey().export_key()  # or = RSA.import_key(open("receiver.pem").read())
    file_out = open("receiver.pem", "wb")
    file_out.write(public_key)


def encrypt_message(message):
    public_key = RSA.import_key(open("receiver.pem").read())
    cipher = PKCS1_OAEP.new(public_key)
    encrypted = cipher.encrypt(message)  # Enter here any string you want to encrypt

    return encrypted


def decrypt_message():
    f = open('encryption.txt', 'r')
    message = f.read()

    private_key = RSA.import_key(open("private.pem").read())
    new_cipher = PKCS1_OAEP.new(private_key)
    decrypted = new_cipher.decrypt(message)  # does not work

    return decrypted
