# UTF-8 validation

[task]()

---

## What is UTF-8?

UTF-8 is a character encoding standard used to represent text in computers. It allows computers to understand and display a wide range of characters, including letters, numbers, symbols, and emojis, from various languages and scripts around the world.

## How does UTF-8 work?

- **Basic Characters**: Simple characters like English letters and numbers are represented by a single byte (8 bits).
  
  - Example: 'A' is represented as `01000001`, and '5' is `00110101`.
- **Fancy Characters**: Complex characters like emojis or special symbols require multiple bytes. Each byte contains 8 bits.
  
  - Example: The thumbs-up emoji '👍' might be represented by several bytes: `11100010 10011111 10011001`.

## Why is UTF-8 important?

UTF-8 ensures that computers and the internet can handle text from different languages and scripts, making communication and data exchange globally accessible. It's the backbone of multilingual support in software, ensuring that text displays correctly, regardless of language or script.

## How to Use this Information

Understanding UTF-8 is crucial for developers, especially when working with text-based data or internationalization. By implementing UTF-8 support in your applications, you can ensure compatibility with various languages and scripts, providing a better user experience for a diverse audience.

For more information on UTF-8 and character encoding, refer to the official Unicode website and documentation.

---

Sure! Here's the README text with examples for each bitwise operation:

---

# Bitwise Operations in Python

Bitwise operations in Python are used to manipulate individual bits of integers or other data types at the binary level. These operations work directly with the binary representation of numbers. Understanding bitwise operations can be helpful for tasks such as optimizing code, working with low-level data, or implementing specific algorithms.

## Commonly Used Bitwise Operations

### 1. Bitwise AND (`&`)

- **Description**: Performs a logical AND operation on corresponding bits of two integers. The result is 1 if both bits are 1, otherwise, it's 0.
  
- **Example**:
  
  ```python
  a = 0b1010  # binary representation of 10
  b = 0b1100  # binary representation of 12
  result = a & b  # bitwise AND operation
  print(bin(result))  # Output: 0b1000 (binary representation of 8)
  ```
  

### 2. Bitwise OR (`|`)

- **Description**: Performs a logical OR operation on corresponding bits of two integers. The result is 1 if at least one of the bits is 1.
  
- **Example**:
  
  ```python
  a = 0b1010  # binary representation of 10
  b = 0b1100  # binary representation of 12
  result = a | b  # bitwise OR operation
  print(bin(result))  # Output: 0b1110 (binary representation of 14)
  ```
  

### 3. Bitwise XOR (`^`)

- **Description**: Performs a logical XOR (exclusive OR) operation on corresponding bits of two integers. The result is 1 if the bits are different, otherwise, it's 0.
  
- **Example**:
  
  ```python
  a = 0b1010  # binary representation of 10
  b = 0b1100  # binary representation of 12
  result = a ^ b  # bitwise XOR operation
  print(bin(result))  # Output: 0b0110 (binary representation of 6)
  ```
  

### 4. Bitwise NOT (`~`)

- **Description**: Performs a unary bitwise NOT operation, which inverts all the bits of the integer.
  
- **Example**:
  
  ```python
  a = 0b1010  # binary representation of 10
  result = ~a  # bitwise NOT operation
  print(bin(result))  # Output: -0b1011 (binary representation of -11)
  ```
  

### 5. Left Shift (`<<`)

- **Description**: Shifts the bits of the integer to the left by a specified number of positions, filling the vacant positions with zeros.
  
- **Example**:
  
  ```python
  a = 0b1010  # binary representation of 10
  result = a << 2  # left shift by 2 positions
  print(bin(result))  # Output: 0b101000 (binary representation of 40)
  ```
  

### 6. Right Shift (`>>`)

- **Description**: Shifts the bits of the integer to the right by a specified number of positions, filling the vacant positions with zeros (for unsigned integers) or the sign bit (for signed integers).
  
- **Example**:
  
  ```python
  a = 0b1010  # binary representation of 10
  result = a >> 1  # right shift by 1 position
  print(bin(result))  # Output: 0b101 (binary representation of 5)
  ```
  

---

## UTF-8

### Valid Ranges

the ranges of Unicode code points and the corresponding number of bytes needed for UTF-8 encoding:

1. **Basic ASCII Characters (U+0000 to U+007F)**:
  
  - Range: 0000–007F
  - Number of bytes: 1 byte
2. **Extended Characters (U+0080 to U+07FF)**:
  
  - Range: 0080–07FF
  - Number of bytes: 2 bytes
3. **Characters in Supplementary Planes (U+0800 to U+FFFF)**:
  
  - Range: 0800–FFFF
  - Number of bytes: 3 bytes
4. **Characters in Supplementary Planes (U+10000 to U+10FFFF)**:
  
  - Range: 10000–10FFFF
  - Number of bytes: 4 bytes

### Invalid range:

For example, consider the byte sequence `C3 28`.

The byte sequence "C3 28" is not a valid UTF-8 encoding because it does not follow the UTF-8 encoding rules. In UTF-8 encoding:

- **Single-byte** characters (ASCII characters) always start with a `0` bit.
- **Multi-byte** characters always start with specific bit patterns indicating the number of bytes used for the character.

Let's analyze "C3 28":

- "C3" in binary is `11000011`.
- "28" in binary is `00101000`.

The first byte "C3" indicates the start of a multi-byte character because it starts with `110`. However, the second byte "28" starts with `0`, which is not the expected continuation pattern for multi-byte characters in UTF-8 encoding.

Therefore, "C3 28" is not a valid UTF-8 encoding. Each byte in a UTF-8 encoded character must follow the rules for UTF-8 encoding to represent valid characters correctly.

### !! needed bits

**!! each number of bytes in utf-8 has a certain pattern**

- `1 bytes` => `0 + 7bits`
  
- `more : 2 to 4 bytes` => the first byte will start by number of bytes and 0 and the rest of bytes will start with 10
  
- `1 byte` => `7 bits` from binary code, starts with `0` => 
  `U+0024 010 0100 00100100 24`
  
- `2 bytes` => `11 bits` from binary code:
  `U+00A3 1010 0011 11000010 10100011 C2 A3`
  

if number of bits not sufficient we add `0`

- `3 bytes` => `16 bits`
  `U+0939 0000 1001 0011 1001 11100000 10100100 10111001 E0 A4 B9`
  
- `4 bytes` => `21 bits`
  `U+10348 0 0001 0000 0011 0100 1000 11110000 10010000 10001101 10001000 F0 90 8D 88`
  

#### [Example]([UTF-8 - Wikipedia](https://en.wikipedia.org/wiki/UTF-8#Examples))