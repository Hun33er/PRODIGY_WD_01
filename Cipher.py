def caesar_cipher(text, shift, direction):
    result = ""
    shift = shift % 26  # Ensure the shift is within the range of the alphabet

    if direction == "decrypt":
        shift = -shift

    for char in text:
        if char.isalpha():
            shift_base = ord('a') if char.islower() else ord('A')
            new_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            result += new_char
        else:
            result += char

    return result

def main():
    print("Welcome to the Caesar Cipher Program!")
    
    while True:
        direction = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").strip().lower()
        if direction in ['encrypt', 'decrypt']:
            break
        else:
            print("Invalid input. Please type 'encrypt' or 'decrypt'.")

    text = input("Enter your message: ").strip()
    shift = int(input("Enter the shift number: ").strip())

    result = caesar_cipher(text, shift, direction)
    print(f"The resulting text is: {result}")

if __name__ == "__main__":
    main()
