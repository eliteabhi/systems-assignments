#include <stdio.h>
#include <stdlib.h> // For exit()

int main(int argc, char** argv) {
    FILE *from_ptr, *to_ptr;
    int c;

    char* from = argv[0];

    // Open file to read
    from_ptr = fopen( from, "r" );
    if ( from_ptr == NULL ) {

        printf( "Cannot open file %s\n", from );
        exit(1);

    }

    if ( argc < 3 ) {

        printf("No file to copy to\n");
        exit(1);

    }

    for ( int i = 1; i < argc; i++ ) {

        char* to = argv[i];

        scanf("%s", to);

        // Open another file for writing
        to_ptr = fopen( to, "w" );
        if (to_ptr == NULL)
        {
            printf( "Cannot open file %s to write\n", to );
            exit(1);
        }

        // Read contents from file
        while ( ( c = fgetc(from_ptr) ) != EOF )
        {
            fputc( c, to_ptr );
        }

        fclose( to_ptr );

    }

    fclose( from_ptr );

    return 0;
}