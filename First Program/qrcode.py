import pyotp
import qrcode

# Step 1: Generate a TOTP secret key
secret = pyotp.random_base32()
print(f"Generated TOTP Secret: {secret}")

# Step 2: Create a TOTP instance
totp = pyotp.TOTP(secret)

# Step 3: Generate the QR code data
user = "your-username@example.com"
issuer = "YourAppName"
qr_data = totp.provisioning_uri(name=user, issuer_name=issuer)

# Step 4: Generate and save the QR code
qr_code = qrcode.make(qr_data)
qr_code.save("mfa_qr_code.png")
print("QR code generated and saved as 'mfa_qr_code.png'.")
