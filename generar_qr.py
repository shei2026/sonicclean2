# pip install "qrcode[pil]"
import qrcode
url = input("Pega el enlace de Vercel: ").strip()
qrcode.make(url).save("SonicClean2_QR.png")
print("QR creado: SonicClean2_QR.png")
