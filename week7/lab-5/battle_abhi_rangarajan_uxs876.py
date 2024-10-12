from typing import List

def battle( monsters: List[ int ] ) -> None:

    while len( monsters ) > 1:
        monster1: int = monsters[0]
        monster2: int = monsters[1]

        if monster1 > monster2:
            monsters[0] -= monster2
            monsters.pop( 1 )

        elif monster2 > monster1:
            monsters[1] -= monster1
            monsters.pop( 0 )

        else:
            monsters.pop( 0 )
            monsters.pop( 0 )

    if monsters:
        print('I have won, but at what cost?')

    else:
        print('Nobody won!')


# Test the function

Test1 = [ 4, 4, 1 ]
Test2 = [ 1, 1, 1, 1, 1, 1 ]
Test3 = [ 9, 8, 7, 6 ]

battle( Test1 )
battle( Test2 )
battle( Test3 )
