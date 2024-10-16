from math import sqrt

class mcomplex:
    def __init__( self, r: int, i: int ) -> None:
        """
        Initialize a mcomplex object and its data attributes
        """
        self.__set_complex_num( r, i )

    def __set_complex_num( self, r: int = 0, i: int = 0) -> None:
        """
        Update the data attributes of this mcomplex object. (Private method)
        Must include real part, imaginary part and the distance magnitude.
        """
        self.r = r
        self.i = i
        self.d = sqrt( self.r * self.r + self.i * self.i )

    def __add__( self, other ):
        """
        :return: (a + bi) + (c + di) = (a + c) + (b + d)i
        """

        return mcomplex( ( self.r + other.r ), ( self.i + other.i ) )


    def __sub__( self, other ):
        """
        Calculate and return the substraction of two mcomplex objects.
        :return: (a + bi) - (c + di) = (a - c) + (b - d)i
        """

        return mcomplex( ( self.r - other.r ), ( self.i - other.i ) )

    def __mul__( self, other ):
        """
        Calculate and return the multiplication of two mcomplex objects.
        :return: (a + bi) * (c + di) = (ac - bd) + (ad + bc)i
        """

        real: int = ( self.r * other.r ) - ( self.i * other.i )
        imaginary: int = ( self.r * other.i ) + ( self.i * other.r )

        return mcomplex( real, imaginary )

    def __truediv__( self, other ):
        """
        Calculate and return the division of two mcomplex objects.

        :return: (a + bi) / (c + di) = ((ac + bd) + (bc - ad)i) / (c^2 + d^2)
        """

        denominator = other.r * other.r + other.i * other.i
        real = ( self.r * other.r + self.i * other.i ) / denominator
        imaginary = ( self.i * other.r - self.r * other.i ) / denominator

        return mcomplex( real, imaginary )

    def __eq__( self, other ) -> bool:
        """
        Compare whether two mcomplex objects are equal.
        Return True if both mcomplex objects are the same, False otherwise.
        """

        return self.r == other.r and self.i == other.i

    def __ne__( self, other ) -> bool:
        """
        Compare whether two mcomplex objects are not equal.
        Return True if both mcomplex objects are not the same, False otherwise.
        """

        return not self.__eq__( other )

    def __lt__( self, other ) -> bool:
        """
        Calculate whether the first mcomplex number is less than the second one and return True,
        otherwise return False.
        :return: self < other ?
        """
        return self.d < other.d

    def __gt__( self, other ) -> bool:
        """
        Calculate whether the first mcomplex number is greater than the second one and return True,
        otherwise return False.
        :return: self > other ?
        """

        return self.d > other.d

    def __str__( self ) -> str:
        return f'{ self.r } + { self.i }i'

    def __repr__( self ):
        return self.__str__()

    def print( self ):
        """
        Prints the string representation of the object.
        This method outputs the object's data in a human-readable format by calling the object's `__str__` method. It is useful for displaying the object's information directly to the console.
        """

        print( self.__str__() )

def test():
    # Any test code that you would like to run

    x: mcomplex = mcomplex( 5, 6 )
    y: mcomplex = mcomplex( 2, 6 )

    print( 'x =', x )

    print( 'y =', y )

    print( 'x < y =', x < y )

    print( 'x > y =', x > y )

    print( 'x / y =', x / y )

    print( 'x * y =', x * y )

    print( 'mcomplex( 5, 0 ) < mcomplex( 4, 3 ) =', mcomplex( 5, 0 ) < mcomplex( 4, 3 ) )

    print( 'mcomplex( 5, 0 ) > mcomplex( 4, 3 ) =', mcomplex( 5, 0 ) > mcomplex( 4, 3 ) )

    print( 'x.d =', x.d )

    print( 'y.d =', y.d )

if __name__ == "__main__":
    test()
