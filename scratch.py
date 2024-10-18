import streamlit as st

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


def cipher_forwards(text: str, CIPHER_KEY: str, ALPHABET: str = ALPHABET):
    result = ""
    for t in text:
        if t in CIPHER_KEY:
            print(f"{t} -> {CIPHER_KEY.index(t)}")
            result += ALPHABET[CIPHER_KEY.index(t)]
        else:
            print(f"{t} -> not found")
            result += t
    return result


def main():
    # Heading
    st.title("Kian's Cipher Sniper")
    a = st.slider("a", min_value=0, max_value=100, value=11, step=1)
    b = st.slider("b", min_value=0, max_value=100, value=3, step=1)

    CIPHER_KEY = encrypt_forwards(a, b, list(ALPHABET))

    # User input
    user_input = st.text_area("Enter your text here:")
    cleaned_input = user_input.lower()
    if st.button("Snipe"):
        if user_input:
            result = cipher_forwards(cleaned_input, CIPHER_KEY)
            st.success(f"Encrypted text: {result}")
            # st.write(result)
        else:
            st.warning("Please enter some text to encrypt.")

    # test_text = input("Enter text to encrypt: ")
    # test_text = test_text.lower()
    # a, b = map(int, input("Enter two integers separated by space: ").split())


if __name__ == "__main__":
    main()
