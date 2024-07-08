import getpass

print("-------------------------------------------- Caesar Cipher --------------------------------------------------")
print("-------------------------------------------- Caesar Cipher Tool --------------------------------------------------")
print("")

def caesar_cipher(text, shift, mode='encrypt'):
    """
    Encrypts or decrypts text using Caesar Cipher.
    
    Parameters:
    - text (str): The input text to be encrypted or decrypted.
    - shift (int): The number of positions to shift the text by.
    - mode (str): Either 'encrypt' or 'decrypt'. Defaults to 'encrypt'.
    
    Returns:
    - str: The encrypted or decrypted text.
    """
    result = ""
    shift = shift % 26  # Ensure shift is within the range of 0-25

    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if char.isalpha():
            # Determine the ASCII offset
            ascii_offset = 65 if char.isupper() else 97
            # Compute the new position and wrap around if necessary
            new_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)


            
            result += new_char
        else:
            # Leave non-alphabetic characters unchanged
            result += char

            
    
    return result

def main():
    print("Caesar Cipher Program")
    print("=====================")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().lower()

    if choice in ['e', 'encrypt']:
        mode = 'encrypt'
    elif choice in ['d', 'decrypt']:
        mode = 'decrypt'
    else:
        print("Invalid choice. Exiting...")
        return

    message = input("Enter your message: ").strip()
    shift_value = int(input("Enter the shift value (integer): ").strip())

    # Perform the encryption or decryption
    result = caesar_cipher(message, shift_value, mode)
    print(f"The resulting text is: {result}")

if __name__ == "__main__":
    main()
