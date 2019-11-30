from Point import Point
from Line import Line
from Circle import Circle
import math
if __name__ == "__main__":
    P1 = Point(0,0)
    P2 = Point(10,15)
    print(P1)
    print(P2)

    L1 = Line(P1, P2)
    print(L1)

    C1 = Circle(P1, round(L1.length(), 2))
    print(C1)

