#define _GNU_SOURCE // For intellisense errors

#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <signal.h>
#include <string.h>

void child_SIGUSR1_handler() {

    printf( "Process ID: %d\n", getpid() );
    printf( "Parent Process ID: %d\n", getppid() );

}

int main( int argc, char **argv ) {


    sigset_t set;
    sigemptyset( &set );
    sigaddset( &set, SIGUSR1 );

    if ( sigprocmask( SIG_BLOCK, &set, NULL ) == -1 ) {

        perror( "sigprocmask" );
        exit( 1 );

    }

    struct sigaction sa;
    sa.sa_handler = child_SIGUSR1_handler;
    sigemptyset( &sa.sa_mask );
    sa.sa_flags = 0;

    if ( sigaction( SIGUSR1, &sa, NULL ) == -1 ) {

        perror( "sigaction" );
        exit( 1 );

    }

    pid_t pid = fork();

    if ( pid < 0 ) {

        perror( "fork" );
        exit( 1 );

    }

    // Parent process
    if ( pid > 0 ) {

        sigemptyset( &set );
        sigprocmask( SIG_SETMASK, &set, NULL );

        sleep( 5 ); // Wait for 5 seconds

        kill( pid, SIGUSR1 );

    // Child process
    } else {

        sigemptyset( &set );
        sigprocmask( SIG_SETMASK, &set, NULL );

        pause();
        
    }

}
