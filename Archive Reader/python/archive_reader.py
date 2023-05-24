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
        "  archivereader -- SecureBlackbox ArchiveReader Demo Application\n\n"
        "SYNOPSIS\n"
        "  archivereader [-arctype archive_type] [-input input_file] [-output output_path] [-pass decryption_password]\n\n"
        "DESCRIPTION\n"
        "  ArchiveReader demonstrates the usage of ArchiveReader from SecureBlackbox.\n"
        "  Used to extract files from archive.\n\n"
        "  The options are as follows:\n\n"
        "  -arctype      The type of archive (Required). Valid values:\n\n"
        "                  1 - ZIP\n"
        "                  2 - GZIP\n"
        "                  3 - BZIP_2\n"
        "                  4 - TAR\n"
        "                  5 - TAR_GZIP\n"
        "                  6 - TAR_BZIP_2\n\n"
        "  -input        An input archive file (Required).\n\n"
        "  -output       Where the extracted files will be saved.\n\n"
        "  -pass         The password for the encrypted archive.\n\n"
        "EXAMPLES\n"
        "  archivereader -arctype 1 -input C:\\archive\\helloworld.zip -output C:\\archive \n\n"
        "  archivereader -arctype 5 -input C:\\archive\\helloworld.tar -pass mypassword \n\n"
    )
    
if (len(sys.argv) < 5):
    displayHelp()
    sys.exit(1)
else:
    archive = ArchiveReader()
    
    arctype = 0
    inputArc = ""
    output = ""

    try:
        for x in range(len(sys.argv)):
            if (sys.argv[x].startswith("-")):
                if (sys.argv[x].lower() == "-arctype"):
                    arctype = int(sys.argv[x+1])
                if (sys.argv[x].lower() == "-input"):
                    inputArc = sys.argv[x+1]
                if (sys.argv[x].lower() == "-output"):
                    output = sys.argv[x+1]
                if (sys.argv[x].lower() == "-pass"):
                    archive.set_decryption_password(sys.argv[x+1])
                
        if (arctype == 0):
            print("-arctype is required.\n")
            displayHelp()
            sys.exit(1)
    
        if (inputArc == ""):
            print("-input is required.\n")
            displayHelp()
            sys.exit(1)

        archive.open(arctype, inputArc)
    
        print("List of files in the archive")
        for y in range(archive.get_file_count()):
            print("    %s"%(archive.get_file_path(y)))
        print("")
                   
        archive.extract_all(output, True)
    
        print("All files from archive extracted.")
    except Exception as e: 
        print(e)



