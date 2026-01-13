import qrcode

def generate_qr():
    # ask user what to encode
    data = input("Enter text/URL to encode in QR: ").strip()
    if not data:
        print("Nothing entered! Try again.")
        return

    # create the qr object
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    # choose a filename
    filename = input("Enter filename to save (example: my_qr.png): ").strip()
    if not filename:
        filename = "qr_code.png"

    if not filename.lower().endswith(".png"):
        filename += ".png"

    # save file
    img.save(filename)
    print(f"QR Code saved as {filename}")

if __name__ == "__main__":
    print("Simple QR Code Generator")
    generate_qr()
