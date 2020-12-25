import pyqrcode
import png
import time

from pyqrcode import *


print("Hello From The Developer of this Application!\n")
time.sleep(2)

try:
    QR = input("Paste URL/Link here: \n")
    time.sleep(2)
    
    url = pyqrcode.create(QR)

    url.svg("YourQRCode.svg", scale = 8)

    url.png("YourQRCode.png", scale = 8)

    time.sleep(2)
    print("Successfully Created!\n")
    time.sleep(2)
    print("Check on your device by searching 'YourQRCode'. You can later change name and location. Thanks!\n")
    time.sleep(2)
    x = input("\nPress any key to exit ")
except:
    print("Umm, Unexpected Error Occured. Please Try Again!\n")


