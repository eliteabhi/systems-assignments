/*
* Abhi Rangarajan
* uxs876
*/

#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

int main(int argc, char *argv[])
{
  // Step 1
  // Pass in your student id via command line argument.
  // Set environment variable USER_ID to your student ID.
  // Print USER_ID
  
  if ( argc < 2 ) {
      
    printf( "No User ID provided" );
    exit(1);
    
  }

  const char* USER_ID = argv[1];
  const int user_id_env_result = setenv( "USER_ID", USER_ID, 1 );
  printf( "User ID is: %s\n", getenv( "USER_ID" ) );

  // Step 2
  // Set environment variable ASSIGNMENT3 to "Environment Variables and Process IDs"
  // Print ASSIGNMENT3

  const char ASSIGNMENT3[] = "Environment Variables and Process IDs";

  const int assignment3_env_result = setenv( "ASSIGNMENT3", ASSIGNMENT3, 1 );
  printf( "Assignment 3 is: %s\n", getenv( "ASSIGNMENT3" ) );

  // Step 3
  // Write code to get your process's ID (PID)
  // Example code to convert int to char[]
  // char pid_str[8] = {0};
  // sprintf(pid_str, "%d", <variable used for getpid>);

  const int PID = getpid();
  char pid_str[8] = {0};
  sprintf( pid_str, "%d", PID );
  printf( "My proccess id is: %s\n", pid_str );

  // Step 4
  // Set environment variable MY_PID to the PID found above
  // Print the PID

  const int my_pid_env_result = setenv( "MY_PID", pid_str, 1 );
  printf( "MY_PID is: %d\n", getenv( "MY_PID" ) );

  // Step 5
  // An environment variable named "COURSE_NAME" is available
  // Print the value
  // Change it to the correct course name (EE3233 Systems Programming)
  // Print it again
  
  printf( "Course Name is %s\n", getenv( "COURSE_NAME" ) );
  const char correct_course_name[] = "EE3233 Systems Programming";
  const int course_name_env_result = setenv( "COURSE_NAME", correct_course_name, 1 );
  printf( "Course Name is %s\n", getenv( "COURSE_NAME" ) );
  
  return 0;
}
