def quadratic_residues(n):
    residues = []
    for x in range(n):
        residue = (x ** 2) % n
        residues.append(residue)
    return residues

# Define the modulus 'n' for which you want to find quadratic residues
n = 29

# Calculate quadratic residues modulo 'n'
residues = quadratic_residues(n)
print(f"residues {residues}")
ints = [14, 6, 11] 
# find index of each number in ints in residues
for i in ints:
    try :
        print(residues.index(i))
    except:
        print("not found")
        
###################################################

qr = [a for a in range(n) if pow(a,2,n) in ints]
print(f"flag {min(qr)}")