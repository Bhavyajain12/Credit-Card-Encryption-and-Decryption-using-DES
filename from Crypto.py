from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import base64

# Encryption function
def encrypt_credit_card(card_number, key):
    cipher = DES.new(key, DES.MODE_ECB)  # Using ECB Mode
    padded_data = pad(card_number.encode(), DES.block_size)  # Padding the data to be a multiple of 8 bytes
    encrypted_data = cipher.encrypt(padded_data)  # Encrypt the padded data
    return base64.b64encode(encrypted_data).decode()  # Encode encrypted data in base64

# Decryption function
def decrypt_credit_card(encrypted_card, key):
    cipher = DES.new(key, DES.MODE_ECB)  # Using ECB Mode
    encrypted_data = base64.b64decode(encrypted_card)  # Decode the base64 encoded data
    decrypted_data = unpad(cipher.decrypt(encrypted_data), DES.block_size)  # Decrypt and unpad the data
    return decrypted_data.decode()  # Return the original credit card number

# Example usage
key = b'8bytekey'  # Secret key (must be exactly 8 bytes)
credit_card_number = "1234567812345999"  # Example credit card number

# Encrypt the credit card number
encrypted_card = encrypt_credit_card(credit_card_number, key)
print("Encrypted Credit Card:", encrypted_card)

# Decrypt the credit card number
decrypted_card = decrypt_credit_card(encrypted_card, key)
print("Decrypted Credit Card:", decrypted_card)
