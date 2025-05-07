from system.py.core import env
from system.controller.file import file
from system.controller.log import log
from system.library.pycryptodome import aes, random_bytes
from system.py.tk import alert


class Crypt:
    def __init__(self):
        self.path_encrypt = env("PATH_ENCRYPT")
        self.path_decrypt = env("PATH_DECRYPT")
        self.encrypt_extension = ".enc"
        self.decrypt_extension = ".dec.txt"

    def decrypt(self, data: list):
        for item in data:
            try:
                filename = item["text"].split(".")[0]
                f = file.read(item["path"], item["text"], close=False, binary=True)
                tag = f.read(16)
                nonce = f.read(15)
                key = f.read(16)
                ciphertext = f.read()
                f.close()

                cipher = aes.new(key, aes.MODE_OCB, nonce=nonce)
                message = cipher.decrypt_and_verify(ciphertext, tag).decode()
                file.write(self.path_encrypt, f"{filename}{self.decrypt_extension}", message)

            except Exception as e:
                log.write(f"Error decrypting file `{item['text']}`: {e}")
                alert.showerror("System", f"An error occurred while decrypting `{item['text']}`: {e}")

    def encrypt(self, data: list):
        for item in data:
            try:
                filename = item["text"].split(".")[0]
                text = file.read(item["path"], item["text"], binary=True)
                key = random_bytes(16)
                cipher = aes.new(key, aes.MODE_OCB)
                ciphertext, tag = cipher.encrypt_and_digest(text)
                assert len(cipher.nonce) == 15

                f = file.write(self.path_decrypt, f"{filename}{self.encrypt_extension}", close=False, binary=True)
                f.write(tag)
                f.write(cipher.nonce)
                f.write(key)
                f.write(ciphertext)
                f.close()

            except Exception as e:
                log.write(f"Error encrypting file `{item['text']}`: {e}")
                alert.showerror("System", f"An error occurred while encrypting `{item['text']}`: {e}")


crypt = Crypt()
