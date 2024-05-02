def is_prime(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))

def is_primitive_root(g, p):
    return pow(g, p - 1, p) == 1 and pow(g, (p - 1) // 2, p) != 1

def diffie_hellman(p, g, x1, x2):
    y1, y2 = pow(g, x1, p), pow(g, x2, p)
    k1, k2 = pow(y2, x1, p), pow(y1, x2, p)
    return k1, k2

while True:
    P = int(input("Enter P (a prime number): "))
    if not is_prime(P):
        print("Not a prime number. Please enter again.")
    else:
        break

while True:
    G = int(input(f"Enter the primitive root of {P}: "))
    if not is_primitive_root(G, P):
        print(f"{G} is not a primitive root of {P}. Please try again.")
    else:
        break

x1 = int(input("Enter the private key of User 1: "))
x2 = int(input("Enter the private key of User 2: "))

if x1 >= P or x2 >= P:
    print(f"Private key of both users should be less than {P}!")
    exit()

k1, k2 = diffie_hellman(P, G, x1, x2)

print(f"\nSecret key for User 1: {k1}")
print(f"Secret key for User 2: {k2}")

if k1 == k2:
    print("Keys have been exchanged successfully.")
else:
    print("Keys have not been exchanged successfully.")
