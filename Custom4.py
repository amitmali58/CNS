import hashlib
import time

class CustomCipher:
    def __init__(self, key):
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, text):
        data = bytearray(text.encode())
        for i in range(len(data)):
            data[i] ^= self.key[i % 32]
            data[i] = (data[i] + i + 5) % 256
        return bytes(data)

    def decrypt(self, cipher):
        data = bytearray(cipher)
        for i in range(len(data)):
            data[i] = (data[i] - i - 5) % 256
            data[i] ^= self.key[i % 32]
        return data.decode()


text = input("Enter plaintext: ")
key = input("Enter secret key: ")

if not key:
    print("Key cannot be empty!")
else:
    cipher = CustomCipher(key)

    start = time.perf_counter()
    encrypted = cipher.encrypt(text)
    enc_time = time.perf_counter() - start

    start = time.perf_counter()
    decrypted = cipher.decrypt(encrypted)
    dec_time = time.perf_counter() - start

    print("Ciphertext:", encrypted.hex())
    print("Decrypted:", decrypted)
    print(f"Encryption Time: {enc_time:.8f} seconds")
    print(f"Decryption Time: {dec_time:.8f} seconds")
    print("Verification:", "SUCCESS" if text == decrypted else "FAILED")