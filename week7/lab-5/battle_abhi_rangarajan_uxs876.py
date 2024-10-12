from typing import List
import heapq as hq

def battle( monsters: List[ int ] ) -> None:

    # Dirty way to convert to a Max heap
    monsters = list( map( lambda x: x * -1, monsters ) )

    hq.heapify( monsters )

    print( monsters )

    while len( monsters ) > 1:
        monster1: int = monsters[0]
        monster2: int = monsters[1]

        if monster1 == monster2:
            hq.heappop( monsters )
            hq.heappop( monsters )
            continue

        push_item: int = monster1 - monster2

        hq.heappushpop( monsters, push_item )

    if monsters:
        print('I have won, but at what cost?')

    else:
        print('Nobody won!')


# Test the function

Test1 = [ 4, 4, 1 ]
Test2 = [ 1, 1, 1, 1, 1, 1 ]
Test3 = [ 9, 8, 7, 6 ]
Test4 = [ 12, 10, 9, 9, 8, 9 ]


battle( Test1 )
battle( Test2 )
battle( Test3 )
battle( Test4 )

