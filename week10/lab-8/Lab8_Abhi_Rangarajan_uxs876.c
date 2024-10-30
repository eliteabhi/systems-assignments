#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>

int main( int argc, int *argv ) {

  pid_t pid = fork();

  if ( pid == 0 )
    printf("[PID %d] Child process. Parent PID = %d.\n", ( int ) getpid(), ( int ) getppid() );
  
  else
    printf("[PID %d] Parent process. Child PID = %d.\n", ( int ) getpid(), ( int ) pid );

}

