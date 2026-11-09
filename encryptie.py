import os
import base64

from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt


def encrypt_text(text, password):
    salt = os.urandom(16)

    kdf = Scrypt(
        salt=salt,
        length=32,
        n=2**14,
        r=8,
        p=1
    )
    key = kdf.derive(password.encode("utf-8"))

    nonce = os.urandom(12)

    aesgcm = AESGCM(key)
    ciphertext = aesgcm.encrypt(
        nonce,
        text.encode("utf-8"),
        None
    )

    encrypted_data = salt + nonce + ciphertext

    return base64.b64encode(encrypted_data).decode("utf-8")

def decrypt_text(encrypted_text, password):
    encrypted_data = base64.b64decode(encrypted_text, validate=True)

    salt = encrypted_data[:16]
    nonce = encrypted_data[16:28]
    ciphertext = encrypted_data[28:]

    kdf = Scrypt(
        salt=salt,
        length=32,
        n=2**14,
        r=8,
        p=1
    )
    key = kdf.derive(password.encode("utf-8"))

    aesgcm = AESGCM(key)
    plaintext = aesgcm.decrypt(nonce, ciphertext, None)

    return plaintext.decode("utf-8")
