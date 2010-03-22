/* UDP half-duplex link emulation program: Sender Side */
#include <stdio.h>      /* standard C i/o facilities */
#include <stdlib.h>     /* needed for atoi() */
#include <unistd.h>  	/* defines STDIN_FILENO, system calls,etc */
#include <sys/types.h>  /* system data type definitions */
#include <sys/socket.h> /* socket specific definitions */
#include <sys/wait.h> /* socket specific definitions */
#include <netinet/in.h> /* INET constants and stuff */
#include <arpa/inet.h>  /* IP address conversion stuff */
#include <netdb.h>	/* gethostbyname */
#include <string.h>     /* for string operations, e.g. strstr() */
#include <errno.h>      /* for errno global variable */

#define MAXMODE     9    // max "netascii"
#define MAXBUF      1500 // max datagram size
#define MAXERR      500 // max size of the ErrMsg field

/* the structure that keeps information about a datagram */
struct message{
  int size; // size of the whole datagram in bytes
  int opcode; 
  int errcode; 
  char data[512];
  char mode[MAXMODE]; // transfer mode 1-netascii, 0-ascii
  char errstr[MAXERR];
};

/* constructs a datagram from the information in the message m. takes 
   care of network byte order. */
void buildmsg(char * buff, struct message m, int mode) {
  int tmp, i;

  tmp = htons(m.opcode);
  memcpy(buff,(char *)&tmp,2);
  buff += 2;

  if (m.opcode == 1) {
    for (i=0; i<m.size-4; i++) {
      *buff = m.data[i]; 
      buff++;
    }    
  }else if (m.opcode == 2) {
    tmp = htons(m.errcode);
    memcpy(buff,(char *)&tmp,2);
    buff += 2;
    for (i=0; i<m.size-4; i++) {
      *buff = m.errstr[i]; 
      buff++;
    }
  }
}

/* replaces CRLFs in s with '\n's, and returns the # of CRLFs that has 
   been cleaned. Also, s does not include CRLFs any more. */
int cleanCRLF(char *s) {
  char crlf[3] = "\r\n";
  char *tmp, *tmp1, *tmp2;
  int count=0; // # of CRLFs cleaned

  while ((tmp=strstr(s,crlf)) != NULL) {
    count++; 
    *tmp = '\n'; // replace '\r' with '\n'
    tmp++;

    tmp1 = tmp;
    tmp2 = tmp;
    tmp2++;
    while (tmp2 != NULL) {
      *tmp1 = *tmp2;
      tmp1++;
      tmp2++;      
    }
    *tmp1 = *tmp2;
  }
  return (count);
}

/* gets information from the received datagram m, and returns them in a
   message structure. */
struct message splitmsg(char * m, int pktsize, int mode) {
  int tmpint;
  struct message tmp;

  memcpy(&tmpint,m,2);
  tmp.opcode = ntohs(tmpint);
  tmp.size = pktsize;
  m += 2;

  if (tmp.opcode==1) { // data
    strcpy(tmp.data,m);
  }else if (tmp.opcode==2) { // error/control
    memcpy(&tmpint,m,2);
    tmp.errcode = ntohs(tmpint);
    m += 2;
    strcpy(tmp.errstr,m);
    if (mode) tmp.size -= cleanCRLF(tmp.errstr);
  }else {
    printf("Wrong opcode value!\n");
    tmp.opcode = -1;
  }
  return (tmp);
}

int main(int argc, char*argv[]) {

  short int recvportnum = (short int)atoi(argv[1]);
  printf ("Receiver's port num: %d\n", recvportnum);

  int ld;
  struct sockaddr_in skaddr, remote;
  int m=0, length, len;
  struct message msg_out;
  int tmode=0;
  char bufout[MAXBUF];

  /* create a socket 
     IP protocol family (PF_INET) 
     UDP protocol (SOCK_DGRAM) 
  */
  if ((ld = socket(PF_INET, SOCK_DGRAM, 0)) < 0) {
    printf("Problem creating socket\n");
    exit(1);
  }
  
  /* establish our address 
     address family is AF_INET
  */
  skaddr.sin_family = AF_INET;
  skaddr.sin_addr.s_addr = inet_addr("192.168.1.76");
  skaddr.sin_port = htons(17566);
  if (bind(ld, (struct sockaddr *) &skaddr, sizeof(skaddr))<0) {
    printf("Problem binding\n");
    exit(0);
  }
  
  /* find out what port we were assigned and print it out */
  length = sizeof( skaddr );
  if (getsockname(ld, (struct sockaddr *) &skaddr, &length)<0) {
    printf("Error getsockname\n");
    exit(0);
  }
  
  /* port numbers are network byte order, we have to convert to
     host byte order before printing !*/
  printf("%d\n",ntohs(skaddr.sin_port));

  /* need to know how big address struct is, len must be set before the
     call to sendto!!! */
  len = sizeof(struct sockaddr_in);

  remote.sin_family = AF_INET;
  remote.sin_addr.s_addr = inet_addr("134.197.43.11");
  remote.sin_port = htons(recvportnum);

  /* Send a sample error/control message */
  msg_out.opcode = 2;
  msg_out.errcode = 4;
  //  strcpy(msg_out.data,"Hello from the other side!");
  strcpy(msg_out.errstr,"Just saying hi!");
  msg_out.size = 4+strlen(msg_out.errstr)+1;
  buildmsg(bufout,msg_out,tmode);
  sendto(ld,bufout,msg_out.size,0,(struct sockaddr *)&remote,len);

  /* Send a sample data message */
  msg_out.opcode = 1;
  char *tmp = msg_out.data;
  *tmp = '7';
  tmp++; m++;
  *tmp = '0';
  tmp++; m++;
  *tmp = '1';
  tmp++; m++;
  *tmp = '0';
  tmp++; m++;
  *tmp = '2';
  tmp++; m++;
  *tmp = '\0';
  //  strcpy(msg_out.data,"Hello from the other side!");
  msg_out.size = 4+m+1;
  buildmsg(bufout,msg_out,tmode);
  sendto(ld,bufout,msg_out.size,0,(struct sockaddr *)&remote,len);
  
  return(0);
}

