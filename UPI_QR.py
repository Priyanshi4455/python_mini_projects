!pip install qrcode
!pip install pillow

import qrcode
#Create QR Code For UPI

upi_id=input("Enter UPI ID: ")
name=input("Enter Name: ")

upi_url= f"upi://pay?pa={upi_id}&pn={name}"

qr=qrcode.make(upi_url)
qr.save("Priyanshi_UPI.png")

print("QR code created successfully!")
