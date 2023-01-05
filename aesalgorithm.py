from Crypto.Cipher import AES

# Set the key and initialization vector
key = b'0123456789abcdef'
iv = b'fedcba9876543210'

# Create the cipher object and encrypt the message
cipher = AES.new(key, AES.MODE_CFB, iv)
encrypted_message = cipher.encrypt(b'Hello, World!')

# Print the encrypted message
print(encrypted_message)

# Decrypt the message
decrypted_message = cipher.decrypt(encrypted_message)

# Print the decrypted message
print(decrypted_message)
