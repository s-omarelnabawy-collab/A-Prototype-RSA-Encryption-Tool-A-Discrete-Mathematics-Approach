def gcd(a, b):
    while b != 0:
        temp_a = a
        temp_b = b
        remainder = temp_a % temp_b
        a = temp_b
        b = remainder
    return a


def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1

    remainder = b % a
    recursion_result = extended_gcd(remainder, a)

    gcd_val = recursion_result[0]
    x1 = recursion_result[1]
    y1 = recursion_result[2]

    quotient = b // a
    product = quotient * x1
    x = y1 - product
    y = x1

    return gcd_val, x, y


def mod_inverse(e, phi):
    result = extended_gcd(e, phi)
    gcd_val = result[0]
    x = result[1]
    y = result[2]

    if gcd_val != 1:
        raise ValueError("The multiplicative inverse does not exist.")

    inverse = x % phi
    return inverse


def encrypt(message, e, n):
    encrypted_list = []
    for i in range(len(message)):
        current_char = message[i]
        numerical_value = ord(current_char)

        cipher_value = pow(numerical_value, e, n)

        encrypted_list.append(cipher_value)

    return encrypted_list


def decrypt(ciphertext_list, d, n):
    decrypted_chars_list = []

    list_length = len(ciphertext_list)
    for i in range(list_length):
        current_cipher = ciphertext_list[i]
        cipher_int = int(current_cipher)

        decrypted_numeric = pow(cipher_int, d, n)

        decrypted_char = chr(decrypted_numeric)

        decrypted_chars_list.append(decrypted_char)

    final_string = ""
    for char in decrypted_chars_list:
        final_string = final_string + char

    return final_string