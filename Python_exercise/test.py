class Calc(object):
    def __init__(self, x, y, z):
        self.i = x
        self.j = y
        self.k = z
def calculate(x):
    i = x - 1
    j = x * 2
    k = i % 3
    return Calc( i, j, k )

number = int( 5 )

lcp = calculate( number )
print( lcp.i + lcp.j + lcp.k )
