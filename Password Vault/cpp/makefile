#
# SecureBlackbox 2022 C++ Edition - Demo Application
#
# Copyright (c) 2023 /n software inc. - All rights reserved. - www.nsoftware.com
#

ifeq ($(shell uname -s), "Darwin") # MACOS
R_PATH=-Wl,-rpath,../../lib64/,-rpath,.

FRAMEWORK = -framework Carbon -framework Security
LD_FLAGS = -lsecureblackbox.22.0 -L../../lib64/
# EM: iconv is needed for multiple CBT products
LD_FLAGS_SRC = -lz -ldl 
OS_CFLAGS = -D UNIX64 -arch x86_64
MACOS = "darwin% Darwin% macos%"

all:
	g++ $(OS_CFLAGS) -D UNIX -o passwordvault passwordvault.cpp  -I../../include/ $(LD_FLAGS) $(FRAMEWORK) $(R_PATH) 
else # LINUX
ifeq ($(shell uname -m), x86_64)
  LIB=lib64
else
  LIB=lib
endif

R_PATH=-Wl,-rpath,../../$(LIB)/,-rpath,.
LD_FLAGS = -lsecureblackbox  -L../../$(LIB)/
LD_FLAGS_SRC = -lz -ldl 
# EM: enabling code generator options for hardware-accelerated encryption

all:
	g++ -D UNIX -o passwordvault passwordvault.cpp  -I../../include/ $(LD_FLAGS) $(R_PATH) 

src: ../../src/secureblackbox.o
	g++ -D UNIX -o passwordvault ../../src/secureblackbox.o passwordvault.cpp  -I../../include/ $(LD_FLAGS_SRC)

../../src/secureblackbox.o:
	g++ -c -fno-exceptions -fno-rtti -fPIC -o ../../src/secureblackbox.o ../../src/secureblackbox.cpp

clean:
	rm -f ../../src/*.o
	rm -f passwordvault *.o
endif