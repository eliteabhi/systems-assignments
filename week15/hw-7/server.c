
#include <netinet/in.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <unistd.h>
#include <arpa/inet.h>

#define BIND_PORT 65433
#define BIND_ADDRESS "127.0.0.1"
#define MAX_REQUESTS 3
#define BUFFER_SIZE 1024

typedef struct transaction {

    char* msg;
    char* response;

} transaction;

transaction handle_client( int client_socket ) {

    char msg[ BUFFER_SIZE ] = "";
    ssize_t bytes_read = 0;
    char* response = "";

    while ( bytes_read == 0 ) bytes_read = read( client_socket, msg, BUFFER_SIZE );

    printf( "\nMsg recieved from client: %s\n", msg );
    printf( "Responding with: " );

    if ( strcmp( msg, "hello") == 0 ) response = "world";
    
    else if ( strcmp( msg, "exit") == 0 ) response = "exit";

    printf( "%s\n", response );

    send( client_socket, response, strlen( response ), 0 );

    return ( transaction ) { .msg = msg, .response = response };

}

int main( int argc, char const* argv[] ) {
    
    struct sockaddr_in address;
    socklen_t addrlen = sizeof( address );
    char buffer[ BUFFER_SIZE ] = { 0 };
    char* response = "";

    int server_socket = socket( AF_INET, SOCK_STREAM, 0 );
    
    if ( server_socket < 0 ) {
        perror( "socket failed" );
        exit( 1 );
    }

    address.sin_family = AF_INET;
    address.sin_port = htons( BIND_PORT );

    if ( inet_pton( AF_INET, BIND_ADDRESS, &address.sin_addr ) <= 0 ) {

        printf( "\nInvalid address/ Address not supported\n" );
        exit( 1 );

    }

    if ( bind( server_socket, ( struct sockaddr* ) &address, addrlen ) < 0 ) {

        perror( "bind failed" );
        exit( 1 );
    
    }

    if ( listen( server_socket, MAX_REQUESTS ) < 0 ) {
        
        perror( "listening failed" );
        exit( 1 );
    
    }

    int client_socket = accept( server_socket, ( struct sockaddr* ) &address, &addrlen );
    if ( client_socket < 0 ) {

        perror( "Couldnt connect to client" );
        exit( 1 );
    
    }

    char* msg = "";

    while ( strcmp( msg, "exit") != 0 ) msg = handle_client( client_socket ).msg;

    printf( "closing connection" );
    
    close( client_socket );
    close( server_socket );

    return 0;

}