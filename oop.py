class  Coordinate(object):
    #initialize atributes:
    def __init__(self, a, b):
        self.x = a
        self.y = b
    #define method:
    #euclidean distance
    def distance(self, second):
        x_diff_sq = (self.x - second.x)**2
        y_diff_sq = (self.y - second.y)**2
        return (x_diff_sq + y_diff_sq)**0.5
 
        
c = Coordinate(3, 4)
z = Coordinate(6, 8)
print(c.x, c.y)
print(z.x, z.y)
print(c.distance(z))