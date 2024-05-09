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

data = integers_list = [20013, 26085, 12354, 128512, 129300]
print(validUTF8(data))

data = integers_list = [66376]
print(validUTF8(data))

print("#" * 50)

# # Test case 1: Empty data set
# data1 = []
# print(validUTF8(data1))  # Expected: False

# # Test case 2: Data set with single-byte characters
# data2 = [65, 97, 48, 33, 127]
# print(validUTF8(data2))  # Expected: True

# # Test case 4: Data set with multi-byte characters (invalid UTF-8)
# data4 = [20013, 26085, 12354, 128512, 129300]
# print(validUTF8(data4))  # Expected: False

# # Test case 5: Data set with invalid byte sequences
# data5 = [300, 5000, 65536, 123456789]
# print(validUTF8(data5))  # Expected: False

# # Test case 6: Data set with single byte character but invalid
# data6 = [192]
# print(validUTF8(data6))  # Expected: False
