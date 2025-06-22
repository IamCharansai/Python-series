import qrcode

def generate_qr(data, filename="my_qr.png"):
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f" QR Code saved as {filename}")

# Run
print(" QR Code Generator")
text = input("Enter text or URL to encode: ")
generate_qr(text)
