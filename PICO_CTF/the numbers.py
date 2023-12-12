s = '16 9 3 15 3 20 6 { 20 8 5 14 21 13 2 5 18 19 13 1 19 15 14 }'
s = s.split(' ')

# function to convert numbers to letters A=1 and Z=26
def convert_to_letters(s):
    flag = ''
    for i in range(len(s)):
        #if i is number
        if s[i].isdigit():
            flag += chr(int(s[i]) + 64)
        else :
            flag += s[i]
    return flag

print(convert_to_letters(s))