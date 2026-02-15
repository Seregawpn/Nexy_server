import sys

import qrcode  # type: ignore


def generate_qr(data, filename="whatsapp_qr.png"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # type: ignore
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)  # type: ignore
    print(f"QR code saved to {filename}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 generate_qr.py <qr_data_string>")
        sys.exit(1)

    data = sys.argv[1]
    # Save to artifacts directory or current directory
    output_path = "/Users/sergiyzasorin/.gemini/antigravity/brain/2d8b56ac-c774-4e66-9fa4-0db4ba606863/whatsapp_qr.png"
    generate_qr(data, output_path)
