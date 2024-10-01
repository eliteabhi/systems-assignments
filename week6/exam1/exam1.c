#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

#define BUFFER_SIZE 1024 // Define a constant for the buffer size

/**
 * Function: copy_file
 * -------------------
 * Copies the content from the source file to the destination file using system calls.
 *
 * Parameters:
 *    - source: The path of the source file (file to copy from).
 *    - destination: The path of the destination file (file to copy to).
 *
 * Write File Permissions: (Must use these file permissions)
 *  S_IRUSR: Owner has read permission.
 *  S_IWUSR: Owner has write permission.
 *  S_IRGRP: Group has read permission.
 *  S_IROTH: Others have read permission.
 *
 * Returns:
 *    0 on success
 *   -1 on failure (if an error occurs while opening, reading, or writing the files).
 *
 * System calls that MUST be used:
 *    - open(): Opens the source and destination files.
 *    - read(): Reads the content from the source file.
 *    - write(): Writes the content to the destination file.
 *    - close(): Closes the files after the operation.
 */
int copy_file( const char *source, const char *destination ) {

    const int from = open( source, O_RDONLY );
    const int to = open( destination, O_WRONLY | S_IRUSR | S_IWUSR | S_IRGRP | S_IROTH );
    
    if ( from == -1 || to == -1 ) {

        printf( "Opening Error!\n" );
        return -1;

    }

    char buffer[ BUFFER_SIZE ] = { 0 };

    const int bytes_read = read( from, buffer, sizeof( buffer ) - 1 );

    write( to, buffer, bytes_read );

    close( from );
    close( to );

    return 0;

}

/**
 * Function: get_env_var
 * ---------------------
 * Retrieves the value of an environment variable.
 *
 * Parameters:
 *    - var_name: The name of the environment variable to retrieve.
 *
 * Returns:
 *    - The value of the environment variable if it exists.
 *    - A message "Environment variable not found" if the variable is not found.
 *
 * This function uses the standard library function getenv() to get the value.
 */
const char *get_env_var( const char *var_name ) {

    const char* env_value = getenv( var_name );
    
    if ( env_value == NULL ) return "Environment Variable not found";

    return env_value;

}

/**
 * Function: set_env_var
 * ---------------------
 * Sets or updates the value of an environment variable.
 *
 * Parameters:
 *    - var_name: The name of the environment variable to set.
 *    - value: The value to assign to the environment variable.
 *    - overwrite: Determines whether to overwrite the variable if it already exists.
 *                 - 1 to overwrite, 0 to prevent overwriting.
 *
 * Returns:
 *    0 on success.
 *   -1 on failure (if setting the environment variable fails).
 */
int set_env_var( const char *var_name, const char *value, int overwrite ) { return setenv( var_name, value, overwrite ); }
