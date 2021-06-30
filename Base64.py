from termcolor import colored
from pyfiglet import figlet_format

print((colored(figlet_format("BASE64 ENCODE & DECODE", font="future_1"), color="red")))
print((colored("-------------------- Coded by Dzaki Althalsyah -------------------- \n", color="blue")))
print((colored("Github: https://github.com/dzakialthalsyah/   ||   Instagram: https://instagram.com/dzakialthalsyah/ \n\n\n", color="cyan")))

import base64

def base64text():

    option = int(input("""(1)base64encode || (2)base64decode \n\n\npilih salah satu dari angka tersebut: """))

    if option == 1:
        kata1 = input("masukkan kata: ")
        kata_encode_byte = kata1.encode("ascii")
        encode = base64.b64encode(kata_encode_byte)
        print(encode)

    elif option == 2:
        kata2 = input("masukkan kata: ")
        decode = base64.b64decode(kata2)
        print(decode)

    else:
        print("salah")


base64text()