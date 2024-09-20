// Abhi Rangarajan uxs876
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main( int argc, char **argv ) {

    if ( argc < 4 ) {

        printf( "Usage: multiple_copies source_file destination_file1 destination_file2\n" );
        exit(1);

    }

    int from = open( argv[1], O_RDONLY );
    int to1 = open( argv[2], O_WRONLY | O_CREAT );
    int to2 = open( argv[3], O_WRONLY | O_CREAT );

    if ( from == -1 ) printf( "Opening Error!: %s\n", argv[1] );

    char buf[100] = { 0 };

    int bytes_read = read( from, buf, sizeof( buf ) - 1 );

    write( to1, buf, bytes_read );
    write( to2, buf, bytes_read );

    close( from );

    return 0;

}
