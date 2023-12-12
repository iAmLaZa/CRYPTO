# ----------------------------------------- RSA third part read subdomaine from PEM file  -------------------------
#read sub domaine from pem file
from cryptography import x509
from cryptography.hazmat.backends import default_backend


# Specify the path to your PEM certificate file
pem_file_path = "transparency.pem"

# Read the PEM certificate file
with open(pem_file_path, "rb") as pem_file:
    pem_data = pem_file.read()
    
# Parse the PEM data and create an X.509 certificate object
cert = x509.load_pem_x509_certificate(pem_data, default_backend())
print(cert.subject)

# Parse the PEM data and create an X.509 certificate object
cert = x509.load_pem_x509_certificate(pem_data, default_backend())

# Check if the certificate has a Subject Alternative Name (SAN) extension
if cert.extensions:
    for extension in cert.extensions:
        if isinstance(extension.value, x509.SubjectAlternativeName):
            san = extension.value
            for name in san:
                if isinstance(name, x509.DNSName):
                    subdomain = name.value
                    print(f"Subdomain: {subdomain}")
else:
    print("No Subject Alternative Name (SAN) extension found in the certificate.")

# If the certificate doesn't have SAN extensions, you may need to look in the Subject field for the commonName (CN).
if not cert.extensions:
    for attribute in cert.subject:
        if attribute.oid == x509.NameOID.COMMON_NAME:
            common_name = attribute.value
            print(f"Common Name (CN): {common_name}")