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
        "  officedecryptor -- SecureBlackbox OfficeDecryptor Demo Application\n\n"
        "SYNOPSIS\n"
        "  officedecryptor [-input input_file] [-output output_file] [-pass decryption_password] \n\n"
        "DESCRIPTION\n"
        "  OfficeDecryptor demonstrates the usage of OfficeDecryptor from SecureBlackbox.\n"
        "  Used to decrypt office documents. \n\n"
        "  The options are as follows:\n\n"
        "  -input        An input file to decrypt (Required).\n\n"
        "  -output       Where the decrypted file will be saved (Required).\n\n"
        "  -pass         Password for file encryption (Required).\n\n"
    )
    
if (len(sys.argv) < 7):
    displayHelp()
    sys.exit(1)
else:
    decryptor = OfficeDecryptor()
    
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
        decryptor.set_input_file(inputF)
        decryptor.set_output_file(outputF)
    
        decryptor.set_password(password)

        decryptor.decrypt()
    
        print("Office document successfully decrypted.")
    except Exception as e: 
        print(e)



