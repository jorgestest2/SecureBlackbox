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
        "  hashfunction -- SecureBlackbox HashFunction Demo Application\n\n"
        "SYNOPSIS\n"
        "  hashfunction [-input input_file] [-pass password] [-encoding encoding_type]\n\n"
        "DESCRIPTION\n"
        "  HashFunction demonstrates the usage of HashFunction from SecureBlackbox.\n"
        "  Used to create an hash from file.\n\n"
        "  The options are as follows:\n\n"
        "  -input        An input file to hash (Required).\n\n"
        "  -pass         The password for derive key.\n\n"
        "  -encoding     The encoding of hash. Valid values:\n\n"
        "                  0 - DEFAULT\n"
        "                  1 - BINARY\n"
        "                  2 - BASE_64\n"
        "                  3 - COMPACT\n"
        "                  4 - JSON\n\n"
        "EXAMPLES\n"
        "  hashfunction -input C:\\hash\\helloworld.txt \n\n"
        "  hashfunction -input C:\\hash\\helloworld.txt -encoding 2 -pass mypassword \n\n"
    )
    
if (len(sys.argv) < 3):
    displayHelp()
    sys.exit(1)
else:
    hashF = HashFunction()
    cm = CryptoKeyManager()
    
    inputF = ""
    password = ""

    for x in range(len(sys.argv)):
        if (sys.argv[x].startswith("-")):
            if (sys.argv[x].lower() == "-input"):
                inputF = sys.argv[x+1]
            if (sys.argv[x].lower() == "-pass"):
                password = sys.argv[x+1]
            if (sys.argv[x].lower() == "-encoding"):
                hashF.set_output_encoding(int(sys.argv[x+1]))
    
    if (inputF == ""):
        print("-input is required.\n")
        displayHelp()
        sys.exit(1)
    
    try:
        if (password != ""):
            cm.derive_key(128, password, "")
            hashF.set_key_handle(cm.get_key_handle())

        output = hashF.hash_file(inputF)
        print("Calculated hash: " + output.decode('utf-8', errors='backslashreplace'))
    except Exception as e: 
        print(e)



