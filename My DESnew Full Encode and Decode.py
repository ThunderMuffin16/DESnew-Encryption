# Here are all the tables used in the program as arrays
# Initial permutation order
IP = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

# Final permutation order
FP = [40, 8, 48, 16, 56, 24, 64, 32,
      39, 7, 47, 15, 55, 23, 63, 31,
      38, 6, 46, 14, 54, 22, 62, 30,
      37, 5, 45, 13, 53, 21, 61, 29,
      36, 4, 44, 12, 52, 20, 60, 28,
      35, 3, 43, 11, 51, 19, 59, 27,
      34, 2, 42, 10, 50, 18, 58, 26,
      33, 1, 41, 9, 49, 17, 57, 25]

# Permutation choice 1
PC1 = [57, 49, 41, 33, 25, 17, 9,
       1, 58, 50, 42, 34, 26, 18,
       10, 2, 59, 51, 43, 35, 27,
       19, 11, 3, 60, 52, 44, 36,
       63, 55, 47, 39, 31, 23, 15,
       7, 62, 54, 46, 38, 30, 22,
       14, 6, 61, 53, 45, 37, 29,
       21, 13, 5, 28, 20, 12, 4]

# Permutation choice 2
PC2 = [14, 17, 11, 24, 1, 5,
       3, 28, 15, 6, 21, 10,
       23, 19, 12, 4, 26, 8,
       16, 7, 27, 20, 13, 2,
       41, 52, 31, 37, 47, 55,
       30, 40, 51, 45, 33, 48,
       44, 49, 39, 56, 34, 53,
       46, 42, 50, 36, 29, 32]

# Expansion table
E = [32, 1, 2, 3, 4, 5,
     4, 5, 6, 7, 8, 9,
     8, 9, 10, 11, 12, 13,
     12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21,
     20, 21, 22, 23, 24, 25,
     24, 25, 26, 27, 28, 29,
     28, 29, 30, 31, 32, 1]

