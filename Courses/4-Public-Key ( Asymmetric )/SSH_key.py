# ----------------------------------------- RSA fourth part read key pub file ssh -------------------------
# read pub ssh key
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

file = open("bruce_rsa.pub", "rb")
public_key = serialization.load_ssh_public_key(
    file.read(),
    backend=default_backend()
)
print(public_key.public_numbers().n)