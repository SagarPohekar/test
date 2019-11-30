class Point(object):
    def __init__(self, x = 0.0, y = 0.0):
        self.m_x = x
        self.m_y = y

    @property
    def x(self):
        return self.m_x
    
    @x.setter
    def x(self, x_):
        self.m_x = x_

    @property
    def y(self):
        return self.m_y
    
    @x.setter
    def x(self, y_):
        self.m_y = y_

    def __repr__(self):
        return "x : %s, y: %s" % (str(self.m_x), str(self.m_y))