# S-boxes (substitution boxes)
SBOX = [
    # S1
    [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
     [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
     [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
     [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],
    # S2
    [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
     [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
     [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
     [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],
    # S3
    [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
     [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
     [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
     [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],
    # S4
    [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
     [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
     [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
     [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],
    # S5
    [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
     [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
     [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
     [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],
    # S6
    [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
     [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
     [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
     [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],
    # S7
    [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
     [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
     [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
     [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],
    # S8
    [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
     [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
     [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
     [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]
]

# Permutation (P) after S-box substitution
P = [16, 7, 20, 21, 29, 12, 28, 17,
     1, 15, 23, 26, 5, 18, 31, 10,
     2, 8, 24, 14, 32, 27, 3, 9,
     19, 13, 30, 6, 22, 11, 4, 25]

# Shift schedule for key schedule
SHIFT = [1, 1, 2, 2, 2, 2, 2, 2,
         1, 2, 2, 2, 2, 2, 2, 1]


# This variable is so when I want to change the amount of rounds preformed I only need to change one number
rounds2do = 16


# Here are a few methods to reduce the amount of times a line of code must be written
# I used this post, https://medium.com/@ziaullahrajpoot/data-encryption-standard-des-dc8610aafdb3, to get all the tables so I would
# not have to type them all out myself and potentially miss label something, I also used this persons program to understand how the
# process of DES worked so I could bring it into my own program

# This will take an input string and will translate each character into its binary equivalent
def string_to_binary(string):
    return ''.join(format(ord(c), '08b') for c in string)

def binary_to_string(binary_string):
    # Split the binary string into chunks of 8 bits
    chars = [binary_string[i:i+8] for i in range(0, len(binary_string), 8)]
    # Convert each chunk to a character and join them
    return ''.join(chr(int(char, 2)) for char in chars)

# Create all subkeys here from the initial input key
def getSubKey(key):
    binaryKey = string_to_binary(key)   
    pc1Key = ''.join([binaryKey[x-1] for x in PC1])

    leftKey, rightKey = pc1Key[:28], pc1Key[28:]
    subkeys = []
    for shift_count in SHIFT:
        leftKey = leftKey[shift_count:] + leftKey[:shift_count]
        rightKey = rightKey[shift_count:] + rightKey[:shift_count]

        joined = leftKey + rightKey

        round_keys = ''.join([joined[x-1] for x in PC2])
        subkeys.append(round_keys)
    return subkeys

# Here is the main encryption algorithm

def encryption(user_str, key1, key2):
    binary_user_str = string_to_binary(user_str)

    # Getting the subkeys
    subkeys1 = getSubKey(key1)
    subkeys2 = getSubKey(key2)

    # Split input from 128 bits into two 64 bit halves
    P1 = binary_user_str[:64] 
    P2 = binary_user_str[64:]

    #  These halves are then given and a regular DES round is run with each one
    P1 = ''.join([P1[x-1] for x in IP])
    P2 = ''.join([P2[x-1] for x in IP])

    # Splitting Parts 1 and 2 in half to run normal DES rounds on them
    P1left = P1[:32]
    P1right = P1[32:]

    P2left = P2[:32]
    P2right = P2[32:]

    for i in range(rounds2do):
        # Part 1 DES round
        # Expand right side from 32 bits to 48 bits
        P1rightExpand = ''.join([P1right[x-1] for x in E])

        # Now it can be XORed with the 48 bit subkey
        P1rightXor = ""
        for j in range(48):
            if P1rightExpand[j] != subkeys1[i][j]:
                P1rightXor += "1"
            else:
                P1rightXor += "0"

        # The XORed result is then run through the s-box and transformed back to 32 bits
        P1rightSub = ""
        for k in range(8):
            start = k * 6
            end = (k + 1) * 6
            block = P1rightXor[start:end]

            row_bits = block[0] + block[5]
            row = int(row_bits, 2)

            col_bits = block[1:5]
            col = int(col_bits, 2)

            sbox_value = SBOX[k][row][col]

            P1rightSub += format(sbox_value,"04b")

        # Permutation is run to reorganize the bits before a final XOR
        P1rightFunction = ''.join([P1rightSub[x-1] for x in P])

        # Another XOR is now run over the 32 bit right side using the left side
        P1newRight = ''
        for l in range(32):
            if P1left[l] != P1rightFunction[l]:
                P1newRight += "1"
            else:
                P1newRight += "0"

        # The left is replaced by the unaltered right while the data we have been working on becomes the new right side
        P1left = P1right
        P1right = P1newRight



        # Part 2 DES round
        # Expand right side from 32 bits to 48 bits
        P2rightExpand = ''.join([P2right[x-1] for x in E])

        # Now it can be XORed with the 48 bit subkey
        P2rightXor = ""
        for j in range(48):
            if P2rightExpand[j] != subkeys2[i][j]:
                P2rightXor += "1"
            else:
                P2rightXor += "0"

        # The XORed result is then run through the s-box and transformed back to 32 bits
        P2rightSub = ""
        for k in range(8):
            start = k * 6
            end = (k + 1) * 6
            block = P2rightXor[start:end]

            row_bits = block[0] + block[5]
            row = int(row_bits, 2)

            col_bits = block[1:5]
            col = int(col_bits, 2)

            sbox_value = SBOX[k][row][col]

            P2rightSub += format(sbox_value,"04b")

        # Permutation is run to reorganize the bits before a final XOR
        P2rightFunction = ''.join([P2rightSub[x-1] for x in P])

        # Another XOR is now run over the 32 bit right side using the left side
        P2newRight = ''
        for l in range(32):
            if P2left[l] != P2rightFunction[l]:
                P2newRight += "1"
            else:
                P2newRight += "0"

        # The left is replaced by the unaltered right while the data we have been working on becomes the new right side
        P2left = P2right
        P2right = P2newRight
       
        # This is where the complexity and extra security comes from in this algorithm as the left sides of both data halves are swapped before the next round
        temp = P1left
        P1left = P2left
        P2left = temp

    # Final string assembly is done right, left to correct for the swap that happens each round except for the least
    P1_final = P1right + P1left
    P2_final = P2right + P2left

    # The final permutation table is run over the two halves seperately
    P1_return = ''.join([P1_final[x-1] for x in FP])
    P2_return = ''.join([P2_final[x-1] for x in FP])

    # And lastly they are converted from binary to ASCII and given back to the call
    P1_text = binary_to_string(P1_return)
    P2_text = binary_to_string(P2_return)

    return P1_text + P2_text

def decryption(user_str, key1, key2):
    # The beginning of decryption looks identicle to encryption because the data needs to be set up in the same way
    binary_user_str = string_to_binary(user_str)

    subkeys1 = getSubKey(key1)
    subkeys2 = getSubKey(key2)

    P1 = binary_user_str[:64]
    P2 = binary_user_str[64:]

    P1 = ''.join([P1[x-1] for x in IP])
    P2 = ''.join([P2[x-1] for x in IP])

    P1left = P1[:32]
    P1right = P1[32:]
    P2left = P2[:32]
    P2right = P2[32:]
    

    for i in range(rounds2do):
        # Here is the first major difference from the encryption algorithm as the steps must be mirrored, we swap the right sides not the left
        temp = P1right
        P1right = P2right
        P2right = temp

        # Part 1 DES round
        # Expand right side from 32 bits to 48 bits
        P1rightExpand = ''.join([P1right[x-1] for x in E])

        # Now it can be XORed with the 48 bit subkey
        P1rightXor = ""
        for j in range(48):
            # Here is the other change to decryption as we must work through our subkeys in reverse, this is done by subtracting the amount
            # rounds being done (minus one since arrays start at 0) by the current round number
            if P1rightExpand[j] != subkeys1[(rounds2do-1)-i][j]:
                P1rightXor += "1"
            else:
                P1rightXor += "0"

        # The XORed result is then run through the s-box and transformed back to 32 bits
        P1rightSub = ""
        for k in range(8):
            start = k * 6
            end = (k + 1) * 6
            block = P1rightXor[start:end]

            row_bits = block[0] + block[5]
            row = int(row_bits, 2)

            col_bits = block[1:5]
            col = int(col_bits, 2)

            sbox_value = SBOX[k][row][col]

            P1rightSub += format(sbox_value,"04b")

        # Permutation is run to reorganize the bits before a final XOR
        P1rightFunction = ''.join([P1rightSub[x-1] for x in P])

        # Another XOR is now run over the 32 bit right side using the left side
        P1newRight = ''
        for l in range(32):
            if P1left[l] != P1rightFunction[l]:
                P1newRight += "1"
            else:
                P1newRight += "0"

        # The left is replaced by the unaltered right while the data we have been working on becomes the new right side
        P1left = P1right
        P1right = P1newRight




        # Expand right side from 32 bits to 48 bits
        P2rightExpand = ''.join([P2right[x-1] for x in E])

        # Now it can be XORed with the 48 bit subkey
        P2rightXor = ""
        for j in range(48):
            if P2rightExpand[j] != subkeys2[(rounds2do-1)-i][j]:
                P2rightXor += "1"
            else:
                P2rightXor += "0"

        # The XORed result is then run through the s-box and transformed back to 32 bits
        P2rightSub = ""
        for k in range(8):
            start = k * 6
            end = (k + 1) * 6
            block = P2rightXor[start:end]

            row_bits = block[0] + block[5]
            row = int(row_bits, 2)

            col_bits = block[1:5]
            col = int(col_bits, 2)

            sbox_value = SBOX[k][row][col]

            P2rightSub += format(sbox_value,"04b")

        # Permutation is run to reorganize the bits before a final XOR
        P2rightFunction = ''.join([P2rightSub[x-1] for x in P])

        # Another XOR is now run over the 32 bit right side using the left side
        P2newRight = ''
        for l in range(32):
            if P2left[l] != P2rightFunction[l]:
                P2newRight += "1"
            else:
                P2newRight += "0"

        # The left is replaced by the unaltered right while the data we have been working on becomes the new right side
        P2left = P2right
        P2right = P2newRight

    # The same final assembly process is then done and the result given back
    P1_final = P1right + P1left
    P2_final = P2right + P2left

    P1_return = ''.join([P1_final[x-1] for x in FP])
    P2_return = ''.join([P2_final[x-1] for x in FP])

    P1_text = binary_to_string(P1_return)
    P2_text = binary_to_string(P2_return)

    return P1_text + P2_text

# Here is the main segment of code that gets run at the start

# Get phrase from users
MA_input = input("Please enter a phrase 16 characters long. (This includes spaces):")
while len(MA_input) != 16:
    if len(MA_input)< 16:
        print(f"Please make input {16-len(MA_input)} characters longer\n")
        MA_input = input("Please enter a phrase 16 characters long. (This includes spaces):")
    else:
        print(f"Please make input {len(MA_input)-16} characters shorter\n")
        MA_input = input("Please enter a phrase 16 characters long. (This includes spaces):")


# Get keys from user, you can choose to omit this portion and hard code keys if desired
MA_key1 = input("Please enter first key that is 8 charaters long:")

while len(MA_key1) != 8:
    if len(MA_key1)< 8:
        print(f"Please make input {8-len(MA_key1)} characters longer\n")
        MA_key1 = input("Please enter a key 8 characters long. (This includes spaces):")
    else:
        print(f"Please make input {len(MA_key1)-8} characters shorter\n")
        MA_key1 = input("Please enter a key 8 characters long. (This includes spaces):")

MA_key2 = input("Please enter second key that is 8 charaters long:")

while len(MA_key2) != 8:
    if len(MA_key2)< 8:
        print(f"Please make input {8-len(MA_key2)} characters longer\n")
        MA_key2 = input("Please enter a key 8 characters long. (This includes spaces):")
    else:
        print(f"Please make input {len(MA_key2)-8} characters shorter\n")
        MA_key2 = input("Please enter a key 8 characters long. (This includes spaces):")

cipherText = encryption(MA_input, MA_key1, MA_key2)

print("Encrypted input:", cipherText, "\n")

plainText = decryption(cipherText, MA_key1, MA_key2)

print("\nDecrypted:", plainText)