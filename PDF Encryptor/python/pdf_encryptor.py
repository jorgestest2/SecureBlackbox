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
        "  pdfencryptor -- SecureBlackbox PDFEncryptor Demo Application\n\n"
        "SYNOPSIS\n"
        "  pdfencryptor [-input input_file] [-output output_file] [-cert certificate_file] [-certpass certificate_password]\n"
        "             [-pass user_password] [-encalg encryption_algorithm] [-nometadata]n\n"
        "DESCRIPTION\n"
        "  PDFEncryptor demonstrates the usage of PDFEncryptor from SecureBlackbox.\n"
        "  Used to encrypt pdf documents.\n\n"
        "  The options are as follows:\n\n"
        "  -input        An input file to encrypt (Required).\n\n"
        "  -output       Where the encrypted file will be saved (Required).\n\n"
        "  -cert         The certificate used to encrypt file.\n\n"
        "  -certpass     The password for the certificate.\n\n"
        "  -pass         The password for encryption.\n\n"
        "  -encalg       The encryption algorithm to use. Valid values: RC2, RC4, DES, 3DES, AES128, AES192, AES256, Blowfish \n\n"
        "  -nometadata   Specifies metadata should not be encrypted.\n\n"
        "EXAMPLES\n"
        "  pdfencryptor -input C:\\pdf\\helloworld.pdf -output C:\\pdf\\mypdf.scs -cert C:\\certs\\mycert.pfx -certpass mypassword \n\n"
        "  pdfencryptor -input C:\\pdf\\helloworld.pdf -output C:\\pdf\\mypdf.scs -pass mypassword -encalg AES128 -nometadata \n\n"
    )
    
if (len(sys.argv) < 5):
    displayHelp()
    sys.exit(1)
else:
    encryptor = PDFEncryptor()
    cm = CertificateManager()
    
    inputF = ""
    outputF = ""
    certF = ""
    certpass = ""
    password = ""

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
            if (sys.argv[x].lower() == "-pass"):
                password = sys.argv[x+1]
            if (sys.argv[x].lower() == "-encalg"):
                encryptor.set_encryption_algorithm(sys.argv[x+1])
            if (sys.argv[x].lower() == "-nometadata"):
                encryptor.set_encrypt_metadata(False)
    
    if (inputF == ""):
        print("-input is required.\n")
        displayHelp()
        sys.exit(1)
    
    if (outputF == ""):
        print("-output is required.\n")
        displayHelp()
        sys.exit(1)
    
    if (certF != ""):
        cm.import_from_file(certF, certpass)
        encryptor.set_encryption_certificate_handle(cm.get_cert_handle())
    else:
        encryptor.set_user_password(password)

    try:
        encryptor.set_input_file(inputF)
        encryptor.set_output_file(outputF)

        encryptor.encrypt()
    
        print("PDF file successfully encrypted.")
    except Exception as e: 
        print(e)



