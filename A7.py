from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import hashes

# 1. Generate DSA Key Pair
private_key = dsa.generate_private_key(key_size=2048)
public_key = private_key.public_key()

# Input original message
message = input("Enter original message: ").encode()

# 2. Create Digital Signature
signature = private_key.sign(message, hashes.SHA256())

print("\nDigital Signature:")
print(signature.hex())

# 3. Verify Original Message
try:
    public_key.verify(signature, message, hashes.SHA256())
    print("\nOriginal Message: Signature is VALID")
except Exception:
    print("\nOriginal Message: Signature is INVALID")

# 4. Input Modified Message
modified_message = input("\nEnter modified message: ").encode()

# Verify Modified Message
try:
    public_key.verify(signature, modified_message, hashes.SHA256())
    print("Modified Message: Signature is VALID")
except Exception:
    print("Modified Message: Signature is INVALID - Message was modified")

