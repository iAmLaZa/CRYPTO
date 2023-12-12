# flag mod 26

flag = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_jdJBFOXJ}"

# function to decode the flag mod 26
def decode_flag_mod26(flag):
    decoded_flag = ""
    for i in range(len(flag)):
        if flag[i].isalpha():
            decoded_flag += chr((ord(flag[i]) - 97 + 13) % 26 + 97)
        else:
            decoded_flag += flag[i]
    return decoded_flag
print(decode_flag_mod26(flag))
