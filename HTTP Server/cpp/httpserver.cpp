/*
 * SecureBlackbox 2022 C++ Edition - Demo Application
 *
 * Copyright (c) 2023 /n software inc. - All rights reserved. - www.nsoftware.com
 *
 */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "../../include/secureblackbox.h"

class MyHTTPServer : public HTTPServer
{
public:

    int FireGetRequest(HTTPServerGetRequestEventParams* e) override {
        wprintf(L"Request received (page: %s)\r\n", e->URI);

        this->SetResponseStatus(e->ConnectionID, 200);
        this->SetResponseString(e->ConnectionID,
                                "<html><head><title>SecureBlackbox HTTP server</title></head><body><h1>Hello there!</h1></body></html>",
                                "text/html");

        e->Handled = true;

        return 0;
    }
};

int main(int argc, char* argv[]) {
    if (argc < 2) {
        wprintf(L"Usage: httpserver <listening-port>\r\n\r\n");
        wprintf(L"Example: httpserver 80\r\n\r\n");
        wprintf(L"Press enter to continue...\r\n");
        getchar();

        return 1;
    }

    const int port = atoi(argv[1]);

    MyHTTPServer httpserver;

    httpserver.SetPort(port);

    const int res = httpserver.Start();
    if (res == 0) {
        wprintf(L"HTTP server started on port %d. Press enter to stop and exit.\r\n", port);
        getchar();

        httpserver.Stop();

        wprintf(L"Server stopped. Bye.\r\n");
        return 0;
    } else {
        wprintf(L"Failed to run the server, error %d\r\n", res);

        return 2;
    }
}


