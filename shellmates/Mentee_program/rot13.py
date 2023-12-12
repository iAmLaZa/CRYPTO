import string

enc = "pnrfne vf fnzr nf ebg13, jryy urer vf lbhe synt furyyzngrf{v_ubcr_lbh_xabj_ubj_pnrfne_jbexf_abj}"
alphabet = string.ascii_lowercase
n = 26

# rot13 function
def rot13(enc):
    dec = ""
    for i in enc:
        if i.isalpha():
            dec += alphabet[(alphabet.index(i) + 13) % n]
        else:
            dec += i
    return dec
print(rot13(enc))