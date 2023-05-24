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
        "  xmldecryptor -- SecureBlackbox XMLDecryptor Demo Application\n\n"
        "SYNOPSIS\n"
        "  xmldecryptor [-input input_file] [-output output_file] [-cert certificate_file] [-certpass certificate_password] \n"
        "           [-pass key_password] [-external external_file] \n\n"
        "DESCRIPTION\n"
        "  XMLDecryptor demonstrates the usage of XMLDecryptor from SecureBlackbox.\n"
        "  Used to decrypt XML file.\n\n"
        "  The options are as follows:\n\n"
        "  -input        An input file to decrypt (Required). \n\n"
        "  -output       Where the decrypted XML file will be saved (Required). \n\n"
        "  -cert         The certificate used to decrypt file. \n\n"
        "  -certpass     The password for the certificate. \n\n"
        "  -pass         The password for the decrypting. \n\n"
        "  -external     The file where the external data will be saved. \n\n"
        "EXAMPLES\n"
        "  xmldecryptor -input C:\\xml\\myenc.xml -output C:\\xml\\myfile.xml -pass mtpassword \n"
        "  xmldecryptor -input C:\\xml\\myenc.xml -output C:\\xml\\myfile.xml -cert C:\\certs\\mycert.pfx -certpass test -external C:\\xml\\external.xml \n"
    )
    
def getKey(algorithm, password):
    reslen = 0

    if (algorithm.lower() == "AES128".lower()):
        reslen = 16
    elif (algorithm.lower() == "AES192".lower()):
        reslen = 24
    elif (algorithm.lower() == "AES256".lower()):
        reslen = 32
    elif (algorithm.lower() == "Camellia128".lower()):
        reslen = 16
    elif (algorithm.lower() == "Camellia192".lower()):
        reslen = 24
    elif (algorithm.lower() == "Camellia256".lower()):
        reslen = 32
    elif (algorithm.lower() == "DES".lower()):
        reslen = 8
    elif (algorithm.lower() == "3DES".lower()):
        reslen = 24
    elif (algorithm.lower() == "RC4".lower()):
        reslen = 16
    elif (algorithm.lower() == "SEED".lower()):
        reslen = 16

    res = password
    while (len(res) < reslen):
        res = res + "/" + password

    resb = res.encode('utf-8')
    print(resb[:reslen])
    return resb[:reslen]

def fireSaveExternalData(e):
    out_file = open(externalF, "wb")
    out_file.write(e.external_data)
    out_file.close()
    
def fireDecryptionInfoNeeded(e):
    cm = CertificateManager()
    
    t = ""
    if (decryptor.get_use_gcm()):
        t = "-GCM"
    print("Encryption method: " + decryptor.get_encryption_method() + t)

    if (decryptor.get_encrypted_data_type() == 0 or decryptor.get_encrypted_data_type() == None): # Element
        t = "Element"
    elif (decryptor.get_encrypted_data_type() == 1): # Content
        t = "Content"
    else:
        t = "External"
    print("Encrypted data type: " + t)

    if (decryptor.get_encrypt_key()):
        print("EncryptKey: true")
        if (decryptor.get_key_encryption_type() == 0 or decryptor.get_key_encryption_type() == None): # KeyTransport
            print("Key encryption type: transport")
            if (decryptor.get_key_transport_method() == 0 or decryptor.get_key_transport_method() == None): # RSA15
                t = "RSA v1.5"
            else:
                t = "RSA-OAEP"
            print("Key transport method: " + t)
        else:
            print("Key encryption type: wrap")
            print("Key wrap method: " + decryptor.get_key_wrap_method())
    else:
        print("EncryptKey: false")

    try:
        t = decryptor.config("KeyName")
        if (t != ""):
            print("Key name: " + t)

        t = decryptor.config("MimeType")
        if (t != ""):
            println("Mime type: " + t)
        print("")

        if (decryptor.get_encrypt_key()):
            if (decryptor.get_key_encryption_type() == 0 or decryptor.get_key_encryption_type() == None): # KeyTransport
                cm.import_from_file(certF, certpass)
                decryptor.set_key_decryption_cert_handle(cm.get_cert_handle())
            else:
                decryptor.set_key_decryption_key(getKey(decryptor.get_key_wrap_method(), keyPass))
        else:
            decryptor.set_decryption_key(getKey(decryptor.get_encryption_method(), keyPass))
    except Exception as e: 
        print(e)
    
if (len(sys.argv) < 3):
    displayHelp()
    sys.exit(1)
else:
    decryptor = XMLDecryptor()
    decryptor.on_save_external_data = fireSaveExternalData
    decryptor.on_decryption_info_needed = fireDecryptionInfoNeeded   
    
    inputF = ""
    outputF = ""
    certF = ""
    certpass = ""
    keyPass = ""
    externalF = ""
    
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
                keyPass = sys.argv[x+1]
            if (sys.argv[x].lower() == "-external"):
                externalFile = sys.argv[x+1]
                    
    if (inputF == ""):
        print("-input is required.\n")
        displayHelp()
        sys.exit(1)
            
    if (outputF == ""):
        print("-output is required.\n")
        displayHelp()
        sys.exit(1)

    try:
        decryptor.set_input_file(inputF)
        decryptor.set_output_file(outputF)

        decryptor.decrypt()
        
        print("XML file successfully decrypted")
    except Exception as e: 
        print(e)



