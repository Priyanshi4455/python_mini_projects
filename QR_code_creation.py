!pip install qrcode
!pip install pillow

import qrcode
data = input("Enter URL to Make QR: ")
qr = qrcode.make(data)
qr.save("firstQR.png")
print("QR code created successfully!")
