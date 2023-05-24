# Sample Projects

## Requirements
These sample projects require the latest version of SecureBlackbox.  Please download from:

> Download: [https://www.nsoftware.com/secureblackbox](https://www.nsoftware.com/secureblackbox)

## Sample Projects
The sample projects demonstrate the usage of the SecureBlackbox components in a simple, 
straightforward way.  They are not complete applications and they are not intended to be.
Error handling and other checks are simplified for clarity.

| Sample Project | Description |
| --- | --- |
| [ASiC Signer](./ASiC%20Signer) | A simple ASiC signer sample created with the ASiCSigner component. Use it to create XAdES-signed, CAdES-signed, and timestamped archives. |
| [ASiC Verifier](./ASiC%20Verifier) | A simple ASiC verifier created with the ASiCVerifier component. Use it to verify ASiC signatures. |
| [Archive Reader](./Archive%20Reader) | A simple Archive Reader sample created with the ArchiveReader component. Use it to read and extract files from archives. |
| [Archive Writer](./Archive%20Writer) | A simple Archive Writer sample created with the ArchiveWriter component. Use it to create and modify archives. |
| [Authenticode Signer](./Authenticode%20Signer) | A simple authenticode signer created with the AuthenticodeSigner component. Use it to sign EXE and DLL files in accordance with MS Authenticode technology. |
| [Authenticode Verifier](./Authenticode%20Verifier) | A simple authenticode verifier based on the AuthenticodeVerifier component. Use it to verify signed EXE and DLL files. |
| [CAdES Signer](./CAdES%20Signer) | A simple CAdES generator created with the CAdESSigner component. The sample supports creation of CAdES signatures of different conformance levels. |
| [CAdES Verifier](./CAdES%20Verifier) | A simple CAdES processor created around the CAdESVerifier component. |
| [DCAuth Service](./DCAuth%20Service) | A simple example of the DC technology. The sample incorporates two counterparts of DC: the application part is represented with PDFSigner control, and the private key part is represented with DCAuth control. |
| [DCAuth WebServer](./DCAuth%20WebServer) | A simple example of the DC technology. The sample incorporates two counterparts of DC: the application part is represented with PDFSigner control, and the private key part is represented with DCAuth control. |
| [DTLS Client](./DTLS%20Client) | A simple DTLS client sample. Use this demo together with its DTLS Server counterpart. |
| [DTLS Server](./DTLS%20Server) | A simple DTLS server sample. Use this demo together with its DTLS Client counterpart. |
| [Distributed Crypto](./Distributed%20Crypto) | A simple example of the DC technology. The sample incorporates two counterparts of DC: the application part is represented with PDFSigner control, and the private key part is represented with DCAuth control. |
| [FTP Client](./FTP%20Client) | A simple FTP client implemented around the FTPClient control. A number of core FTP operations, as well as various TLS modes, are supported. |
| [FTP Server](./FTP%20Server) | A fully functional FTP server application built around the FTPServer component. Core file operations, user management, and various TLS modes are supported. |
| [HTTP Get](./HTTP%20Get) | This tiny sample illustrates the HTTP GET functionality. |
| [HTTP Post](./HTTP%20Post) | A simple HTTP POST example. |
| [HTTP Server](./HTTP%20Server) | A basic HTTP server application built around the HTTPServer component. Straightforward HTTP request handling is supported. |
| [Hash Function](./Hash%20Function) | Use this example to learn about calculate hash with HashFunction control. |
| [IMAP Client](./IMAP%20Client) | A small mail receiving program based on the IMAPClient component. It can list mailboxes on the server, list messages in the selected mailbox, download them from the server and upload local messages to the server. |
| [JAdES Signer](./JAdES%20Signer) | A simple example of creating JWS/JAdES signature with JAdESSigner control. |
| [JAdES Verifier](./JAdES%20Verifier) | Use this demo to learn how to verify JWS/JAdES signature using the JAdESVerifier control. |
| [JWC Encryptor](./JWC%20Encryptor) | Use this example to learn about encrypting and decrypting messages in JSON format with SymmetricCrypto control. |
| [JWC Signer](./JWC%20Signer) | Use this example to learn about signing and verifying messages in JSON format with PublicKeyCrypto control. |
| [KMIP Client](./KMIP%20Client) | A powerful KMIP client sample built around the KMIPClient component. Most of KMIP functionality, such as certificate management and cryptographic operations, is supported. |
| [KMIP Server](./KMIP%20Server) | A powerful KMIP server sample built with the KMIPServer component. Most of KMIP functionality, such as certificate management and cryptographic operations, is supported. |
| [Mail Reader](./Mail%20Reader) | A simple e-mail messages parsing and reading demo based on the MailReader component. |
| [Mail Writer](./Mail%20Writer) | A simple e-mail messages creation demo based on the MailWriter component. |
| [Message Compressor](./Message%20Compressor) | A simple example of PKCS7-compliant message compressing functionality. |
| [Message Decompressor](./Message%20Decompressor) | This small example illustrates the PKCS7-compliant message decompressing functionality. |
| [Message Decryptor](./Message%20Decryptor) | A lightweight example of PKCS7 messaged decryption, built around the MessageDecryptor component. |
| [Message Encryptor](./Message%20Encryptor) | This small demo illustrates the use of PKCS7 certificate-based messaged encryption functionality. |
| [Message Signer](./Message%20Signer) | Learn how to implement PKCS7 signing in your application with this simple example. MessageSigner is a simpler version of CAdESSigner, which excludes the AdES piece. |
| [Message Timestamp Verifier](./Message%20Timestamp%20Verifier) | This small demo shows how to validate PKCS7 timestamped messages with the MessageTimestampVerifier class. |
| [Message Timestamper](./Message%20Timestamper) | This example illustrates the creation of PKCS7 timestamped messages. |
| [Message Verifier](./Message%20Verifier) | This sample illustrates the verification of signed PKCS7 documents. For advanced validations that include certificate chain processing see CAdESVerifier. |
| [OTP Client](./OTP%20Client) | A very simple OTP password generator. TOTP and HOTP protocols are supported. |
| [OTP Server](./OTP%20Server) | A simple OTP password generator (server side). HOTP and TOTP protocols are supported. |
| [Office Decryptor](./Office%20Decryptor) | A very simple office document decryptor app built using the OfficeDecryptor control. |
| [Office Encryptor](./Office%20Encryptor) | A lightweight encryptor of Office documents. |
| [Office Signer](./Office%20Signer) | A simple example of Office document signing with OfficeSigner control. |
| [Office Verifier](./Office%20Verifier) | Use this demo to learn how to verify signed Office document using the OfficeVerifier control. |
| [PDF Decryptor](./PDF%20Decryptor) | A simple PDF decryption example. Both certificate- and password-encrypted document types are supported. |
| [PDF Encryptor](./PDF%20Encryptor) | A tiny PDF encryption example which supports password- and certificate-based encryption. |
| [PDF Signer](./PDF%20Signer) | An easy-to-use PDF signing example. Both generic and PAdES signatures are supported. |
| [PDF Signer External](./PDF%20Signer%20External) | An easy-to-use PDF signing example. Both generic and PAdES signatures are supported. |
| [PDF Verifier](./PDF%20Verifier) | This small demo illustrates the use of the PDFVerifier control for processing PDF signatures. |
| [PGP Keys](./PGP%20Keys) | A simple PGP keyring manager. Generation and browsing of PGP keys are supported. |
| [PGP Reader](./PGP%20Reader) | Use this easy-to-use example to learn about integrating PGP decryption and verification into your application. |
| [PGP Writer](./PGP%20Writer) | A simple PGP encryptor-plus-verifier. |
| [PKCS11 Certificate Storage](./PKCS11%20Certificate%20Storage) | An easy-to-use Certificate Storage for work with PKCS11 storages. |
| [POP Client](./POP%20Client) | A small mail receiving program based on the POP3Client component. It can connect to a POP3 server and receive messages from the mailbox or delete messages directly on the server. |
| [Password Vault](./Password%20Vault) | A simple Password Vault to save user's information and passwords. |
| [Public Key Crypto](./Public%20Key%20Crypto) | Use this example to learn about sign and verify with PublicKeyCrypto control. |
| [REST Server](./REST%20Server) | The sample shows interaction between a web page and a simple REST server built around the RESTServer control. |
| [SAML IdP Server](./SAML%20IdP%20Server) | A simple SAML IdP server built with the SAMLIDPServer component. The sample supports creation of the identity provider and user authorization for SAML protocol. |
| [SAML SP Server](./SAML%20SP%20Server) | A simple SAML SP server built with the SAMLSPServer control. The sample illustrates creation of a SAML-protected web server. |
| [SFTP Client](./SFTP%20Client) | A small but powerful SFTP client built with the SFTPClient component. Directory browsing, uploads, and downloads are supported. |
| [SFTP Server](./SFTP%20Server) | A powerful SFTP server created around the SFTPServer component. Most of SFTP operations are supported. |
| [SMTP Client](./SMTP%20Client) | A small mail sender program based on the SMTPClient component. Just creates a plain text message and sends it to the specified SMTP server. |
| [SOAP Signer](./SOAP%20Signer) | This small example illustrates the signing of SOAP messages with SOAPSigner control. |
| [SOAP Verifier](./SOAP%20Verifier) | Use this example to learn about SOAP signature validation with SOAPVerifier control. |
| [Simple Authenticator](./Simple%20Authenticator) | A simple Authenticator created with the Authenticator component. Use it to user authentication. |
| [Simple PDF Signer](./Simple%20PDF%20Signer) | An easy-to-use PDF signing example. Supported PKCS11 and Win32 storages. |
| [Symmetric Crypto](./Symmetric%20Crypto) | Use this example to learn about encrypt and decrypt with SymmetricCrypto control. |
| [TLS Client](./TLS%20Client) | A simple TLS client sample. Use this demo together with its TLS Server counterpart. |
| [TLS Server](./TLS%20Server) | A simple TLS server sample. Use this demo together with its TLS Client counterpart. |
| [XAdES Signer](./XAdES%20Signer) | Use this demo to learn how to create signed XAdES documents of various levels. |
| [XAdES Verifier](./XAdES%20Verifier) | This small demo illustrates the use of XAdESVerifier for XAdES signature validations. |
| [XML Decryptor](./XML%20Decryptor) | A tiny XML decryption example. |
| [XML Encryptor](./XML%20Encryptor) | A tiny XML encryption example. |
| [XML Signer](./XML%20Signer) | This small example shows how to create basic XML signatures with XMLSigner control. See XAdESSigner for more sophisticated signatures. |
| [XML Verifier](./XML%20Verifier) | This sample demonstrates the use of XMLVerifier for validating basic XML signatures. For validations involving certificate chain checks, see XAdESVerifier. |

## Support
If you have questions or need help, please contact support@nsoftware.com or explore other support options 
at www.nsoftware.com.
