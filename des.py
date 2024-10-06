from random import randint

ip = [57, 49, 41, 33, 25, 17, 9,  1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7,
      56, 48, 40, 32, 24, 16, 8,  0,
      58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6]

expansion_table = [
    31,  0,  1,  2,  3,  4,
    3,  4,  5,  6,  7,  8,
    7,  8,  9, 10, 11, 12,
    11, 12, 13, 14, 15, 16,
    15, 16, 17, 18, 19, 20,
    19, 20, 21, 22, 23, 24,
    23, 24, 25, 26, 27, 28,
    27, 28, 29, 30, 31,  0
]

pc1 = [56, 48, 40, 32, 24, 16, 8,
        0, 57, 49, 41, 33, 25, 17,
        9, 1, 58, 50, 42, 34, 26,
        18, 10, 2, 59, 51, 43, 35,
        62, 54, 46, 38, 30, 22, 14,
        6, 61, 53, 45, 37, 29, 21,
        13, 5, 60, 52, 44, 36, 28,
        20, 12, 4, 27, 19, 11, 3]

left_rotations = [
    1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1
]

pc2 = [13, 16, 10, 23, 0, 4,
       2, 27, 14, 5, 20, 9,
       22, 18, 11, 3, 25, 7,
       15, 6, 26, 19, 12, 1,
       40, 51, 30, 36, 46, 54,
       29, 39, 50, 44, 32, 47,
       43, 48, 38, 55, 33, 52,
       45, 41, 49, 35, 28, 31]

fp = [
    39,  7, 47, 15, 55, 23, 63, 31,
    38,  6, 46, 14, 54, 22, 62, 30,
    37,  5, 45, 13, 53, 21, 61, 29,
    36,  4, 44, 12, 52, 20, 60, 28,
    35,  3, 43, 11, 51, 19, 59, 27,
    34,  2, 42, 10, 50, 18, 58, 26,
    33,  1, 41,  9, 49, 17, 57, 25,
    32,  0, 40,  8, 48, 16, 56, 24
]

sbox = [
    # S1
    [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
     0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
     4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
     15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],

    # S2
    [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
     3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
     0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
     13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],

    # S3
    [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8,
     13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
     13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
     1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],

    # S4
    [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
     13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
     10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4,
     3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],

    # S5
    [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
     14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
     4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
     11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],

    # S6
    [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11,
     10, 15, 4, 2, 1, 9, 14, 7, 6, 0, 8, 13, 3, 11, 5, 12,
     9, 14, 15, 8, 3, 0, 5, 6, 1, 13, 11, 2, 12, 7, 4, 10,
     3, 11, 8, 12, 7, 4, 2, 9, 15, 10, 1, 6, 0, 13, 5, 14],

    # S7
    [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
     13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
     1, 4, 11, 13, 12, 7, 0, 10, 14, 9, 2, 15, 8, 3, 5, 6,
     10, 3, 12, 0, 8, 14, 9, 1, 7, 11, 5, 4, 15, 2, 6, 13],

    # S8
    [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
     1, 15, 13, 8, 10, 3, 4, 2, 11, 6, 12, 5, 9, 14, 0, 7,
     5, 3, 9, 6, 10, 11, 1, 15, 13, 4, 2, 8, 12, 7, 0, 14,
     7, 11, 2, 15, 3, 10, 1, 9, 8, 12, 6, 4, 14, 0, 5, 13]
]

def text_to_bits(text):
    return [int(bit) for char in text for bit in bin(ord(char))[2:].zfill(8)]

def bits_to_text(bits):
    chars = [chr(int(''.join(map(str, bits[i:i+8])), 2)) for i in range(0, len(bits), 8)]
    return ''.join(chars)

def permute(bits, table):
    return [bits[i] for i in table]

def left_rotate(bits, rotations):
    return bits[rotations:] + bits[:rotations]

def generate_keys(key):
    key = permute(text_to_bits(key), pc1)
    left, right = key[:28], key[28:]
    keys = []

    for rotation in left_rotations:
        left = left_rotate(left, rotation)
        right = left_rotate(right, rotation)
        keys.append(permute(left + right, pc2))
    return keys

def feistel_function(right, subkey):
    expanded = permute(right, expansion_table)
    xor_result = [expanded[i] ^ subkey[i] for i in range(48)]
    sbox_output = []

    for i in range(8):
        row = (xor_result[i * 6] << 1) | xor_result[i * 6 + 5]
        col = int(''.join(map(str, xor_result[i * 6 + 1:i * 6 + 5])), 2)
        sbox_output += list(map(int, bin(sbox[i][row * 16 + col])[2:].zfill(4)))

    return permute(sbox_output, [i for i in range(32)])

def encrypt(plaintext, key):
    keys = generate_keys(key)
    bits = permute(text_to_bits(plaintext), ip)
    left, right = bits[:32], bits[32:]

    for i in range(16):
        temp = right
        right = [left[j] ^ feistel_function(right, keys[i])[j] for j in range(32)]
        left = temp

    return bits_to_text(permute(right + left, fp))

def decrypt(ciphertext, key):
    keys = generate_keys(key)
    bits = permute(text_to_bits(ciphertext), ip)
    left, right = bits[:32], bits[32:]

    for i in range(15, -1, -1):
        temp = right
        right = [left[j] ^ feistel_function(right, keys[i])[j] for j in range(32)]
        left = temp

    return bits_to_text(permute(right + left, fp))


def main():
    while True:
        print("DES Encryption and Decryption")
        choice = input("Pilih Opsi (1: Encrypt, 2: Decrypt, 3: Exit): ")
        if choice == '1':
            plaintext = input("Masukkan plaintext: ")
            key = input("Masukkan key (8 characters): ")
            ciphertext = encrypt(plaintext, key)
            print(f"Ciphertext: {ciphertext}")
        elif choice == '2':
            ciphertext = input("Masukkan ciphertext: ")
            key = input("Masukkan key (8 characters): ")
            plaintext = decrypt(ciphertext, key)
            print(f"Plaintext: {plaintext}")
        elif choice == '3':
            break
        else:
            print("Pilihan Error")

if __name__ == "__main__":
    main()