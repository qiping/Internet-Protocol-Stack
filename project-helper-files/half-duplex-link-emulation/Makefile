# Makefile for simple udp client and echo server

# This rule describes how to build a .o file from a .c file
# -Wall tells gcc to print all warnings!

.c.o:
	gcc -c -Wall $<


# on solaris we need to explicitly include the socket and name server
# libraries, this because sockets are not supported by the O.S. directly,
# but are a library that calls the native (XTI) network API. 
# Leave this commented out unless you are on a Sun running Solaris

#LIBS= -lsocket -lnsl

# by default Make will build the first target - so here we define the
# first target "all", which depends on targets "client" and "server"

all: sender receiver

# Here are the rules that tell make how to build the executables
# named "client" and "server". If LIBS is not defined, including it
# does no harm!

sender: sender.o 
	gcc -o sender sender.o ${LIBS}

receiver: receiver.o 
	gcc -o receiver receiver.o ${LIBS}


clean:
	rm *~ *.o sender receiver

