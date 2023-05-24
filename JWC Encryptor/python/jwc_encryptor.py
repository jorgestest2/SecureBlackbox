#
# SecureBlackbox 2022 Python Edition - Demo Application
#
# Copyright (c) 2023 /n software inc. - All rights reserved. - www.nsoftware.com
#

import sys
import string
from secureblackbox import *

input = sys.hexversion<0x03000000 and raw_input or input

def displayHelp():
    print(
        "NAME\n"
        "  jwencryption -- SecureBlackbox SymmetricCrypto Demo Application\n\n"
        "SYNOPSIS\n"
        "  jwencryption -e/-d [-input input_data] [-pass encryption_password] [-compact] [-encalg encryption_algorithm]\n\n"
        "DESCRIPTION\n"
        "  This sample illustrates how to encrypt text to a JW token with a password.\n"
        "  Used to encrypt and decrypt data.\n\n"
        "  The options are as follows:\n\n"
        "  -e            Whether to encrypt input data. \n\n"
        "  -d            Whether to decrypt input data. \n\n"
        "  -input        An input data to encrypt/decrypt (Required). \n\n"
        "  -pass         Password for encryption (Required). \n\n"
        "  -compact      Whether to use compact format \n\n"
        "  -encalg       The encryption algorithm to use. Valid values: RC2, RC4, DES, 3DES, AES128, AES192, AES256, Blowfish \n\n"
        "EXAMPLES\n"
        "	jwencryption -e -input \"And now that you don’t have to be perfect, you can be good.\" -pass mypassword -encalg AES256 \n\n"
        "	jwencryption -d -input eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2Q0JDLUhTNTEyIn0..kuN2U -pass mypassword -compact \n\n"
    )

if (len(sys.argv) < 6):
    displayHelp()
    sys.exit(1)
else:
    crypto = SymmetricCrypto()
    ckm = CryptoKeyManager()
    
    encrypt = False
    decrypt = False
    inputD = ""
    password = ""
    compact = False
    
    for x in range(len(sys.argv)):
        if (sys.argv[x].startswith("-")):
            if (sys.argv[x].lower() == "-e"):
                encrypt = True
            if (sys.argv[x].lower() == "-d"):
                decrypt = True
            if (sys.argv[x].lower() == "-input"):
                inputD = sys.argv[x+1]
            if (sys.argv[x].lower() == "-pass"):
                password = sys.argv[x+1]
            if (sys.argv[x].lower() == "-encalg"):
                crypto.set_encryption_algorithm(sys.argv[x+1])
            if (sys.argv[x].lower() == "-compact"):
                compact = True

    if (not (encrypt or decrypt)):
        print("-e or -d is required.\n")
        displayHelp()
        sys.exit(1)

    if (encrypt and decrypt):
        print("-Use only one -e or -d parameter.\n")
        displayHelp()
        sys.exit(1)

    if (inputD == ""):
        print("-input is required.\n")
        displayHelp()
        sys.exit(1)
            
    if (password == ""):
        print("-pass is required.\n")
        displayHelp()
        sys.exit(1)
        
    try:     
        # PasswordToKey
        ckm.derive_key(256, password, "")
        
        iv = bytearray(16)
        ckm.set_key_iv(iv)
        
        crypto.set_key_handle(ckm.get_key_handle())

        inputB = inputD.encode('utf-8')
        
        if encrypt:
            if compact:
                crypto.set_output_encoding(3); # cetCompact
            else:
                crypto.set_output_encoding(4); # cetJSON

            outputB = crypto.encrypt(inputB)
            print("Encrypted token: " + outputB.decode('utf-8', errors='backslashreplace'))
        else:
            if compact:
                crypto.set_input_encoding(3); # cetCompact
            else:
                crypto.set_input_encoding(4); # cetJSON
                
            outputB = crypto.decrypt(inputB)
            print("Decrypted string: " + outputB.decode('utf-8', errors='backslashreplace')) 
    except Exception as e: 
        print(e)


