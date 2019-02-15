#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Made by Ano Mobb
# MultiFunction Bitcoin Cracker/ mfbc
# 

try:
    import hashlib, random, os, base64, binascii, ecdsa, base58, secrets, time
except ImportError:
    import subprocess
    subprocess.check_call(["python", '-m', 'pip', 'install', 'base58==1.0.0'])
    subprocess.check_call(["python", '-m', 'pip', 'install', 'ecdsa==0.13'])






def print_menu():
    print ("""
    
    
               ____________________________________________________
               |                                                  |
               |   ___________________________________________    |
               |   |                                         |    |
               |   |  C:\>_MultiFunction Bitcoin Cracker     |    |
               |   |  C:\>_                                  |    |
               |   |                                         |    |
               |   |                                         |    |
               |   |  C:\>_                                  |    |
               |   |                                         |    |
               |   |                                         |    |
               |   |                                         |    |
               |   |                                         |    |
               |   |                                         |    |
               |   |                                         |    |
               |   |   C:\>_Author: Ano.Mobb                 |    |
               |   |_________________________________________|    |
               |                                                  |
                \_________________________________________________/
                      \___________________________________/
                    ___________________________________________
                 _-'    .-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.  --- `-_
              _-'.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.--.  .-.-.`-_
           _-'.-.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-`__`. .-.-.-.`-_
        _-'.-.-.-.-. .-----.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-----. .-.-.-.-.`-_
     _-'.-.-.-.-.-. .---.-. .-------------------------. .-.---. .---.-.-.-.`-_
    :-------------------------------------------------------------------------:
    `---._.-------------------------------------------------------------._.---'
                                  -Ano.Mobb-
                 Donate: 1GmQaG9R5NPs3ZzR6XPMD9jZk17F9MuoWn
    """)
    print ("1) os.urandom gen.  no base64         " + "\n" +
           "2) os.urandom gen. with base64        " + "\n" +
           "3) secrets.token_bytes gen.  no base64       " + "\n" +
           "4) secrets.token_bytes gen. with base64      " + "\n" +
           "5) dict. attack random word gen.  no base64  (no space)  " + "\n" +
           "6) dict. attack random word gen. with base64 (no space)  " + "\n" +
           "7) dict. attack random word gen.  no base64  (with space) " + "\n" +
           "8) dict. attack random word gen. with base64 (with space) " + "\n" +
           "0) Exit " + "\n")



loop = True

