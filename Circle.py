from Point import Point
from Line import Line

class Circle(object):
    def __init__(self, center = Point(0,0), radius = 10):
        self.m_center_point = center
        self.m_radius = radius

    def __repr__(self):
        return "Circle with center @ (%s) and radius %s" % (str(self.m_center_point), str(self.m_radius))
