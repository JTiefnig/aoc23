
class vec3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    # Overload operators
    def __add__(self, other):
        return vec3(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other):
        return vec3(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __mul__(self, other):
        return vec3(self.x * other, self.y * other, self.z * other)
    
    def __truediv__(self, other):
        return vec3(self.x / other, self.y / other, self.z / other)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z
    
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"
    
    def __repr__(self):
        return str(self)

stones = []

bounds = (200000000000000, 400000000000000, 200000000000000, 400000000000000) #(7, 27, 7, 27)

with open("input_24.txt") as f:
    for line in f.readlines():
        (sp, sv)  = line.strip().split(" @ ")

        pos_arr = [float(x) for x in sp.split(",")]
        pos = vec3(pos_arr[0], pos_arr[1], pos_arr[2])
        vel_arr = [float(x) for x in sv.split(",")]
        vel = vec3(vel_arr[0], vel_arr[1], vel_arr[2])

        stones.append((pos, vel))


# solve linear equation for x, y to get intersection point 

# x = x0 + t * vx where t has to be positive
# y = y0 + t * vy

def intersect(s1, s2):
    # solve for t
    # x0 + t * vx = x0' + ts * vx'
    # y0 + t * vy = y0' + ts * vy'
    # t = ((x2 - x1) * dy2 - (y2 - y1) * dx2) / (dx1 * dy2 - dx2 * dy1)

    # check for parallel lines
    if s1[1].x * s2[1].y == s2[1].x * s1[1].y:
        print ("parallel lines{} {}".format(s1, s2)) # check if they are the same line
        if (s1[0].x - s2[0].x) / s2[1].x == (s1[0].y - s2[0].y) / s2[1].y:
            print("same line ")
            return (s1[0].x, s1[0].y) # this could result in a problem when checking for within bounds
        return None

    t = ((s2[0].x - s1[0].x) * s2[1].y - (s2[0].y - s1[0].y) * s2[1].x) / (s1[1].x * s2[1].y - s2[1].x * s1[1].y)

    t2 = ((s2[0].x - s1[0].x) * s1[1].y - (s2[0].y - s1[0].y) * s1[1].x) / (s1[1].x * s2[1].y - s2[1].x * s1[1].y)
    # check if t is positive
    if t < 0 or t2 < 0:
        #print("t: {}, t2: {}".format(t, t2))
        return None
    
    #print("t: {}, t2: {}".format(t, t2))
    if t < 0 or t2 < 0:
        return None

    # calculate intersection point
    x = s1[0].x + t * s1[1].x
    y = s1[0].y + t * s1[1].y

    return (x, y)

sum = 0
for i, s1 in enumerate(stones):
    for j, s2 in enumerate(stones):
        if i == j:
            break # don't compare to self and don't compare twice
        #print("comparing {} and {}".format(i, j))
        ip = intersect(s1, s2)
        if ip == None:  
            continue
        (ix, iy) = ip
        if ix >= bounds[0] and ix <= bounds[1] and iy >= bounds[2] and iy <= bounds[3]:
            #print("intersection at ({}, {})".format(ix, iy))
            sum += 1

print("Result1: {}".format(sum)) 


# part 2

# assumption: stone has to hit storm directly, hitpoint is int 

# approach solve for one axis at a time

# p = p0 + t * dp where t > 0
# for all axis and solve for t

# ti = (x0 - xi) / (dxi - dx0)
# ti = (y0 - yi) / (dyi - dy0)
# ti = (z0 - zi) / (dzi - dz0)

# Ax = b
# where x is x, y, z, dx, dy, dz
# Three equations per stone and 6 unknowns -> 2 only stones needed

# overdetermined system of equations -> approach least squares