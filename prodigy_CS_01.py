def caesar_cipher_encrypt(text, shift):
    result = ""
    
    # Traverse text
    for char in text:
        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            # Append non-alphabetic characters unchanged
            result += char
            
    return result

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

def main():
    while True:
        print("Caesar Cipher Tool")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            message = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value: "))
            encrypted_message = caesar_cipher_encrypt(message, shift)
            print(f"Encrypted message: {encrypted_message}")
        elif choice == '2':
            message = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value: "))
            decrypted_message = caesar_cipher_decrypt(message, shift)
            print(f"Decrypted message: {decrypted_message}")
        elif choice == '3':
            print("Exiting the Caesar Cipher Tool. Goodbye!")
            break
        else:
            print("Invalid choice! Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
