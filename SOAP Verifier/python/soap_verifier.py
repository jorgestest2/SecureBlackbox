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
        "  soapverifier -- SecureBlackbox SOAPVerifier Demo Application\n\n"
        "SYNOPSIS\n"
        "  soapverifier [-input input_file] [-cert certificate_file] [-certpass certificate_password] [-showrefs]\n"
        "DESCRIPTION\n"
        "  SOAPVerifier demonstrates the usage of SOAPVerifier from SecureBlackbox.\n"
        "  Used to verify the signature.\n\n"
        "  The options are as follows:\n\n"
        "  -input        An input file to verify (Required).\n\n"
        "  -cert         The certificate used to sign files.\n\n"
        "  -certpass     The password for the signing certificate.\n\n"
        "  -showrefs     Whether to display detailed results of reference verification.\n\n"
        "EXAMPLES\n"
        "soapverifier -input C:\\soap\\mysoap.scs -cert C:\\certs\\mycert.pfx -certpass mypassword -showrefs\n\n"
    )

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
    
def fireReferenceValidated(e):
    if (showrefs):
        valid = "false"
        if (e.digest_valid):
            valid = "true"
        print("%.10s %.22s %.22s %s\n"%(e.id, e.uri, e.ref_type, valid))
        
if (len(sys.argv) < 3):
    displayHelp()
    sys.exit(1)
else:
    verifier = SOAPVerifier()
    verifier.on_reference_validated = fireReferenceValidated
    cm = CertificateManager()
    
    inputF = ""
    certF = ""
    certpass = ""
    showrefs = False
    
    try:
        for x in range(len(sys.argv)):
            if (sys.argv[x].startswith("-")):
                if (sys.argv[x].lower() == "-input"):
                    inputF = sys.argv[x+1]
                if (sys.argv[x].lower() == "-cert"):
                    certF = sys.argv[x+1]
                if (sys.argv[x].lower() == "-certpass"):
                    certpass = sys.argv[x+1]
                if (sys.argv[x].lower() == "-showrefs"):
                    showrefs = True
                    
        if (inputF == ""):
            print("-input is required.\n")
            displayHelp()
            sys.exit(1)

        verifier.set_input_file(inputF)

        if not (certF == ""):
            cm.import_from_file(certF, certpass)
            verifier.set_known_cert_count(1)
            verifier.set_known_cert_handle(0, cm.get_cert_handle())

        if showrefs:
            print("ID URI RefType DigestValid\n--------------------------")
            
        verifier.verify()
        
        print("There are %i signatures in this file.\n"%(verifier.get_signature_count()))
        for x in range(verifier.get_signature_count()):
            print("Signature " + str(x+1))
            print("  Claimed signing time: " + verifier.get_signature_claimed_signing_time(x))
            print("  Timestamp: " + verifier.get_signature_validated_signing_time(x))
            print("  Signature Validation Result: " + translateSigValidity(verifier.get_signature_signature_validation_result(x)))
            print("  Chain Validation Result: " + translateChainValidity(verifier.get_signature_chain_validation_result(x)) + "\n")

    except Exception as e: 
        print(e)



