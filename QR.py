import qrcode
qr=qrcode.QRcode(
    version=15,
    box_size=10,
    border=5
)
data="https://luxabord.com/"
qr.add_data(data)
qr.make(fit=true)
img=qr.make_image(fill="black",black_color="white")
img.save('text.png')