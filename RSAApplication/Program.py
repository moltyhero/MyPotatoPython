from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA


def main():
    # random_generator = Random.new().read
    key = RSA.generate(2048)  # generate public and private keys

    public_key = key.publickey().export_key()  # pub key export for exchange

    message = b'You can attack now!'
    cipher = PKCS1_OAEP.new(public_key)
    encrypted = cipher.encrypt(message)
    # message to encrypt is in the above line 'encrypt this message'

    print 'encrypted message:', encrypted  # ciphertext

    f = open('encryption.txt', 'w')
    f.write(str(encrypted))  # write ciphertext to file
    f.close()

    # decrypted code below

    f = open('encryption.txt', 'r')
    message = f.read()

    private_key = key.export_key()
    cipher = PKCS1_OAEP.new(private_key)
    decrypted = cipher.decrypt(message)

    print 'decrypted', decrypted

    f = open('encryption.txt', 'w')
    f.write(str(message))
    f.write(str(decrypted))
    f.close()


if __name__ == '__main__':
    main()