#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8

data = [65]
print(validUTF8(data))

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))

data = [229, 65, 127, 256]
print(validUTF8(data))

print("#" * 56)

data = [195, 164]  # UTF-8 representation of 'ä' (U+00E4)
print(validUTF8(data))  # Expected output: True

data = [128]  # Invalid single-byte character
print(validUTF8(data))  # Expected output: False

data = [195, 65]  # Invalid continuation byte
print(validUTF8(data))  # Expected output: False

data = [195]  # Incomplete multi-byte character sequence
print(validUTF8(data))  # Expected output: False

data = [195, 128]  # Overlong encoding of 'ä'
print(validUTF8(data)) # Expected output: False