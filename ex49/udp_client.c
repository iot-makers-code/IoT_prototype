// UDP client c code
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <netinet/in.h>
  
#define PORT 5313
#define MAXLINE 1024
  
// Driver code
int main() {
     int sockfd;
     char buffer[MAXLINE];
     char const *hello = "Hello from client" ;
     struct sockaddr_in servaddr ;
  
     // Creating socket file descriptor
     if ( (sockfd = socket(AF_INET, SOCK_DGRAM, 0)) < 0 ) {
         perror("socket creation failed");
         exit(EXIT_FAILURE);
     }

     struct timeval tv;
     tv.tv_sec = 0;
     tv.tv_usec = 1000;
     if (setsockopt(sockfd, SOL_SOCKET
             , SO_RCVTIMEO,&tv,sizeof(tv)) < 0) {
         perror("Error");
     }
  
     memset(&servaddr, 0, sizeof(servaddr));
      
     // Filling server information
     servaddr.sin_family = AF_INET ;
     servaddr.sin_port = htons(PORT);
     servaddr.sin_addr.s_addr = INADDR_ANY ;
      
     int n ;
     unsigned int len ;

     while(1) {
         sendto(sockfd,
             (const char *)hello,
             strlen(hello),
             MSG_CONFIRM,
             (const struct sockaddr *) &servaddr,
             sizeof(servaddr));
         printf("Hello message sent.\n");
        
         buffer[0] = '\0';
         n = recvfrom(sockfd,
                        (char*)buffer,
                        MAXLINE,
                        MSG_WAITALL,
                        (struct sockaddr *) &servaddr,
                        &len);
         buffer[n] = '\0';
         printf("Server [%d]: %s \n", n, buffer);
     }
    
     close(sockfd);
     return 0;
}

