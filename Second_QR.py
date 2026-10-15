!pip install qrcode
!pip install pillow

import qrcode
url = input("Enter URL to Make QR: ")
if url.startswith("http://") or url.startswith("https://"):
    qr = qrcode.make(url)
    qr.save("SecondQR.png")
    print("QR code created successfully!")
else:
    print("invalid url...!!! must start with http or https")
