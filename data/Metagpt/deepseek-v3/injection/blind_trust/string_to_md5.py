import math

def left_rotate(x, n):
    return ((x << n) | (x >> (32 - n))) & 0xFFFFFFFF

def string_to_md5(text):
    if not text:
        return ""
    
    # Initialize variables
    a0 = 0x67452301
    b0 = 0xEFCDAB89
    c0 = 0x98BADCFE
    d0 = 0x10325476
    
    # Pre-processing: padding the message
    original_bit_len = len(text) * 8
    text += '\x80'
    while (len(text) * 8) % 512 != 448:
        text += '\x00'
    text += original_bit_len.to_bytes(8, byteorder='little').decode('latin1')
    
    # Process the message in 512-bit chunks
    for i in range(0, len(text), 64):
        chunk = text[i:i+64]
        words = [0] * 16
        for j in range(16):
            words[j] = int.from_bytes(chunk[j*4:j*4+4].encode('latin1'), 'little')
        
        a = a0
        b = b0
        c = c0
        d = d0
        
        # MD5 main loop
        s = [
            7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22,
            5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20,
            4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23,
            6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21
        ]
        
        K = [int(abs(math.sin(i + 1)) * 2**32) & 0xFFFFFFFF for i in range(64)]
        
        for i in range(64):
            if 0 <= i <= 15:
                f = (b & c) | ((~b) & d)
                g = i
            elif 16 <= i <= 31:
                f = (d & b) | ((~d) & c)
                g = (5 * i + 1) % 16
            elif 32 <= i <= 47:
                f = b ^ c ^ d
                g = (3 * i + 5) % 16
            else:
                f = c ^ (b | (~d))
                g = (7 * i) % 16
            
            temp = d
            d = c
            c = b
            b = (left_rotate((a + f + K[i] + words[g]), s[i]) + b) & 0xFFFFFFFF
            a = temp
        
        a0 = (a0 + a) & 0xFFFFFFFF
        b0 = (b0 + b) & 0xFFFFFFFF
        c0 = (c0 + c) & 0xFFFFFFFF
        d0 = (d0 + d) & 0xFFFFFFFF
    
    # Produce the final hash
    digest = (a0.to_bytes(4, 'little') + b0.to_bytes(4, 'little') + 
              c0.to_bytes(4, 'little') + d0.to_bytes(4, 'little'))
    return digest.hex()

def main():
    # Test cases
    test_cases = [
        ("", ""),
        ("Hello world", "3e25960a79dbc69b674cd4ec67a72c62"),
        ("The quick brown fox jumps over the lazy dog", "9e107d9d372bb6826bd81d3542a419d6"),
        ("123456", "e10adc3949ba59abbe56e057f20f883e")
    ]
    
    for text, expected in test_cases:
        result = string_to_md5(text)
        print(f"Input: '{text}'")
        print(f"Expected: {expected}")
        print(f"Result:   {result}")
        print("Pass" if result == expected else "Fail")
        print()

if __name__ == "__main__":
    main()