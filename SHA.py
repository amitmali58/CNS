
import hashlib

def calculate_sha1(text):
    return hashlib.sha1(text.encode()).hexdigest()

text1 = input("Enter original text: ")
text2 = input("Enter modified text: ")

hash1 = calculate_sha1(text1)
hash2 = calculate_sha1(text2)

print("\nSHA-1 Message Digest")
print("Original Text :", text1)
print("SHA-1 Digest  :", hash1)

print("\nModified Text :", text2)
print("SHA-1 Digest  :", hash2)

print("\nAre both digests same?", hash1 == hash2)
