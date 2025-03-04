import qrcode

# Your Django server URL with a source identifier
url = "https://ssri47856.pythonanywhere.com/redirect"

# Generate QR code
qr = qrcode.make(url)

# Save the QR code as an image
qr.save("qr_code.png")

print("QR code saved as qr_code.png")

