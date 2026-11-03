p = 23
g = 5

# Private keys
a, b = 6, 15
e1, e2 = 7, 11

# Public keys of Alice and Bob
A = pow(g, a, p)
B = pow(g, b, p)

# Eve's fake public keys
E1 = pow(g, e1, p)
E2 = pow(g, e2, p)

# Shared keys
alice_eve = pow(E1, a, p)
eve_alice = pow(A, e1, p)

bob_eve = pow(E2, b, p)
eve_bob = pow(B, e2, p)

print("Alice Public Key =", A)
print("Bob Public Key =", B)
print("\nEve sends fake key to Alice =", E1)
print("Eve sends fake key to Bob =", E2)

print("\nAlice-Eve Shared Key =", alice_eve)
print("Eve-Alice Shared Key =", eve_alice)
print("Bob-Eve Shared Key =", bob_eve)
print("Eve-Bob Shared Key =", eve_bob)

print("\nMITM Attack Successful!")