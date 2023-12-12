alphabet = {'!': 8, ' ': 42, ',': 58, '.': 6, '1': 7, '0': 1, '3': 34, '2': 37, '5': 3, '4': 47, '7': 43, '6': 63, '9': 54, '8': 13, '?': 60, 'A': 35, 'C': 57, 'B': 16, 'E': 31, 'D': 64, 'G': 9, 'F': 23, 'I': 29, 'H': 32, 'K': 55, 'J': 53, 'M': 21, 'L': 5, 'O': 52, 'N': 41, 'Q': 40, 'P': 26, 'S': 22, 'R': 18, 'U': 51, 'T': 15, 'W': 17, 'V': 62, 'Y': 45, 'X': 66, 'Z': 50, 'a': 25, 'c': 38, 'b': 0, 'e': 30, 'd': 33, 'g': 14, 'f': 2, 'i': 10, 'h': 4, 'k': 59, 'j': 39, 'm': 11, 'l': 28, 'o': 12, 'n': 19, 'q': 24, 'p': 49, 's': 46, 'r': 61, 'u': 20, 't': 27, 'w': 36, 'v': 44, 'y': 56, 'x': 48, 'z': 65}
s = 'EgiMbrC7AbHOTyCiRJTU4eWlQwfgK4?fGQvzcjXBBw?NpxK6rv3OsObp?N9vjIqzHC?O9WwOT1VVtu32my2CzNNkHTozl5W,nE7Lm4rBJucP8XezREIuzgl0C7ANnn.561s9jBIYgECq!8XezREBDQ6sOG2i44iQIligvf9.Auk5hgNMuzREcjXzvPWrieWlQwfgK4km0xS?o0tuPB7VJo0t,nOwCUZAyxYyf0LvcfrIFmbPJDoAs9xaJA!cQF8?ffkln7SKO.h CVdc?JqPiAK9c8jt5Ck9ZAyrVP.y13pyC6OdvrN1dkHTseEgnDHQGEfKjBIf90KjAyFNBBwtXMaTZpbycC3HiqFp07SK44inxH5YAvEEml?CKjNQoCJwzNNbHOTyCnE7Lm4uZFCir'

# build new string froms to alphabet dict
new_s = ''
for c in s:
    new_s += str(alphabet[c])
    
# split new string into array of 2 by 2 and chr
new_s = [chr(int(new_s[i:i+2])) for i in range(0, len(new_s), 2)]
print(''.join(new_s))
print(ord('!'))