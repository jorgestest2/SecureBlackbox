/*
 * SecureBlackbox 2022 C++ Edition - Demo Application
 *
 * Copyright (c) 2023 /n software inc. - All rights reserved. - www.nsoftware.com
 *
 */

#include <stdio.h>
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
        "  messageencryptor -- SecureBlackbox MessageEncryptor Demo Application\n\n"
        "SYNOPSIS\n"
        "  messageencryptor [-input input_file] [-output output_file] [-cert certificate_file] [-certpass certificate_password] [-encalg encryption_algorithm] \n\n"
        "DESCRIPTION\n"
        "  MessageEncryptor demonstrates the usage of MessageEncryptor from SecureBlackbox.\n"
        "  Used to create encrypted ('enveloped') PKCS#7 messages. \n\n"
        "  The options are as follows:\n\n"
        "  -input        An input file to encrypt (Required).\n\n"
        "  -output       Where the encrypted file will be saved (Required).\n\n"
        "  -cert         The certificate used to encrypt file (Required).\n\n"
        "  -certpass     The password for the encryption certificate (Required).\n\n"
        "  -encalg       The encryption algorithm. Valid values: 3DES, RC4, RC2, AES128, AES192, AES256, Twofish128 \n\n"
        "EXAMPLES\n"
        "  messageencryptor -input C:\\pkcs7\\helloworld.txt -output C:\\pkcs7\\enc.pkcs7 -cert C:\\certs\\mycert.pfx -certpass mypassword \n\n"
        "  messageencryptor -input C:\\pkcs7\\helloworld.txt -output C:\\pkcs7\\enc.pkcs7 -cert C:\\certs\\mycert.pfx -certpass mypassword -alg AES128 \n\n"
    );
}

int main(int argc, char** argv) {
    MessageEncryptor encryptor;
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
    if (optext(argc, argv, "-encalg")) {
        encryptor.SetEncryptionAlgorithm(optval(argc, argv, "-encalg"));
    }

    // Required options
    encryptor.SetInputFile(input);
    encryptor.SetOutputFile(output);
    cm.ImportFromFile(cert, certpass);
    encryptor.SetEncryptionCertHandle(cm.GetCertHandle());

    // Encrypt
    if (encryptor.Encrypt()) {
        goto done;
    }
    printf("The file successfully encrypted.\n");

done:
    if (encryptor.GetLastErrorCode()) {
        printf("Error: [%i] %s\n", encryptor.GetLastErrorCode(), encryptor.GetLastError());
    }
    getchar();
}


