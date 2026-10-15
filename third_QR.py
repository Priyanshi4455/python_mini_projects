!pip install qrcode
!pip install pillow

import qrcode
url=input("Enter URL to Make QR: ")
if url.startswith("http://") or url.startswith("https://"):
    qr=qrcode.QRCode(version=1,
    error_correction=qrcode.constants. ERROR_CORRECT_H,
    box_size=10,# 10×10
    border=4
    )
    qr.add_data(url)
    qr.make()
    
    image=qr.make_image(fill_color="blue", back_color="red")
    
    image.save("ThirdQR.png")
    print("QR code created successfully!")
else:
    print("Invalid Url .. !!! Must start with http or https")
