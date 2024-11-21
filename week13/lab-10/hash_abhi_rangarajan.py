import sys
import hashlib as h
from typing import List

def hash_file( filepath: str, hash_function: str, chunk_size: int = 4096 ) -> str:
    try:

        hash_object: h._Hash = h.new( hash_function )

        with open( filepath, 'rb' ) as f:
            for chunk in iter( lambda: f.read( chunk_size ), b'' ):
                hash_object.update( chunk )

    except IOError:
        print( 'Input file not found' )
        sys.exit( 1 )

    return hash_object.hexdigest()

def main( argc: int, argv: List[ str ] ) -> None:

    hash_function: str = 'sha256'

    if argc < 2 or argc > 3:
        print( 'Usage: python hash_abhi_rangarajan.py <input file> [hash_function]\n' )
        print( f'Available Hash Functions: { h.algorithms_available }\nDefault: sha256\n' )
        
        sys.exit( 1 )

    elif argc == 2:
        print( 'No hash function provided, defaulting to SHA256...\n' )

    elif argv[ 2 ] in h.algorithms_available:
        hash_function = argv[ 2 ].lower()

    else:
        print( 'Hash function invalid, defaulting to SHA256...\n' )

    input_file: str = sys.argv[ 1 ]

    hashed_file_str: str = hash_file( input_file, hash_function )

    print( f"Hashed file '{ input_file }' with '{ hash_function }' to:\n{ hashed_file_str }\n" )

    print( "Writing to 'output.txt' file..." )

    with open( r'./output.txt', 'w+' ) as f:
        f.write( hashed_file_str )

if __name__ == '__main__':
    main( len( sys.argv ) , sys.argv )