#
# SecureBlackbox 2022 Python Edition - Demo Application
#
# Copyright (c) 2023 /n software inc. - All rights reserved. - www.nsoftware.com
#

import sys
import string
from secureblackbox import *

input = sys.hexversion<0x03000000 and raw_input or input

def fireCertificateValidate(e):
    e.accept = 1
    
def fireDocumentStart(e):
    print("--- Document started ---")
    
def fireDocumentFinish(e):
    print("--- Document finished ---\n")
    
def firePreparedHeaders(e):
    print("Headers sent: ")
    for x in range(http.get_req_header_count()):
        print("   " + http.get_req_header_name(x) + ": " + http.get_req_header_value(x))
    print("")
    
def fireReceivingHeaders(e):
    print("Headers received: ")
    for x in range(http.get_resp_header_count()):
        print("   " + http.get_resp_header_name(x) + ": " + http.get_resp_header_value(x))
    print("")
    
def fireRedirection(e):
    print("Request redirected to " + e.new_url + "\n")
    e.allow_redirection = 1
    
if (len(sys.argv) < 2):
    print("usage: httpget url");
    print("Options: ");
    print("  url    the url to fetch (Required)");
    print("\nExample: httpget https://www.google.com");  
else:
    http = HTTPClient()
    http.on_tls_cert_validate = fireCertificateValidate
    http.on_document_begin = fireDocumentStart
    http.on_document_end = fireDocumentFinish
    http.on_headers_prepared = firePreparedHeaders
    http.on_headers_received = fireReceivingHeaders
    http.on_redirection = fireRedirection
    
    try:
        http.get(sys.argv[2])
        print(http.get_output_string().encode('utf8'))
    except Exception as e: 
        print(e)

