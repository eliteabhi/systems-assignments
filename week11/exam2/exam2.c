#include <stdio.h>
#include <stdlib.h>
#include <unistd.h> 
#include <string.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <sys/wait.h>
#include <fcntl.h>
#include <errno.h>

#define PID_MAX_PATH "/proc/sys/kernel/pid_max"
#define BUFFER_SIZE 16

int read_file( const char* filepath, const int buffer_size, char* buffer ) {

    printf( "Reading from file: %s...\n", filepath );

    int fd = open( filepath, O_RDONLY | O_CREAT );

    if ( fd == -1 ) {

        printf( "Error opening file for read\n" );
        exit( 1 );

    }

    const int bytes_read = read( fd, buffer, buffer_size - 1 );
    buffer[ bytes_read ] = '\0';

    printf( "Read %d bytes from file...\n", bytes_read );

    printf( "Closing file...\n\n" );

    if ( close( fd ) == -1 ) {

        printf( "Error closing file after read\n" );
        exit( 1 );

    }

    return bytes_read;

}

int write_file( const char* filepath, const char* content, const int content_size ) {

    int fd = open( filepath, O_WRONLY | O_TRUNC );

    if ( fd == -1 ) {

        printf( "\nError opening pid file for write\n" );
        exit( 1 );

    }

    printf( "\nWriting %d bytes to file: %s...\n", sizeof( content ), filepath );
    const int bytes_written = write( fd, content, content_size );

    if ( close( fd ) == -1 ) {

        printf( "\nError closing file after write\n" );
        exit( 1 );

    }

    return bytes_written;

}

int main( int argc, char **argv ) {

    if ( argc != 2 ) {
    
        printf( "Usage: exam2.c <max_pid>\n" );
        exit( 1 );
    
    }

    const char *new_max_pid = argv[1];

    pid_t process = fork();

    if ( process < 0 ) {

        printf( "Failed to create child process\n" );
        exit( 1 );

    }

    if ( process == 0 ) {

        char buffer[ BUFFER_SIZE ];
        read_file( PID_MAX_PATH, BUFFER_SIZE, buffer );

        printf( "Current max_pid: %s", buffer );
        printf( "New max_pid: %s\n", new_max_pid );

        write_file( PID_MAX_PATH, new_max_pid, strlen( new_max_pid ) );
    
    } else {

        wait( NULL );
        printf( "\nChild process finished\n" );

        printf( "\nChecking pid file...\n\n" );
        
        char buffer[ BUFFER_SIZE ];
        read_file( PID_MAX_PATH, BUFFER_SIZE, buffer );

        printf( "Current max_pid: %s\n", buffer );
        
        if ( atoi( buffer ) == atoi( new_max_pid ) ) {
            printf( "PID_MAX Updated Correctly!\n" );
            exit( 0 );
        }

        else {

            printf( "PID_MAX failed to update\n" );
            exit( 1 );

        }

    }

}
