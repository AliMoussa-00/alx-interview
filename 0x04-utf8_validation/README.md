# UTF-8 validation

[task](https://drive.google.com/file/d/1GP1y8RIzo7-PTX4ZBtGFe0_j8JRoWjVD/view?usp=drive_link)

---

### Overview

In UTF-8, characters ranging from U+0000 to U+10FFFF are encoded using sequences of 1 to 4 bytes. Each byte in the sequence follows a specific pattern based on the character's Unicode code point.

- For a single-byte sequence, the higher-order bit of the octet is set to 0, and the remaining 7 bits encode the character number.
- For multi-byte sequences (2 to 4 bytes), the initial octet has the higher-order bits set to 1, followed by a 0 bit. Subsequent bytes have the higher-order bit set to 1 and the following bit set to 0, leaving the rest of the bits for encoding the character number.

The table below illustrates the format of these different octet types:

| Char. number range | UTF-8 octet sequence |
| --- | --- |
| 0000 0000-0000 007F | 0xxxxxxx |
| 0000 0080-0000 07FF | 110xxxxx 10xxxxxx |
| 0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx |
| 0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx |

Encoding a character to UTF-8 involves determining the number of octets required, preparing the high-order bits of the octets, and filling in the remaining bits with the character number.

### Explanation of Solution Code:

The provided solution code, a Python function named `validUTF8`, checks if a given set of data represents a valid UTF-8 encoding. Here's a breakdown:

1. The function iterates through each byte in the data set to determine the number of additional bytes needed for multi-byte characters.
  
2. It uses bitwise operations to inspect the leading bits of each byte, identifying whether it's the start byte of a UTF-8 sequence or a continuation byte.
  
3. If a byte is the start byte of a multi-byte sequence, the function calculates the number of additional bytes required.
  
4. For each continuation byte, it verifies that the leading bits match the pattern '10', indicating a valid continuation byte.
  
5. For single-byte characters, it ensures the most significant bit is zero.
  
6. The function returns `True` if the data set represents a valid UTF-8 encoding, and `False` otherwise.