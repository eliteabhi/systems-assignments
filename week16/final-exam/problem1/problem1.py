import sys
import os
import shutil
from typing import List

def main( argc: int, argv: List[ str ] ) -> None:

    if argc not in { 3, 4 }:
        print( "\nUsage: python python_script.py <input_file> <output_file> [append string]\n" )
        return

    input_file: str = argv[1]
    output_file: str = argv[2]
    append_string: str = argv[3] or None

    if not os.path.exists( input_file ):
        print( f"\nError: Input file '{ input_file }' does not exist.\n" )

    with open( input_file, 'r', encoding='utf-8' ) as in_f:
        with open( output_file, 'w', encoding='utf-8' ) as out_f:
            for line in in_f:
                out_f.write( line )
                out_f.flush()

    if append_string:
        if "out" in output_file or os.stat( output_file ).st_size / ( 1024 * 1024 ) > 1: # bytes -> mega = bytes / ( 1024 ^ 2 )
            shutil.copy( output_file, f"{ output_file }.bkp" )

        with open( output_file, 'a', encoding='utf-8' ) as out_f:
            out_f.write( append_string )

    with open( output_file, 'r', encoding='utf-8' ) as out_f:
        print( out_f.read() )

if __name__ == "__main__":
    main( len( sys.argv ), sys.argv )
