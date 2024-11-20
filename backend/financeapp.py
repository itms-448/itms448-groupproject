
from dotenv import load_dotenv
import os

# Load variables from the .env file
load_dotenv()

# Access API keys securely
OPEN_EXCHANGE_RATE_KEY = os.getenv("OPEN_EXCHANGE_RATE_KEY")
ALPACA_KEY = os.getenv("ALPACA_KEY")
ALPACA_SECRET = os.getenv("ALPACA_SECRET")
PLAID_CLIENT_ID = os.getenv("PLAID_CLIENT_ID")
PLAID_SECRET = os.getenv("PLAID_SECRET")

import requests

# Alpaca API endpoint
url = "https://paper-api.alpaca.markets/v2/account"

# Secure headers using environment variables
headers = {
    "APCA-API-KEY-ID": ALPACA_KEY,
    "APCA-API-SECRET-KEY": ALPACA_SECRET
}

# Make the API request
response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("Alpaca Account Data:", response.json())
else:
    print(f"Error: {response.status_code}", response.json())

    import bcrypt

# Hash a user password
def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# Verify a password
def verify_password(password, hashed):
    return bcrypt.checkpw(password.encode('utf-8'), hashed)

# Example Usage
plain_password = "mypassword123"
hashed_password = hash_password(plain_password)
print("Hashed Password:", hashed_password)

if verify_password("mypassword123", hashed_password):
    print("Password is valid!")
else:
    print("Invalid password!")