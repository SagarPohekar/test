from Point import Point
import math

class Line(object):

    def __init__(self, start = Point(0,0), end = Point(10,0)):
        self.m_start_point = start
        self.m_end_point = end

    def __repr__(self):
        return "Line with\nstart point : (%s),\nend point : (%s)" % (str(self.m_start_point) , str(self.m_end_point))

    def length(self):
        return math.sqrt(( self.m_start_point.x - self.m_end_point.x ) * ( self.m_start_point.x - self.m_end_point.x ) \
        + ( self.m_start_point.y - self.m_end_point.y ) * ( self.m_start_point.y - self.m_end_point.y ) )
    