while loop:
    print_menu()
    menu = int(input("Choose your number: "))
    if menu == 1:
        print ("Menu 1 has been selected")
        print ("0) Exit")
        select_byts = int(input("Enter your number of bytes: "))
        if select_byts == 0:
            break
        while True:
            secret_exponent = os.urandom(select_byts)
            pvt = hashlib.sha256(secret_exponent).hexdigest()
            privatekey = binascii.unhexlify(pvt)
            s = ecdsa.SigningKey.from_string(privatekey, curve = ecdsa.SECP256k1)
            publickey = '04' + binascii.hexlify(s.verifying_key.to_string()).decode('utf-8')
            extended_key = "80"+pvt
            first_sha256 = hashlib.sha256(binascii.unhexlify(extended_key)).hexdigest()
            second_sha256 = hashlib.sha256(binascii.unhexlify(first_sha256)).hexdigest()
            final_key = extended_key+second_sha256[:8]
            WIF = base58.b58encode(binascii.unhexlify(final_key))
            alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
            c = '0'; byte = '00'; zero = 0
            var = hashlib.new('ripemd160')
            var.update(hashlib.sha256(binascii.unhexlify(publickey.encode())).digest())
            a = (byte + var.hexdigest())
            doublehash = hashlib.sha256(hashlib.sha256(binascii.unhexlify(a.encode())).digest()).hexdigest()
            address = a + doublehash[0:8]
            for char in address:
                if (char != c):
                    break
                zero += 1
            zero = zero // 2
            n = int(address, 16)
            output = []
            while (n > 0):
                n, remainder = divmod (n, 58)
                output.append(alphabet[remainder])
            count = 0
            while (count < zero):
                output.append(alphabet[0])
                count += 1
            addr = ''.join(output[::-1])
            print("Privatekey: " + " " + str(pvt) + "\n" + "Address:    " + " " + str(addr) +"\n" + "WIF:        " + " " + str(WIF)+"\n")
            with open("addr-data.txt", "r") as m:
                add = m.read().split()
                for ad in add:
                    continue
                if addr in add:
                    data = open("Win.txt","a")
                    data.write("found " + str(secret_exponent) + "\n" + str(pvt)+"\n" +str(addr)+"\n"+str(WIF)+"\n"+"\n")
                    data.close()
                elif addr not in add:
                    print("No luck!!!"+"\n")


    if menu == 2:
        print ("Menu 2 has been selected")
        print ("0) Exit")
        select_byts = int(input("Enter your number of bytes: "))
        if select_byts == 0:
            break
        while True:
            secret_exponent = os.urandom(select_byts)
            b64 = base64.b64encode(secret_exponent)
            pvt = hashlib.sha256(b64).hexdigest()
            privatekey = binascii.unhexlify(pvt)
            s = ecdsa.SigningKey.from_string(privatekey, curve = ecdsa.SECP256k1)
            publickey = '04' + binascii.hexlify(s.verifying_key.to_string()).decode('utf-8')
            extended_key = "80"+pvt
            first_sha256 = hashlib.sha256(binascii.unhexlify(extended_key)).hexdigest()
            second_sha256 = hashlib.sha256(binascii.unhexlify(first_sha256)).hexdigest()
            final_key = extended_key+second_sha256[:8]
            WIF = base58.b58encode(binascii.unhexlify(final_key))
            alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
            c = '0'; byte = '00'; zero = 0
            var = hashlib.new('ripemd160')
            var.update(hashlib.sha256(binascii.unhexlify(publickey.encode())).digest())
            a = (byte + var.hexdigest())
            doublehash = hashlib.sha256(hashlib.sha256(binascii.unhexlify(a.encode())).digest()).hexdigest()
            address = a + doublehash[0:8]
            for char in address:
                if (char != c):
                    break
                zero += 1
            zero = zero // 2
            n = int(address, 16)
            output = []
            while (n > 0):
                n, remainder = divmod (n, 58)
                output.append(alphabet[remainder])
            count = 0
            while (count < zero):
                output.append(alphabet[0])
                count += 1
            addr = ''.join(output[::-1])
            print("base64:    " + "  " + str(b64) + "\n" + "Privatekey: " + " " + str(pvt) + "\n" + "Address   : " + " " + str(addr) +"\n" + "WIF:        " + " " + str(WIF)+"\n")
            with open("addr-data.txt", "r") as m:
                add = m.read().split()
                for ad in add:
                    continue
                if addr in add:
                    data = open("Win.txt","a")
                    data.write("found " + str(secret_exponent) + "\n" + str(b64) + "\n" + str(pvt)+"\n" +str(addr)+"\n"+str(WIF)+"\n"+"\n")
                    data.close()
                elif addr not in add:
                    print("No luck!!!"+"\n")





    elif menu == 3:
        print ("Menu 3 has been selected")
        print ("0) Exit")
        select_byts = int(input("Enter your number of bytes: "))
        if select_byts == 0:
            break
        while True:
            secret_exponent = secrets.token_bytes(select_byts)
            pvt = hashlib.sha256(secret_exponent).hexdigest()
            privatekey = binascii.unhexlify(pvt)
            s = ecdsa.SigningKey.from_string(privatekey, curve = ecdsa.SECP256k1)
            publickey = '04' + binascii.hexlify(s.verifying_key.to_string()).decode('utf-8')
            extended_key = "80"+pvt
            first_sha256 = hashlib.sha256(binascii.unhexlify(extended_key)).hexdigest()
            second_sha256 = hashlib.sha256(binascii.unhexlify(first_sha256)).hexdigest()
            final_key = extended_key+second_sha256[:8]
            WIF = base58.b58encode(binascii.unhexlify(final_key))
            alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
            c = '0'; byte = '00'; zero = 0
            var = hashlib.new('ripemd160')
            var.update(hashlib.sha256(binascii.unhexlify(publickey.encode())).digest())
            a = (byte + var.hexdigest())
            doublehash = hashlib.sha256(hashlib.sha256(binascii.unhexlify(a.encode())).digest()).hexdigest()
            address = a + doublehash[0:8]
            for char in address:
                if (char != c):
                    break
                zero += 1
            zero = zero // 2
            n = int(address, 16)
            output = []
            while (n > 0):
                n, remainder = divmod (n, 58)
                output.append(alphabet[remainder])
            count = 0
            while (count < zero):
                output.append(alphabet[0])
                count += 1
            addr = ''.join(output[::-1])
            print("Token_bytes: " + str(secret_exponent) + "\n" + "Private key: " + str(pvt) + "\n" + "Address:    " + str(addr) + "\n" + "WIF:        " + str(WIF) + "\n")
            with open("addr-data.txt", "r") as m:
                add = m.read().split()
                for ad in add:
                    continue
                if addr in add:
                    data = open("Win.txt","a")
                    data.write("found " + str(secret_exponent) + "\n" + str(pvt)+"\n" +str(addr)+"\n"+str(WIF)+"\n"+"\n")
                    data.close()
                elif addr not in add:
                    print("No luck!!!"+"\n")


    elif menu == 4:
        print ("Menu 4 has been selected")
        print ("0) Exit")
        select_byts = int(input("Enter your number of bytes: "))
        if select_byts == 0:
            break
        while True:
            secret_exponent = secrets.token_bytes(select_byts)
            b64 = base64.b64encode(secret_exponent)
            pvt = hashlib.sha256(b64).hexdigest()
            privatekey = binascii.unhexlify(pvt)
            s = ecdsa.SigningKey.from_string(privatekey, curve = ecdsa.SECP256k1)
            publickey = '04' + binascii.hexlify(s.verifying_key.to_string()).decode('utf-8')
            extended_key = "80"+pvt
            first_sha256 = hashlib.sha256(binascii.unhexlify(extended_key)).hexdigest()
            second_sha256 = hashlib.sha256(binascii.unhexlify(first_sha256)).hexdigest()
            final_key = extended_key+second_sha256[:8]
            WIF = base58.b58encode(binascii.unhexlify(final_key))
            alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
            c = '0'; byte = '00'; zero = 0
            var = hashlib.new('ripemd160')
            var.update(hashlib.sha256(binascii.unhexlify(publickey.encode())).digest())
            a = (byte + var.hexdigest())
            doublehash = hashlib.sha256(hashlib.sha256(binascii.unhexlify(a.encode())).digest()).hexdigest()
            address = a + doublehash[0:8]
            for char in address:
                if (char != c):
                    break
                zero += 1
            zero = zero // 2
            n = int(address, 16)
            output = []
            while (n > 0):
                n, remainder = divmod (n, 58)
                output.append(alphabet[remainder])
            count = 0
            while (count < zero):
                output.append(alphabet[0])
                count += 1
            addr = ''.join(output[::-1])
            print("Token_bytes: " + str(secret_exponent) + "\n" + "Base64:      " + str(b64) + "\n" + "Privatekey:  " + str(pvt)+ "\n" + "Address:     " + str(addr) + "\n" + "WIF:         " + str(WIF) + "\n")
            with open("addr-data.txt", "r") as m:
                add = m.read().split()
                for ad in add:
                    continue
                if addr in add:
                    data = open("Win.txt","a")
                    data.write("found " + str(secret_exponent) + "\n" + str(b64) + "\n" + str(pvt)+"\n" +str(addr)+"\n"+str(WIF)+"\n")
                    data.close()
                elif addr not in add:
                    print("No luck!!!"+"\n")
        
    elif menu == 5:
        while True:
            print ("Menu 5 has been selected"+ "\n")
            fobj = input("Enter name or path of txt file: ")
            sa = input("Enter number of passphrases: ")
            file = open(fobj, "r")
            dict = {}
            with file as f:
                words = f.read().split()
                for word in words:
                    sent = [random.choice(words)
                            for word in range(int(sa))]
                    sect = ''.join(sent)
                    secret_exponent1 = bytes(str(sect).encode("utf-8"))
                    pvt1 = hashlib.sha256(secret_exponent1).hexdigest()
                    privatekey1 = binascii.unhexlify(pvt1)
                    s = ecdsa.SigningKey.from_string(privatekey1, curve = ecdsa.SECP256k1)
                    publickey1 = '04' + binascii.hexlify(s.verifying_key.to_string()).decode('utf-8')
                    extended_key1 = "80"+pvt1
                    first_sha2561 = hashlib.sha256(binascii.unhexlify(extended_key1)).hexdigest()
                    second_sha2561 = hashlib.sha256(binascii.unhexlify(first_sha2561)).hexdigest()
                    final_key1 = extended_key1+second_sha2561[:8]
                    WIF1 = base58.b58encode(binascii.unhexlify(final_key1))
                    alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
                    c = '0'; byte = '00'; zero = 0
                    var = hashlib.new('ripemd160')
                    var.update(hashlib.sha256(binascii.unhexlify(publickey1.encode())).digest())
                    a = (byte + var.hexdigest())
                    doublehash = hashlib.sha256(hashlib.sha256(binascii.unhexlify(a.encode())).digest()).hexdigest()
                    address = a + doublehash[0:8]
                    for char in address:
                        if (char != c):
                            break
                        zero += 1
                    zero = zero // 2
                    n = int(address, 16)
                    output = []
                    while (n > 0):
                        n, remainder = divmod (n, 58)
                        output.append(alphabet[remainder])
                    count = 0
                    while (count < zero):
                        output.append(alphabet[0])
                        count += 1
                    addr1 = ''.join(output[::-1])
                    print("Passphrase: " + str(secret_exponent1) + "\n" + "Privatekey: " + str(pvt1)+"\n" + "Address:    " + str(addr1)+"\n"+ "WIF:        " +str(WIF1)+"\n")
                    with open("addr-data.txt", "r") as m:
                        add = m.read().split()
                        for ad in add:
                            continue
                        if addr1 in add:
                            data = open("Win.txt","a")
                            data.write("found " + str(secret_exponent1) + "\n" + "\n" + str(pvt1)+"\n" +str(addr1)+"\n"+str(WIF1)+"\n")
                            data.close()
                        elif addr1 not in add:
                            print("No luck!!!"+"\n")       
     
    elif menu == 6:
        while True:
            print ("Menu 6 has been selected"+ "\n")
            fobj = input("Enter name or path of txt file: ")
            sa = input("Enter number of passphrases: ")
            file = open(fobj, "r")
            dict = {}
            with file as f:
                words = f.read().split()
                for word in words:
                    sent = [random.choice(words)
                            for word in range(int(sa))]
                    sect = ''.join(sent)
                    secret_exponent1 = bytes(str(sect).encode("utf-8"))
                    b6 = base64.b64encode(secret_exponent1)
                    pvt1 = hashlib.sha256(b6).hexdigest()
                    privatekey1 = binascii.unhexlify(pvt1)
                    s = ecdsa.SigningKey.from_string(privatekey1, curve = ecdsa.SECP256k1)
                    publickey1 = '04' + binascii.hexlify(s.verifying_key.to_string()).decode('utf-8')
                    extended_key1 = "80"+pvt1
                    first_sha2561 = hashlib.sha256(binascii.unhexlify(extended_key1)).hexdigest()
                    second_sha2561 = hashlib.sha256(binascii.unhexlify(first_sha2561)).hexdigest()
                    final_key1 = extended_key1+second_sha2561[:8]
                    WIF1 = base58.b58encode(binascii.unhexlify(final_key1))
                    alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
                    c = '0'; byte = '00'; zero = 0
                    var = hashlib.new('ripemd160')
                    var.update(hashlib.sha256(binascii.unhexlify(publickey1.encode())).digest())
                    a = (byte + var.hexdigest())
                    doublehash = hashlib.sha256(hashlib.sha256(binascii.unhexlify(a.encode())).digest()).hexdigest()
                    address = a + doublehash[0:8]
                    for char in address:
                        if (char != c):
                            break
                        zero += 1
                    zero = zero // 2
                    n = int(address, 16)
                    output = []
                    while (n > 0):
                        n, remainder = divmod (n, 58)
                        output.append(alphabet[remainder])
                    count = 0
                    while (count < zero):
                        output.append(alphabet[0])
                        count += 1
                    addr1 = ''.join(output[::-1])
                    print("Passphrase: " + str(secret_exponent1) + "\n" + "Base64:     " + str(b6) + "\n" + "Privatekey: " + str(pvt1)+"\n" + "Address:    " + str(addr1) +" \n" + "WIF:        " + str(WIF1)+"\n")
                    with open("addr-data.txt", "r") as m:
                        add = m.read().split()
                        for ad in add:
                            continue
                        if addr1 in add:
                            data = open("Win.txt","a")
                            data.write("found " + str(secret_exponent1) + "\n" + str(b6) + "\n" + str(pvt1)+"\n" +str(addr1)+"\n"+str(WIF1)+"\n")
                            data.close()
                        elif addr1 not in add:
                            print("No luck!!!"+"\n")




    elif menu == 7:
        while True:
            print ("Menu 7 has been selected"+ "\n")
            fobj = input("Enter name or path of txt file: ")
            sa = input("Enter number of passphrases: ")
            file = open(fobj, "r")
            dict = {}
            with file as f:
                words = f.read().split()
                for word in words:
                    sent = [random.choice(words)
                            for word in range(int(sa))]
                    sect = ' '.join(sent)
                    secret_exponent1 = bytes(str(sect).encode("utf-8"))
                    pvt1 = hashlib.sha256(secret_exponent1).hexdigest()
                    privatekey1 = binascii.unhexlify(pvt1)
                    s = ecdsa.SigningKey.from_string(privatekey1, curve = ecdsa.SECP256k1)
                    publickey1 = '04' + binascii.hexlify(s.verifying_key.to_string()).decode('utf-8')
                    extended_key1 = "80"+pvt1
                    first_sha2561 = hashlib.sha256(binascii.unhexlify(extended_key1)).hexdigest()
                    second_sha2561 = hashlib.sha256(binascii.unhexlify(first_sha2561)).hexdigest()
                    final_key1 = extended_key1+second_sha2561[:8]
                    WIF1 = base58.b58encode(binascii.unhexlify(final_key1))
                    alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
                    c = '0'; byte = '00'; zero = 0
                    var = hashlib.new('ripemd160')
                    var.update(hashlib.sha256(binascii.unhexlify(publickey1.encode())).digest())
                    a = (byte + var.hexdigest())
                    doublehash = hashlib.sha256(hashlib.sha256(binascii.unhexlify(a.encode())).digest()).hexdigest()
                    address = a + doublehash[0:8]
                    for char in address:
                        if (char != c):
                            break
                        zero += 1
                    zero = zero // 2
                    n = int(address, 16)
                    output = []
                    while (n > 0):
                        n, remainder = divmod (n, 58)
                        output.append(alphabet[remainder])
                    count = 0
                    while (count < zero):
                        output.append(alphabet[0])
                        count += 1
                    addr1 = ''.join(output[::-1])
                    print("Passphrase: " + str(secret_exponent1) + "\n" + "Privatekey: " + str(pvt1) + "\n" + "Address:    " + str(addr1) + "\n" + "WIF:        " + str(WIF1)+"\n")
                    with open("addr-data.txt", "r") as m:
                        add = m.read().split()
                        for ad in add:
                            continue
                        if addr1 in add:
                            print("Found: " + " " +addr1)
                            data = open("Win.txt","a")
                            data.write("found " + str(secret_exponent1) + "\n" + str(b6) + "\n" + str(pvt1)+"\n" +str(addr1)+"\n"+str(WIF1)+"\n")
                            data.close()
                        elif addr1 not in add:
                            print("No luck!!!"+"\n")


    elif menu == 8:
        while True:
            print ("Menu 8 has been selected"+ "\n")
            fobj = input("Enter name or path of txt file: ")
            sa = input("Enter number of passphrases: ")
            file = open(fobj, "r")
            dict = {}
            with file as f:
                words = f.read().split()
                for word in words:
                    sent = [random.choice(words)
                            for word in range(int(sa))]
                    sect = ' '.join(sent)
                    secret_exponent1 = bytes(str(sect).encode("utf-8"))
                    b6 = base64.b64encode(secret_exponent1)
                    pvt1 = hashlib.sha256(b6).hexdigest()
                    privatekey1 = binascii.unhexlify(pvt1)
                    s = ecdsa.SigningKey.from_string(privatekey1, curve = ecdsa.SECP256k1)
                    publickey1 = '04' + binascii.hexlify(s.verifying_key.to_string()).decode('utf-8')
                    extended_key1 = "80"+pvt1
                    first_sha2561 = hashlib.sha256(binascii.unhexlify(extended_key1)).hexdigest()
                    second_sha2561 = hashlib.sha256(binascii.unhexlify(first_sha2561)).hexdigest()
                    final_key1 = extended_key1+second_sha2561[:8]
                    WIF1 = base58.b58encode(binascii.unhexlify(final_key1))
                    alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
                    c = '0'; byte = '00'; zero = 0
                    var = hashlib.new('ripemd160')
                    var.update(hashlib.sha256(binascii.unhexlify(publickey1.encode())).digest())
                    a = (byte + var.hexdigest())
                    doublehash = hashlib.sha256(hashlib.sha256(binascii.unhexlify(a.encode())).digest()).hexdigest()
                    address = a + doublehash[0:8]
                    for char in address:
                        if (char != c):
                            break
                        zero += 1
                    zero = zero // 2
                    n = int(address, 16)
                    output = []
                    while (n > 0):
                        n, remainder = divmod (n, 58)
                        output.append(alphabet[remainder])
                    count = 0
                    while (count < zero):
                        output.append(alphabet[0])
                        count += 1
                    addr1 = ''.join(output[::-1])
                    print("Passphrase: " + str(secret_exponent1) + "\n" + "Base64:     " + str(b6) + "\n" + "Privatekey: " + str(pvt1) + "\n" + "Address:    " + str(addr1) + "\n" + "WIF:        " + str(WIF1)+"\n")
                    with open("addr-data.txt", "r") as m:
                        add = m.read().split()
                        for ad in add:
                            continue
                        if addr1 in add:
                            print("Found: " + " " +addr1)
                            data = open("Win.txt","a")
                            data.write("found " + str(secret_exponent1) + "\n" + str(b6) + "\n" + str(pvt1)+"\n" +str(addr1)+"\n"+str(WIF1)+"\n")
                            data.close()
                        elif addr1 not in add:
                            print("No luck!!!"+"\n")


                    

    elif menu == 0:
        break
        loop=False
    else:
        # Any integer inputs other than values 1-5 we print an error message
        key = input("Wrong option selection. Enter any key to try again..")








