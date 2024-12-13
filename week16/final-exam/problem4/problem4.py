import sys
from typing import List
from threading import Thread, Lock

sum_lock: Lock = Lock()
total_sum: int = 0

def adder( n: int ) -> None:
    global total_sum

    sum_to_n: int = sum( range( 1, n + 1 ) )

    with sum_lock:
        total_sum += sum_to_n

def main( argc: int, argv: List[ str ] ) -> None:

    if argc != 2:
        print( "\nUsage: python problem4.py <n>\n" )
        return

    n: int = int( argv[1] )

    if n < 1 or n % 1 != 0:
        print( "\nError: 'n' must be a positive, non-zero integer.\n" )
        return

    threads: List[ Thread ] = [ Thread( target=adder, args=( n, ) ) for _ in range( n ) ]

    for t in threads:
        t.start()
        t.join()

    print( f'\nThreads: { n }\nThread Sum: { sum( range( 1, n + 1 ) ) }\nTotal Sum: { total_sum }')

if __name__ == "__main__":
    main( len( sys.argv ), sys.argv )
