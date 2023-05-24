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
        "  xadesverifier -- SecureBlackbox XAdESVerifier Demo Application\n\n"
        "SYNOPSIS\n"
        "  xadesverifier [-input input_file] [-data original_data_file] [-cert certificate_file] [-certpass certificate_password] \\\n"
        "                [-detached] [-showsigs] [-showrefs]\n"
        "DESCRIPTION\n"
        "  XAdESVerifier demonstrates the usage of XAdESVerifier from SecureBlackbox.\n"
        "  Used to verify an XML Extended Signature (XAdES) from an XML file.\n\n"
        "  The options are as follows:\n\n"
        "  -input        A signature to verify (Required). If the signature is detached, this will take\n"
        "                the signature file and -data will take the original data.\n\n"
        "  -cert         The certificate used to verify the signature. Required if no key is included in the signature.\n\n"
        "  -certpass     The password for the certificate.\n\n"
        "  -detached     Whether the signature is detached. Use -datafile to specify the original data.\n\n"
        "  -data         The original data file.\n\n"
        "  -showinfo     Whether to display detailed XAdES options used with the signature.\n\n"
        "  -showrefs     Whether to display detailed results of reference verification.\n\n"
        "EXAMPLES\n"
        "  xadesverifier -input C:\\xades\\mysigned.xml\n"
        "  xadesverifier -input C:\\xades\\mysigned.xml -detached -data C:\\xades\\my.xml\n"
        "  xadesverifier -input C:\\xades\\mysigned.xml -cert C:\\certs\\mycert.pfx -certpass test\n"
        "  xadesverifier -input C:\\xades\\mysigned.xml -showinfo -showrefs\n"
    )

def fireReferenceValidated(e):
    if (showrefs):
        valid = "false"
        if (e.digest_valid):
            valid = "true"
        print("%.10s %.22s %.22s %s\n"%(e.id, e.uri, e.ref_type, valid))

def translateSigValidity(value):
    if (value == xsvValid):
        return "Valid"
    elif (value == xsvCorrupted):
        return "Corrupted"
    elif (value == xsvSignerNotFound):
        return "Signer not found"
    elif (value == xsvFailure):
        return "Failure"
    elif (value == xsvReferenceCorrupted):
        return "Invalid references"
    else:
        return "Unknown" 
    
def translateChainValidity(value):
    if (value == cvtValid):
        return "Valid"
    elif (value == cvtValidButUntrusted):
        return "Valid but untrusted"
    elif (value == cvtInvalid):
        return "Invalid"
    elif (value == cvtCantBeEstablished):
        return "Can't be established"
    else:
        return "Unknown" 
    
def translateXAdESVersion(ver):
    if (ver == 1):
        return "1.1.1"
    elif (ver == 2):
        return "1.2.2"
    elif (ver == 3):
        return "1.3.2"
    elif (ver == 4):
        return "1.4.1"
    else:
        return "Unknown"

def translateXAdESForm(form):
    if (form == 1):
        return "XAdES"
    elif (form == 2):
        return "XAdES-BES"
    elif (form == 3):
        return "XAdES-EPES"
    elif (form == 4):
        return "XAdES-T"
    elif (form == 5):
        return "XAdES-C"
    elif (form == 6):
        return "XAdES-X"
    elif (form == 7):
        return "XAdES-X-L"
    elif (form == 8):
        return "XAdES-A"
    elif (form == 9):
        return "XAdES-E-BES"
    elif (form == 10):
        return "XAdES-E-EPES"
    elif (form == 11):
        return "XAdES-E-T"
    elif (form == 12):
        return "XAdES-E-C"
    elif (form == 13):
        return "XAdES-E-X"
    elif (form == 14):
        return "XAdES-E-X-Long"
    elif (form == 15):
        return "XAdES-E-X-L"
    elif (form == 16):
        return "XAdES-E-A"
    else:
        return "Unknown"

if (len(sys.argv) < 3):
    displayHelp()
    sys.exit(1)
else:
    verifier = XAdESVerifier()
    verifier.on_reference_validated = fireReferenceValidated
    cm = CertificateManager()
    
    inputF = ""
    certF = ""
    certpass = ""
    dataF = ""
    detached = False
    showinfo = False
    showrefs = False
    
    try:
        for x in range(len(sys.argv)):
            if (sys.argv[x].startswith("-")):
                if (sys.argv[x].lower() == "-input"):
                    inputF = sys.argv[x+1]
                if (sys.argv[x].lower() == "-data"):
                    dataF = sys.argv[x+1]
                if (sys.argv[x].lower() == "-cert"):
                    certF = sys.argv[x+1]
                if (sys.argv[x].lower() == "-certpass"):
                    certpass = sys.argv[x+1]
                if (sys.argv[x].lower() == "-detached"):
                    detached = True
                if (sys.argv[x].lower() == "-showinfo"):
                    showinfo = True
                if (sys.argv[x].lower() == "-showrefs"):
                    showrefs = True
                    
        if (inputF == ""):
            print("-input is required.\n")
            displayHelp()
            sys.exit(1)
            
        if (detached and dataF == ""):
            print("-data is required if -detached is used.\n")
            displayHelp()
            sys.exit(1)

        verifier.set_input_file(inputF)

        if not (certF == ""):
            cm.import_from_file(certF, certpass)
            verifier.set_known_cert_count(1)
            verifier.set_known_cert_handle(0, cm.get_cert_handle())

        if showrefs:
            print("ID URI RefType DigestValid\n--------------------------")
            
        if detached:
            verifier.set_data_file(dataF)
            verifier.set_data_type(1) # cxdtBinary
            verifier.set_data_uri(os.path.basename(dataF))
            verifier.verify_detached()
        else:
            verifier.verify()
        
        for x in range(verifier.get_signature_count()):
            print("Signature " + str(x+1))
            print("  Claimed signing time: " + verifier.get_signature_claimed_signing_time(x))
            print("  Timestamp: " + verifier.get_signature_validated_signing_time(x))
            print("  Signature Validation Result: " + translateSigValidity(verifier.get_signature_signature_validation_result(x)))
            print("  Chain Validation Result: " + translateChainValidity(verifier.get_signature_chain_validation_result(x)) + "\n")

            if showinfo and (verifier.get_signature_signature_validation_result(0) == xsvValid):
                print("XAdES Detailed Information:")
                print("   XAdES Version: " + translateXAdESVersion(verifier.get_x_ad_es_version()))
                print("   XAdES Form: " + translateXAdESForm(verifier.get_x_ad_es_form()))
    except Exception as e: 
        print(e)



