import qrcode
import image
while True:
    qr=qrcode.QRCode(
        version=15,
        box_size=10,
        border=5
    )
    data=input("Enter the url for which you want to generate the QR:")
    qr.add_data(data)
    qr.make(fit=True)
    img=qr.make_image(fill="black",back_color="white")
    img.save("test.png")

