import qrcode
generate = qrcode.make("https://www.apple.com/in/")
generate.save("Apple_Website_QRCode.png")