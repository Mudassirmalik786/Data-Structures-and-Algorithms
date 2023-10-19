# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 14:47:54 2023

@author: HP
"""

# 1st point in karatsuba.py


def multiply_integer(a, b):
    a_str = str(a)
    b_str = str(b)
    result = 0
    for i in range(len(b_str)):
        result += int(a_str) * int(b_str[i]) * 10 ** (len(b_str) - i - 1)
    
    return str(result)

# 2nd point in which we should take input as string

def multiply_string(a, b):
    result = multiply_integer(int(a), int(b))
    return result

# 3rd point in which we should vidualize multiplication

def visualize_multiplication(a, b):
    a_int = int(a)
    b_int = int(b)
    
    print(a_int)
    print(b_int)
    print("----")
    
    for i in range(len(b)):
        partial_product = a_int * int(b[i])
        print(f"{partial_product:<{len(a) + len(b) + 1 - i}}")
    
    print("-" * (len(a) + len(b) + 1))
    
    result = a_int * b_int
    print(result)

  
# 4rth point in which we should recursive multiplication
def multiply_recursive(a, b):
    # Base case: If either a or b is 0, return 0
    if a == "0" or b == "0":
        return "0"
    
    # Convert strings to integers

    
    # Recursive multiplication
    half_len = max(len(a), len(b)) // 2
    
    a_high = a[:-half_len]
    a_low = a[-half_len:]
    
    b_high = b[:-half_len]
    b_low = b[-half_len:]
    
    # Recursive calls for multiplication
    z0 = multiply_recursive(a_low, b_low)
    z1 = multiply_recursive(str(int(a_low) + int(a_high)), str(int(b_low) + int(b_high)))
    z2 = multiply_recursive(a_high, b_high)
    
    # Calculate the final result using the recursive formulas
    result = str(int(z2) * 10 ** (2 * half_len) + (int(z1) - int(z2) - int(z0)) * 10 ** half_len + int(z0))
    
    return result

# not working recursive multiplication

#%th pint in which we write karatsuba algorithm

def karatsuba_recursive(a, b):
    # Base case: If either a or b is 0, return 0
    if a == "0" or b == "0":
        return "0"
    
    # Convert strings to integers
    a_int = int(a)
    b_int = int(b)
    
    # Recursive multiplication using Karatsuba algorithm
    n = max(len(a), len(b))
    
    # If n is small, use regular multiplication
    if n < 2:
        return str(a_int * b_int)
    
    # Calculate the split position
    half_len = n // 2
    
    a_high = a[:-half_len]
    a_low = a[-half_len:]
    
    b_high = b[:-half_len]
    b_low = b[-half_len:]
    
    # Recursive calls for multiplication
    z0 = karatsuba_recursive(a_low, b_low)
    z1 = karatsuba_recursive(str(int(a_low) + int(a_high)), str(int(b_low) + int(b_high)))
    z2 = karatsuba_recursive(a_high, b_high)
    
    # Calculate the final result using the Karatsuba algorithm
    result = str(int(z2) * 10 ** (2 * half_len) + (int(z1) - int(z2) - int(z0)) * 10 ** half_len + int(z0))
    
    return result


def multiply2(x, y):
    # Validate inputs
    if not all(c in "01" for c in x) or not all(c in "01" for c in y):
        print("Invalid input for base 2.")
        return ""
    
    # Convert binary strings to integers and use the recursive multiplication function
    result = multiply_recursive(x, y)
    return result

# Karatsuba.py

def multiply16(x, y):
    valid_hex_chars = set("0123456789ABCDEFabcdef")
    if not all(c in valid_hex_chars for c in x) or not all(c in valid_hex_chars for c in y):
        print("Invalid input for base 16.")
        return ""
    
    # Convert hex strings to integers and use the recursive multiplication function
    result = multiply_recursive(int(x, 16), int(y, 16))
    return hex(int(result))[2:]  



'''
# Example usage for first point

first_integer = int(input("Enter a number: "))
second_integer = int(input("Enter second number: "))
result_int = multiply_integer(first_integer, second_integer)
print("Integer Multiplication:", result_int)

# Example usage for second point
result_str = multiply_string("123", "456")
print("String Multiplication:", result_str)

# Example usage for third point
visualize_multiplication("22", "45")

# Example usage for fourth point
result_recursive = multiply_recursive("123", "456")
print("Recursive Multiplication:", result_recursive)


# Example usage for 5th point
result_karatsuba = karatsuba_recursive("123", "456")
print("Karatsuba Multiplication:", result_karatsuba)

# Example usage for sixth point
result_base2 = multiply2("1101", "1010")
print("Base 2 Multiplication:", result_base2)

# Example usage for seventh point
result_base16 = multiply16("1AF", "B3")
print("Base 16 Multiplication:", result_base16) 
'''