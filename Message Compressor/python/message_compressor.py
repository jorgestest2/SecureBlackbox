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
        "  messagecompressor -- SecureBlackbox MessageCompressor Demo Application\n\n"
        "SYNOPSIS\n"
        "  messagecompressor [-input input_file] [-output output_file] [-level level]\n\n"
        "DESCRIPTION\n"
        "  MessageCompressor demonstrates the usage of MessageCompressor from SecureBlackbox.\n"
        "  Used to create compressed PKCS#7 messages.\n\n"
        "  The options are as follows:\n\n"
        "  -input        An input file to compress (Required).\n\n"
        "  -output       Where the compressed file will be saved (Required).\n\n"
        "  -level        The comression level. \n\n"
        "EXAMPLES\n"
        "  messagecompressor -input C:\\pkcs7\\helloworld.txt -output C:\\pkcs7\\mypkcs7.cps \n\n"
        "  messagecompressor -input C:\\pkcs7\\helloworld.txt -output C:\\pkcs7\\mypkcs7.cps -level 7 \n\n"
    )
    
if (len(sys.argv) < 5):
    displayHelp()
    sys.exit(1)
else:
    compressor = MessageCompressor()
    
    inputF = ""
    outputF = ""

    for x in range(len(sys.argv)):
        if (sys.argv[x].startswith("-")):
            if (sys.argv[x].lower() == "-input"):
                inputF = sys.argv[x+1]
            if (sys.argv[x].lower() == "-output"):
                outputF = sys.argv[x+1]
            if (sys.argv[x].lower() == "-level"):
                compressor.set_compression_level(int(sys.argv[x+1]))
    
    if (inputF == ""):
        print("-input is required.\n")
        displayHelp()
        sys.exit(1)
    
    if (outputF == ""):
        print("-output is required.\n")
        displayHelp()
        sys.exit(1)
    
    try:
        compressor.set_input_file(inputF)
        compressor.set_output_file(outputF)
    
        compressor.compress()
    
        print("The file successfully compressed.")
    except Exception as e: 
        print(e)



