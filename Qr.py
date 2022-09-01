import pyqrcode
import png
link = "https://github.com/Josuedaniiv/Python"
qr_code = pyqrcode.create(link)
qr_code.png("Github.png", scale=5)
