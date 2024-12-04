// Client side C program to demonstrate Socket
// programming
#include <arpa/inet.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <unistd.h>
#include <arpa/inet.h>

#define SERVER_PORT 65433
#define SERVER_ADDRESS "127.0.0.1"
#define BUFFER_SIZE 1024

int main( int argc, char const* argv[] ) {

    struct sockaddr_in serv_addr;
    socklen_t addrlen = sizeof( serv_addr );

    int client_socket = socket( AF_INET, SOCK_STREAM, 0 );

    if ( client_socket < 0 ) {

        printf( "\nSocket creation error\n" );
        exit( 1 );
    }

    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons( SERVER_PORT );

    if ( inet_pton( AF_INET, SERVER_ADDRESS, &serv_addr.sin_addr ) <= 0 ) {
    
        printf( "\nInvalid address/ Address not supported\n" );
        exit( 1 );
    
    }
    if ( connect( client_socket, ( struct sockaddr* ) &serv_addr, addrlen ) < 0 ) {
        
        printf( "\nConnection Failed\n" );
        exit( -1 );
    
    }

    char buffer[ BUFFER_SIZE ] = { 0 };
    
    char* msg = "hello";
    printf( "\nMsg to send: hello\n" );
    send( client_socket, msg, strlen( msg ), 0 );

    read( client_socket, buffer, BUFFER_SIZE );
    printf( "Response from server: %s\n\n", buffer );

    memset( buffer, 0, BUFFER_SIZE ); // Clear the buffer

    msg = "exit";
    printf( "Msg to send: exit\n" );
    send( client_socket, msg, strlen( msg ), 0 );

    read( client_socket, buffer, BUFFER_SIZE );
    printf( "Response from server: %s\n", buffer );

    printf( "closing connection" );
    close( client_socket );

    return 0;

}
