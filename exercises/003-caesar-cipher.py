def caesar_cipher(text, shift):
    """
    Encrypts or decrypts text using the Caesar cipher.

    Args:
    text (str): The text to be encrypted or decrypted.
    shift (int): The number of positions to shift each letter. Positive for encryption, negative for decryption.

    Returns:
    str: The encrypted or decrypted text.
    """
    result = ""
    for char in text:
        if char.isalpha():
            # Determine the ASCII offset based on whether the character is uppercase or lowercase
            ascii_offset = 65 if char.isupper() else 97
            # Apply the shift and wrap around the alphabet
            shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            result += shifted_char
        else:
            # If the character is not a letter, leave it unchanged
            result += char
    return result


def main():
    while True:
        choice = input("Choose operation (1 for encryption, 2 for decryption, 3 to quit): ")

        if choice == '3':
            break

        if choice not in ['1', '2']:
            print("Invalid choice. Please try again.")
            continue

        text = input("Enter the text: ")
        shift = int(input("Enter the shift value: "))

        if choice == '2':
            shift = -shift  # For decryption, we use the negative of the shift

        result = caesar_cipher(text, shift)

        operation = "Encrypted" if choice == '1' else "Decrypted"
        print(f"{operation} text: {result}")
        print()

if __name__ == "__main__":
    main()
