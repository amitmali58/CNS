from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
import time

key_sizes = [ 1024, 2048, 3072]
message_sizes = [8, 16, 32, 48,60]  # bytes

for bits in key_sizes:
    # 1. Generate RSA key pair
    start = time.perf_counter()

    private_key = rsa.generate_private_key(
        public_exponent=65537, key_size=bits
    )
    public_key = private_key.public_key()

    key_time = time.perf_counter() - start

    print(f"\nRSA Key Size: {bits} bits")
    print(f"Key generation time: {key_time:.6f} seconds")
    print("Message Size | Encrypt (s) | Decrypt (s)")

    for size in message_sizes:
        message = b"A" * size

        # 2. Encrypt message
        start = time.perf_counter()
        ciphertext = public_key.encrypt(
            message,
            padding.OAEP(
                mgf=padding.MGF1(hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        enc_time = time.perf_counter() - start

        # 3. Decrypt message
        start = time.perf_counter()
        plaintext = private_key.decrypt(
            ciphertext,
            padding.OAEP(
                mgf=padding.MGF1(hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        dec_time = time.perf_counter() - start

        assert plaintext == message
        print(f"{size:12} | {enc_time:.8f} | {dec_time:.8f}")
