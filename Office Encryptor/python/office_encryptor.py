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
        "  officeencryptor -- SecureBlackbox OfficeEncryptor Demo Application\n\n"
        "SYNOPSIS\n"
        "  officeencryptor [-input input_file] [-output output_file] [-pass encryption_password] [-enctype encryption_type] [-encalg encryption_algorithm] \n\n"
        "DESCRIPTION\n"
        "  OfficeEncryptor demonstrates the usage of OfficeEncryptor from SecureBlackbox.\n"
        "  Used to encrypt office documents. \n\n"
        "  The options are as follows:\n\n"
        "  -input        An input file to encrypt (Required).\n\n"
        "  -output       Where the encrypted file will be saved (Required).\n\n"
        "  -pass         Password for file encryption (Required).\n\n"
        "  -enctype      The type of encryption to use. Enter the corresponding number. Valid values:\n\n"
        "                  0 - DEFAULT\n"
        "                  1 - BINARY_RC4\n"
        "                  2 - BINARY_RC4CRYPTO_API\n"
        "                  3 - OPEN_XMLSTANDARD\n"
        "                  4 - OPEN_XMLAGILE\n"
        "                  5 - OPEN_DOCUMENT\n\n"
        "  -encalg       The encryption algorithm to use. Valid values: RC2, RC4, DES, 3DES, AES128, AES192, AES256, Blowfish \n\n"
        "EXAMPLES\n"
        "  officeencryptor -input C:\\office\\helloworld.doc -output C:\\office\\helloworld.enc -pass mypassword \n\n"
        "  officeencryptor -input C:\\office\\helloworld.doc -output C:\\office\\helloworld.enc -pass mypassword -enctype 2 -encalg AES128 \n\n"
    )
    
if (len(sys.argv) < 7):
    displayHelp()
    sys.exit(1)
else:
    encryptor = OfficeEncryptor()
    
    inputF = ""
    outputF = ""
    password = ""

    for x in range(len(sys.argv)):
        if (sys.argv[x].startswith("-")):
            if (sys.argv[x].lower() == "-input"):
                inputF = sys.argv[x+1]
            if (sys.argv[x].lower() == "-output"):
                outputF = sys.argv[x+1]
            if (sys.argv[x].lower() == "-pass"):
                password = sys.argv[x+1]
            if (sys.argv[x].lower() == "-enctype"):
                encryptor.set_encryption_type(int(sys.argv[x+1]))
            if (sys.argv[x].lower() == "-encalg"):
                encryptor.set_encryption_algorithm(sys.argv[x+1])
    
    if (inputF == ""):
        print("-input is required.\n")
        displayHelp()
        sys.exit(1)
    
    if (outputF == ""):
        print("-output is required.\n")
        displayHelp()
        sys.exit(1)
    
    if (password == ""):
        print("-pass is required.\n")
        displayHelp()
        sys.exit(1)

    try:
        encryptor.set_input_file(inputF)
        encryptor.set_output_file(outputF)
    
        encryptor.set_password(password)

        encryptor.encrypt()
    
        print("Office document successfully encrypted.")
    except Exception as e: 
        print(e)



