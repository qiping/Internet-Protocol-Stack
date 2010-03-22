/* UDP half-duplex link emulation program: Sender Side */
#include <stdio.h>      /* standard C i/o facilities */
#include <stdlib.h>     /* needed for atoi() */
#include <unistd.h>  	/* defines STDIN_FILENO, system calls,etc */
#include <sys/types.h>  /* system data type definitions */
#include <sys/socket.h> /* socket specific definitions */
#include <sys/wait.h> /* socket specific definitions */
#include <netinet/in.h> /* INET constants and stuff */
#include <arpa/inet.h>  /* IP address conversion stuff */
#include <string.h>     /* for string operations, e.g. strstr() */
#include <errno.h>      /* for errno global variable */
#include <math.h>

static int L = 0; // packet loss fraction (between 0 and 100)
static int C = 0; // packet corruption fraction (between 0 and 100)

/* Wrapper function to emulate an erroneous link */
int sendto_garbled(int s, const void *msg, size_t len, int flags, 
		   const struct sockaddr *to, socklen_t tolen)
{
  int localint, i;
  char * localpoint;

  srand48(11); // initialize the random number generator

  /* Decide whether to loose this packet */
  if (drand48()*100 < L)
    return len; // act as if the packet was sent correctly!

  /* Decide whether to corrupt this packet */
  if (drand48()*100 < C)
    if (len > 0) {
      // pick a random location to corrupt
      localint = round(drand48()*len);
      i = 0;
      localpoint = (char *)msg;
      while (i < localint) {
	i++;
	localpoint++;
      }
      *localpoint = ~(*localpoint);
    }

  return sendto(s, msg, len, flags, (struct sockaddr *)to, tolen);
}

