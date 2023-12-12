def bytes2matrix(text):
    """ Converts a 16-byte array into a 4x4 matrix.  """
    for i in range(0, len(text), 4):
        print(text[i:i+4])
    return [list(text[i:i+4]) for i in range(0, len(text), 4)]

def matrix2bytes(matrix):
    # return bytes from matrix 
    return bytes(sum(matrix, []))

matrix = [
    [99, 114, 121, 112],
    [116, 111, 123, 105],
    [110, 109, 97, 116],
    [114, 105, 120, 125],
]
print(bytes2matrix(b'crypto{inmatrix}'))
print(matrix2bytes(matrix))
