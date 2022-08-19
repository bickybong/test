class Square:
    def __init__(self, side) -> None:
        self.side = side

    def __add__(one, two):
        return(4*(one.side + two.side))
        """ Overload add operator """
    
    def __pow__(one, two):
        return(one.side**two.side)

one = Square(2)
two = Square(4)

print(f"Sum of both squares {one ** two}")