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
        "  messagedecompressor -- SecureBlackbox MessageDecompressor Demo Application\n\n"
        "SYNOPSIS\n"
        "  messagedecompressor [-input input_file] [-output output_file]\n\n"
        "DESCRIPTION\n"
        "  MessageDecompressor demonstrates the usage of MessageDecompressor from SecureBlackbox.\n"
        "  Used to decompressed PKCS#7 messages.\n\n"
        "  The options are as follows:\n\n"
        "  -input        An input file to decompress (Required).\n\n"
        "  -output       Where the original file will be saved (Required).\n\n"
    )
    
if (len(sys.argv) < 5):
    displayHelp()
    sys.exit(1)
else:
    decompressor = MessageDecompressor()
    
    inputF = ""
    outputF = ""

    for x in range(len(sys.argv)):
        if (sys.argv[x].startswith("-")):
            if (sys.argv[x].lower() == "-input"):
                inputF = sys.argv[x+1]
            if (sys.argv[x].lower() == "-output"):
                outputF = sys.argv[x+1]
    
    if (inputF == ""):
        print("-input is required.\n")
        displayHelp()
        sys.exit(1)
    
    if (outputF == ""):
        print("-output is required.\n")
        displayHelp()
        sys.exit(1)
    
    try:
        decompressor.set_input_file(inputF)
        decompressor.set_output_file(outputF)
    
        decompressor.decompress()
    
        print("The file successfully decompressed.")
    except Exception as e: 
        print(e)



