/*
 * SecureBlackbox 2022 C++ Edition - Demo Application
 *
 * Copyright (c) 2023 /n software inc. - All rights reserved. - www.nsoftware.com
 *
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "../../include/secureblackbox.h"

namespace ArgParser {
    static char* optval(int argc, char** argv, const char* option) {
        for (int x = 0; x < argc - 1; x++) {
            if (!strcmp(argv[x], option)) {
                return argv[x + 1];
            }
        }
        return (char*)"";
    }

    static bool optext(int argc, char** argv, const char* option) {
        for (int x = 0; x < argc; x++) {
            if (!strcmp(argv[x], option)) {
                return true;
            }
        }
        return false;
    }
};

using namespace ArgParser;

void displayHelp() {
    printf(
        "NAME\n"
        "  soapsigner -- SecureBlackbox SOAPSigner Demo Application\n\n"
        "SYNOPSIS\n"
        "  soapsigner [-input input_file] [-output output_file] [-cert certificate_file] [-certpass certificate_password]\n"
        "             [-signbody] [-hashalg hash_algorithm] [-sigtype signature_type]\n\n"
        "DESCRIPTION\n"
        "  SOAPSigner demonstrates the usage of SOAPSigner from SecureBlackbox.\n"
        "  Used to create SOAP or WSS signatures.\n\n"
        "  The options are as follows:\n\n"
        "  -input        An input file to sign (Required).\n\n"
        "  -output       Where the signed file will be saved (Required).\n\n"
        "  -cert         The certificate used to sign files (Required).\n\n"
        "  -certpass     The password for the signing certificate (Required).\n\n"
        "  -sigtype      The type of signature to use. Enter the corresponding number. Valid values:\n\n"
        "                  1 - SST_WSSSIGNATURE\n"
        "                  2 - SST_SOAPSIGNATURE\n\n"
        "  -hashalg      The hash algorithm.\n\n"
        "  -signbody     Whether to sign body.\n\n"
        "EXAMPLES\n"
        "  soapsigner -input C:\\soap\\helloworld.txt -output C:\\soap\\mysoap.scs -cert C:\\certs\\mycert.pfx -certpass mypassword\n\n"
        "  soapsigner -input C:\\soap\\helloworld.txt -output C:\\soap\\mysoap.scs -cert C:\\certs\\mycert.pfx -certpass mypassword \\\n"
        "             -sigtype 2 -hashalg SHA256 -signbody\n\n"
    );
}

int main(int argc, char** argv) {
    SOAPSigner signer;
    CertificateManager cm;

    // Validate input
    if (argc < 8) {
        displayHelp();
        goto done;
    }

    char* input = optval(argc, argv, "-input");
    if (!strcmp(input, "")) {
        printf("-input is required.");
        displayHelp();
        goto done;
    }

    char* output = optval(argc, argv, "-output");
    if (!strcmp(output, "")) {
        printf("-output is required.");
        displayHelp();
        goto done;
    }

    char* cert = optval(argc, argv, "-cert");
    if (!strcmp(cert, "")) {
        printf("-cert is required.");
        displayHelp();
        goto done;
    }

    char* certpass = optval(argc, argv, "-certpass");
    if (!strcmp(certpass, "")) {
        printf("-certpass is required.");
        displayHelp();
        goto done;
    }

    // Additional options
    if (optext(argc, argv, "-signbody")) {
        signer.AddBodyReference("", true);
    }

    signer.SetNewSigSignatureType(optext(argc, argv, "-sigtype") ?
                                atoi(optval(argc, argv, "-sigtype")) :
                                signer.SetNewSigSignatureType(SST_WSSSIGNATURE));


    if (optext(argc, argv, "-hashalg")) {
        signer.SetNewSigHashAlgorithm(optval(argc, argv, "-hashalg"));
    }

    // Required options
    signer.SetInputFile(input);
    signer.SetOutputFile(output);
    cm.ImportFromFile(cert, certpass);
    signer.SetSigningCertHandle(cm.GetCertHandle());

    // Sign & Create
    if (signer.Sign()) goto done;
    printf("SOAP message successfully signed.\n");

done:
    if (signer.GetLastErrorCode()) {
        printf("Error: [%i] %s\n", signer.GetLastErrorCode(), signer.GetLastError());
    }
    getchar();
}


