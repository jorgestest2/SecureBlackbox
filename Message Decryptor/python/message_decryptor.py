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
        "  messagedecryptor -- SecureBlackbox MessageDecryptor Demo Application\n\n"
        "SYNOPSIS\n"
        "  messagedecryptor [-input input_file] [-output output_file] [-cert certificate_file] [-certpass certificate_password]\n\n"
        "DESCRIPTION\n"
        "  MessageDecryptor demonstrates the usage of MessageDecryptor from SecureBlackbox.\n"
        "  Used to decryption of encrypted ('enveloped') PKCS#7 messages. \n\n"
        "  The options are as follows:\n\n"
        "  -input        An input file to decrypt (Required).\n\n"
        "  -output       Where the decrypted file will be saved (Required).\n\n"
        "  -cert         The certificate used to decrypt file (Required).\n\n"
        "  -certpass     The password for the decryption certificate (Required).\n\n"
        "EXAMPLES\n"
        "  messagedecryptor -input C:\\pkcs7\\enc.pkcs7 -output C:\\pkcs7\\helloworld.txt -cert C:\\certs\\mycert.pfx -certpass mypassword \n\n"
    )
    
if (len(sys.argv) < 9):
    displayHelp()
    sys.exit(1)
else:
    decryptor = MessageDecryptor()
    cm = CertificateManager()
    
    inputF = ""
    outputF = ""
    certF = ""
    certpass = ""

    for x in range(len(sys.argv)):
        if (sys.argv[x].startswith("-")):
            if (sys.argv[x].lower() == "-input"):
                inputF = sys.argv[x+1]
            if (sys.argv[x].lower() == "-output"):
                outputF = sys.argv[x+1]
            if (sys.argv[x].lower() == "-cert"):
                certF = sys.argv[x+1]
            if (sys.argv[x].lower() == "-certpass"):
                certpass = sys.argv[x+1]
    
    if (inputF == ""):
        print("-input is required.\n")
        displayHelp()
        sys.exit(1)
    
    if (outputF == ""):
        print("-output is required.\n")
        displayHelp()
        sys.exit(1)
    
    if (certF == ""):
        print("-cert is required.\n")
        displayHelp()
        sys.exit(1)
    
    if (certpass == ""):
        print("-certpass is required.\n")
        displayHelp()
        sys.exit(1)

    try:
        decryptor.set_input_file(inputF)
        decryptor.set_output_file(outputF)
    
        cm.import_from_file(certF, certpass)
        decryptor.set_cert_count(1);
        decryptor.set_cert_handle(0, cm.get_cert_handle())

        decryptor.decrypt()
    
        print("The file successfully decrypted.")
    except Exception as e: 
        print(e)



