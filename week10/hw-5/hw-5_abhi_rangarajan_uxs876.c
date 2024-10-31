#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <signal.h>
#include <string.h>

int pipe_fd[2];

const int BUFFER_SIZE = 256;

void parent_SIGUSR1_handler() {

    printf( "Parent received SIGUSR1!\n" );

}

void parent_SIGUSR2_handler() {

    printf( "Parent received SIGUSR2!\n" );

}

void child_SIGUSR1_handler() {

    printf( "Child received SIGUSR1!\n" );

}


void setup_signal_handlers() {

    struct sigaction sa1, sa2, sa3;

    sa1.sa_handler = parent_SIGUSR1_handler;
    sigemptyset( &sa1.sa_mask );
    sa1.sa_flags = 0;
    
    if ( sigaction( SIGUSR1, &sa1, NULL ) == -1 ) {
        perror( "sigaction" );
        exit( 1 );
    }

    sa2.sa_handler = parent_SIGUSR2_handler;
    sigemptyset( &sa2.sa_mask );
    sa2.sa_flags = 0;
    
    if ( sigaction( SIGUSR2, &sa2, NULL ) == -1 ) {
        perror( "sigaction" );
        exit( 1 );
    }

    sa3.sa_handler = child_SIGUSR1_handler;
    sigemptyset( &sa3.sa_mask );
    sa3.sa_flags = 0;
    
    if ( sigaction( SIGUSR1, &sa3, NULL ) == -1 ) {
        perror( "sigaction" );
        exit( 1 );
    }

}

int main( int argc, char **argv ) {

    if ( pipe( pipe_fd ) == -1 ) {

        perror( "pipe" );
        exit( 1 );
    
    }

    sigset_t set;
    sigemptyset( &set );
    sigaddset( &set, SIGUSR1 );
    sigaddset( &set, SIGUSR2 );
    if ( sigprocmask( SIG_BLOCK, &set, NULL ) == -1 ) {

        perror( "sigprocmask" );
        exit( 1 );
    
    }

    setup_signal_handlers();

    pid_t pid = fork();

    if ( pid < 0 ) {

        perror( "Error: Failed to fork a child process.\n" );
        exit(1);
    
    }

    if ( pid > 0 ) { 

        sigemptyset( &set );
        sigprocmask( SIG_SETMASK, &set, NULL );

        printf( "Parent started...\n" );

        sleep( 3 );

        printf( "Parent about to signal child...\n" );

        kill( pid, SIGUSR1 );

        char message[] = "Hello from Parent!\n";
        write( pipe_fd[1], message, strlen( message ) + 1 );

        pause();

        printf( "Goodbye from Parent (PID: %d)\n", getpid() );

        close( pipe_fd[1] );

    } else {

        sigemptyset( &set );
        sigprocmask( SIG_SETMASK, &set, NULL );

        pause();

        char buffer[ BUFFER_SIZE ];
        int bytes_read = read( pipe_fd[0], buffer, sizeof( buffer ) - 1 );
        buffer[ bytes_read ] = '\0';
        printf( "Message from Parent: %s", buffer );

        kill( getppid(), SIGUSR2 );

        printf( "Goodbye from Child (PID: %d)\n", getpid() );

        close( pipe_fd[0] );

    }

    exit( 0 );

}
