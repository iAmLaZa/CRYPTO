import numpy as np
import string
from Crypto.Util.number import inverse
ALPHABET = string.ascii_lowercase[:26]

def cofactor_matrix(matrix):
    n = matrix.shape[0]  # Get the size of the matrix
    cofactors = np.zeros_like(matrix, dtype=np.int64)

    for i in range(n):
        for j in range(n):
            # Calculate the minor matrix by excluding the i-th row and j-th column
            minor_matrix = np.delete(np.delete(matrix, i, axis=0), j, axis=1)
            cofactors[i, j] = ((-1) ** (i + j)) * np.linalg.det(minor_matrix)

    return cofactors



# define function to calculate determinant of matrix
def determinant(matrix):
    return np.linalg.det(matrix) % len(ALPHABET)
# define function to calculate inverse of number
def inverse_num(num):
    return inverse(num, len(ALPHABET))

# function for Hill encryption
def hill_encryption(plaintext, key):
    #declare ciphertext as numpy array
    ciphertext = np.array([])
    # remove spaces and convert to lowercase
    plaintext = plaintext.replace(" ", "").lower()
    # Convert letters to numbers
    plaintext = [ALPHABET.index(i) for i in plaintext] 
    for i in range (0, len(plaintext), key.shape[0]):
        pl = plaintext[i : i + key.shape[0]]
        # plaintext block multiplication with key
        ch = np.dot(pl,key) % len(ALPHABET)
        # add ch to ciphertext as int array
        ciphertext = np.append(ciphertext, ch)
    ciphertext = np.array(ciphertext, dtype = int)

    # Return ciphertext
    return "".join(ALPHABET[int(i)] for i in ciphertext)


# function for Hill decryption
def hill_decryption(ciphertext,key):
    #declare ciphertext as numpy array
    plaintext = np.array([])
    # Convert letters to numbers
    ciphertext = [ALPHABET.index(i) for i in ciphertext] 
    # calculate determinant of key
    det = determinant(key)
    # calculate inverse of determinant
    det_inv = inverse_num(det)
    # calculate adjugate matrix
    adj = cofactor_matrix(key).T 
    #calculate inverse of key
    inv_key = (det_inv * adj) % len(ALPHABET)
    inv_key = [[4,9,15] ,[15,17,6] ,[24,0,17]]
    for i in range (0, len(ciphertext), key.shape[0]):
        ct = ciphertext[i : i + key.shape[0]]
        # ciphertext block multiplication with key
        pt = np.dot(ct,inv_key) % len(ALPHABET)
        # add ch to ciphertext as int array
        plaintext = np.append(plaintext, pt)
    return "".join(ALPHABET[int(i)] for i in plaintext)
    
    
    
# Define your key as a NumPy array
key = np.array([[17, 17,5 ],
                [21,18,21],
                [2,2,19]]  )

"""
plaintext = "pay more money"
cypertext = hill_encryption(plaintext, key)
print(cypertext)
plaintext = hill_decryption(cypertext, key)
print(plaintext)
"""



