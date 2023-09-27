"""Hexadecimal can be used in such a way to represent ASCII strings. 
    First each letter is converted to an ordinal number according to the ASCII table (as in the previous challenge).
    Then the decimal numbers are converted to base-16 numbers, otherwise known as hexadecimal. 
    The numbers can be combined together, into one long hex string.
"""
hex = '63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d'
string =bytes.fromhex(hex).decode('utf-8') # bytes.fromhex(hex) -> get string from hex
# decode from bytes to string
print(string) 
# convert string to HEX
print(string.encode('utf-8').hex()) # string.encode('utf-8').hex() -> get hex from string