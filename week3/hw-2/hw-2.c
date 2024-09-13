// Abhi Rangarajan uxs876
#include <stdio.h>
#include <stdlib.h> // For exit()

int main( int argc, char **argv ) {

    FILE *from_ptr, *to1_ptr, *to2_ptr;
    char *from, *to1, *to2;
    int c;

    if ( argc < 4 ) {

        printf( "Usage: multiple_copies source_file destination_file1 destination_file2\n" );
        exit(1);

    }

    from = argv[1];
    to1 = argv[2];
    to2 = argv[3];

    // Open one file for reading
    from_ptr = fopen( from, "r" );
    if ( from_ptr == NULL )
    {
        printf( "Opening Error!: %s\n", from );
        exit(1);
    }

    // Open another file for writing
    to1_ptr = fopen( to1, "w" );
    if ( to1_ptr == NULL )
    {
        printf( "Opening Error!: %s\n", to1 );
        exit(1);
    }
    
    // Open another file for writing
    to2_ptr = fopen( to2, "w" );
    if ( to2_ptr == NULL )
    {
        printf( "Opening Error!: %s\n", to2 );
        exit(1);
    }

    // Read contents from file
    while ( ( c = fgetc( from_ptr ) ) != EOF )
    {
        fputc( c, to1_ptr );
        fputc( c, to2_ptr );
    }

    fclose( from_ptr );
    fclose( to1_ptr );
    fclose( to2_ptr );
    return 0;

}
