import os
import requests
import subprocess
import hashlib
import jwt  # PyJWT, used for JWT encoding/decoding

# Hardcoded secret (detectable via secrets rule)
API_KEY = "1234567890abcdef"

# Insecure HTTP request (instead of HTTPS)
def fetch_data():
    url = "http://example.com/api/data"
    response = requests.get(url)
    return response.json()

# Dangerous use of subprocess without shell=False
def run_command(cmd):
    subprocess.call(cmd, shell=True)

# Unused variable
def calculate():
    x = 42  # this variable is never used
    return 10 + 5

# Weak hash function (MD5)
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

# Insecure JWT decode without verification
def decode_token(token):
    return jwt.decode(token, options={"verify_signature": False})
