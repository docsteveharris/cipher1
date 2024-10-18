ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def encrypt_forwards(a, b, text: list):
    cipher_key = ""
    for t in text:
        u = ALPHABET.index(t)
        v = ((u * a) + b) % len(ALPHABET)
        cipher_key += ALPHABET[v]
    if len(set(cipher_key)) != len(ALPHABET):
        raise ValueError("Duplicate characters in cipher key")
    return cipher_key


if __name__ == "__main__":
    test_text = input("Enter text to encrypt: ")
    test_text = test_text.lower()
    a, b = map(int, input("Enter two integers separated by space: ").split())

    try:
        CIPHER_KEY = encrypt_forwards(a, b, list(ALPHABET))
    except ValueError as e:
        print(e)
        print("Hint: you probably need larger values for A and B")
    print(f"{ALPHABET} -> {CIPHER_KEY}")

    cracked_text = ""
    for t in test_text:
        if t in CIPHER_KEY:
            print(f"{t} -> {CIPHER_KEY.index(t)}")
            cracked_text += ALPHABET[CIPHER_KEY.index(t)]
        else:
            print(f"{t} -> not found")
            cracked_text += t
    print(cracked_text)
