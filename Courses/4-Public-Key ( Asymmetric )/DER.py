# ----------------------------------------- RSA fourth part read key from der file  -------------------------
# read private key from der file rsa certificatat 

from cryptography import x509
from cryptography.hazmat.backends import default_backend

# Specify the path to your PEM certificate file
pem_file_path = "2048b-rsa-example-cert.der"

# Read the PEM certificate file
with open(pem_file_path, "rb") as pem_file:
    pem_data = pem_file.read()

# Parse the PEM data and create an X.509 certificate object
cert = x509.load_der_x509_certificate(pem_data, default_backend())
print(cert.public_key().public_numbers().n)
# Display certificate information
print(f"Subject: {cert.subject}")
print(f"Issuer: {cert.issuer}")
print(f"Serial Number: {cert.serial_number}")
print(f"Version: {cert.version}")
print(f"Validity Not Before: {cert.not_valid_before}")
print(f"Validity Not After: {cert.not_valid_after}")
