import pdb

def transform(x, y):
    y = y**2
    x *= 2
    z = x + y
    return z


x = 50
y = 60
z = 5
n = 1000

pdb.set_trace()

z = transform(5, 10)
print("z = {}".format(z))

n = transform(2, 3)
print("n = {}".format(n))