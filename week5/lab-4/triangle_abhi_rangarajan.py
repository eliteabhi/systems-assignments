from math import sqrt, atan, degrees
from typing import Tuple

class Triangle:

    def __init__( self, base: float, height: float) -> None:
       
        if base <= 0:
            base = 1
        if height <= 0:
            height = 2

        self.__base: float = base
        self.__height: float = height
        self.side: float = 0.0
        self.perimeter: float = 0.0
        self.area: float = 0.0
        self.alpha: float = 0.0
        self.beta: float = 0.0

    def __str__( self ) -> str:
        return f'''------------------------------
base: { self.__base }
height : { self.__height }
side : { self.side }
perimeter: { self.perimeter }
area : { self.area }
alpha : { self.alpha }
beta : { self.beta }
------------------------------
    '''
    def __repr__( self ) -> str:
        return self.__str__()

    def print_all( self ) -> None:
        print( self.__str__() )
    
    def set_base( self, base: float ) -> None:
        if base <= 0:
            print( 'Invalid base length' )
            
        self.__base = base

    def set_height( self, height ) -> None:
        if height <= 0:
            print( 'Invalid height length' )

        self.__height = height

    def calc_side( self ) -> float:
        if self.side > 0:
            return self.side

        self.side = sqrt( ( ( self.__base * 0.5 ) * ( self.__base * 0.5 ) ) + ( self.__height * self.__height ) )
        return self.side

    def calc_perimeter( self ) -> float:
        if self.perimeter > 0:
            return self.perimeter

        if self.side == 0:
            self.calc_side()

        self.perimeter = self.side * 2 + self.__base 
        return self.perimeter

    def calc_area( self ) -> float:
        if self.area > 0:
            return self.area

        self.area = self.__base * self.__height * 0.5
        return self.area

    def calc_alpha( self ) -> float:
        if self.alpha > 0:
            return self.alpha

        self.alpha = degrees( atan( self.__height / ( self.__base * 0.5 ) ) )
        return self.alpha

    def calc_beta( self ) -> float:
        if self.beta > 0:
            return self.beta

        if self.alpha == 0:
            self.calc_alpha()

        self.beta = 90 - self.alpha
        return self.beta

    def calc_all( self ) -> Tuple[ float, float, float, float, float ]:
        self.calc_perimeter()
        self.calc_area()
        self.calc_beta()

        return ( self.side, self.perimeter, self.area, self.alpha, self.beta )
