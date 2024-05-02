def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

def main():
    text = input("Enter the text: ")
    shift = int(input("Enter the shift value: "))

    encrypted_text = caesar_cipher(text, shift)
    print("Encrypted:", encrypted_text)

    decrypted_text = caesar_cipher(encrypted_text, -shift)
    print("Decrypted:", decrypted_text)

if __name__ == "__main__":
    main()
