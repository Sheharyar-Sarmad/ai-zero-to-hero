import qrcode
import requests
from urllib.parse import urlparse

data = input("Enter Website URL: ").strip()

# Add https:// if missing
if not data.startswith(("http://", "https://")):
    data = "https://" + data

try:
    parsed = urlparse(data)

    # Check if domain exists
    if not parsed.netloc:
        raise ValueError("Invalid URL!")

    # Check if website is reachable
    response = requests.get(data, timeout=5)

    if response.status_code != 200:
        raise Exception("Website is not reachable!")

    # Generate QR Code 
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    filename = parsed.netloc.replace("www.", "").split(".")[0]

    img.save(f"qr_codes/{filename}.png")

    print(f"QR Code saved as {filename}.png")

except requests.exceptions.RequestException:
    print("Website does not exist or is unreachable.")

except Exception as e:
    print(f"{e}")