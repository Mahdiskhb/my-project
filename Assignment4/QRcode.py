
import qrcode
name = input("please enter your name : ")
number = input ("please enter your number : ")
qr= qrcode.make(name+"💛🐋"+number)
qr.save("name_number_QR.png")