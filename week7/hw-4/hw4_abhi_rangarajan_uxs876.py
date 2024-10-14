
import sys
import os

from pwd import getpwuid
from grp import getgrgid
from typing import List, Generator

def lines_from_file_generator( filepath: str ) -> Generator[ str, None, None ]:
    for row in open( file=filepath, mode='r', encoding='utf-8' ):
        yield row.strip()

def details( ext: str, dirpath: str ) -> str:

    details_of_files: List[ str ]= []

    for file in os.listdir( dirpath ):
        if ext not in file:
            continue

        file_stat = os.stat( f'{ dirpath }/{ file }' )
        mode: int = file_stat.st_mode
        owner: str = getpwuid( file_stat.st_uid ).pw_name
        group: str = getgrgid( file_stat.st_gid ).gr_name

        details_of_files.append( f'File: { file }\nPermissions: { mode }\nOwner: { owner }\nGroup: { group }' )

    return '\n\n'.join( details_of_files )


def search( keyword: str, ext: str, dirpath: str ) -> str:

    files_with_keyword: List[ str ] = []

    for file in os.listdir( dirpath ):
        if ext not in file:
            continue

        # Use generator to find keyword in file ( I just wanted an excuse to use a generator lol )
        for line in lines_from_file_generator( f'{ dirpath }/{ file }' ):
            if keyword in line:
                files_with_keyword.append( file )
                break

    if not files_with_keyword:
        return f"No files containing keyword '{ keyword }'"

    return f"Files containing keyword '{ keyword }': { ', '.join( files_with_keyword ) }"

if __name__ == '__main__':

    usage: str = f'Usage: python { sys.argv[0] } <command> <extension> <dirpath> [keyword]'

    if len( sys.argv ) < 4 or len( sys.argv ) > 5:
        print( usage )
        sys.exit(1)

    command: str = sys.argv[ 1 ]
    extension: str = sys.argv[ 2 ]
    path: str = sys.argv[ 3 ]

    if not os.path.isdir( path ):
        print( f"Error: { path } is not a directory/does not exist" )
        sys.exit(1)

    if command == "details":

        if len( sys.argv ) != 4:
            print( usage )
            sys.exit(1)

        print( details( extension, path ) )

    elif command == "search":

        if len( sys.argv ) != 5:
            print( usage )
            sys.exit(1)

        name: str = sys.argv[ 4 ]

        print( search( name, extension, path ) )

    else:
        print(f"Invalid command: { command }\n")
        print( usage )

    sys.exit(0)
