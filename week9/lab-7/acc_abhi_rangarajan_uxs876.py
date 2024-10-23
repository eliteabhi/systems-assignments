import threading as th
from typing import List

glist: List = list( range( 500 ) )

def accumulate( i: int, acc_sum_list: List[ int ] ) -> None:
    starting_index: int = i * 100
    acc_sum_list[ i ] = sum( glist[ starting_index : starting_index + 100 ] )

    tid: int = th.get_native_id()
    print( f'Accumulated value in thread [ { tid } -> { i } ] is { acc_sum_list[ i ] }' )

def main() -> None:
    threads: List[ th.Thread ] = []
    sum_list: List[ int ] = [0] * 5

    for i in range( 5 ):
        t: th.Thread = th.Thread( target=accumulate, args=( i, sum_list ) )
        threads.append( t )
        t.start()

    for t in threads:
        t.join()

    print( f'Total is: { sum( sum_list ) }' )

if __name__ == "__main__":
    main()
