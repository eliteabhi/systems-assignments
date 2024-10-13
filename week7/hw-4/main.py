
import sys

from stat import S_ISBLK, S_ISCHR, S_ISDIR, \
    S_ISDOOR, S_ISGID, S_ISLNK, S_ISREG, \
    S_ISSOCK, S_ISUID, S_ISVTX, S_IXGRP, S_IXOTH, S_IXUSR


def file_type_letter( mode: int ) -> int:
    c: str = '?'

    if S_ISREG(mode):
        c = '-'
    elif S_ISDIR(mode):
        c = 'd'
    elif S_ISBLK(mode):
        c = 'b'
    elif S_ISCHR(mode):
        c = 'c'
    elif S_ISLNK(mode):
        c = 'l'
    elif S_ISSOCK(mode):
        c = 's'
    elif S_ISDOOR(mode):
        c = 'D'

    return c


def ls_perms( mode: int ) -> str:
    rwx = [ "---", "--x", "-w-", "-wx",
           "r--", "r-x", "rw-", "rwx" ]

    bits = [0] * 10

    bits[0] = file_type_letter( mode )
    bits[1] = rwx[ ( mode >> 6 ) & 7 ]
    bits[4] = rwx[ ( mode >> 3 ) & 7 ]
    bits[7] = rwx[ ( mode & 7 ) ]

    if mode & S_ISUID:
        bits[3] = 's' if (mode & S_IXUSR) else 'S'
    if mode & S_ISGID:
        bits[6] = 's' if (mode & S_IXGRP) else 'l'
    if mode & S_ISVTX:
        bits[9] = 't' if (mode & S_IXOTH) else'T'

    bits = [i for i in bits if i != 0]
    return ''.join(bits)


def details( ext: str, dir: str ) -> str:
    pass


def search( file_name: str, ext: str, dir: str ) -> str:
    pass

if __name__ == '__main__':

    if len( sys.argv ) < 4 or len( sys.argv ) > 5:
        print( f"Usage: { sys.argv[0] } <command> [name] <extension> <dirpath>" )
        sys.exit(1)

    command: str = sys.argv[ 1 ]
    extension: str = sys.argv[ len( sys.argv ) - 2 ]
    dirpath: str = sys.argv[ len( sys.argv ) - 1 ]

    if command == "details":

        if len( sys.argv ) != 4:
            print( f"Usage: { sys.argv[0] } details <extension> <dirpath>" )
            sys.exit(1)

        print( details( extension, dirpath ) )

    elif command == "search":

        if len( sys.argv ) != 5:
            print( f"Usage: { sys.argv[0] } details <extension> <dirpath>" )
            sys.exit(1)

        name: str = sys.argv[ 2 ]

        print( search( name, extension, dirpath ) )

    else:
        print(f"Invalid command: { command }")
