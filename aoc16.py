
input = []

with open('input_16.txt') as f:
    for line in f.readlines():
        input.append([c for c in line.strip()])

class grid2:
    def __init__(self, grid):
        self.grid = grid
        self.width = len(grid[0])
        self.height = len(grid)
    
    def __getitem__(self, vec):
        return self.grid[vec.y][vec.x]
    
    def __setitem__(self, vec, value):
        self.grid[vec.y][vec.x] = value
    
    def print(self):
        for line in self.grid:
            print("".join(line))

    def in_bounds(self, vec):
        return vec.x >= 0 and vec.y >= 0 and vec.x < self.width and vec.y < self.height
    
    def __iter__(self):
        return self.grid.__iter__()
 
class vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        # Ensure that the hash is computed based on the content of the object
        return hash((self.x, self.y))

    def __add__(self, other):
        return vec2(self.x + other.x, self.y + other.y)

    def __eq__(self, __value: object) -> bool:
        return self.x == __value.x and self.y == __value.y
    
    def __sub__(self, other):
        return vec2(self.x - other.x, self.y - other.y)
    
    def get(self, grid):
        return grid[self.y][self.x]
    
    def set(self, grid, value):
        grid[self.y][self.x] = value

grid = grid2(input)

def calculate_energetization(paths):
    mark = set()
    trace = set()
    while paths:
        new_paths = []
        for (p, d) in paths:
            newp = p + d
            if grid.in_bounds(newp) == False:
                continue 
            
            if (newp, d) in mark:
                continue
            mark.add((newp, d))

            trace.add(newp)

            sym = grid[newp]
            
            if sym == "/" :
                new_paths.append((newp, vec2(-d.y, -d.x)))
                continue
            if sym == "\\":
                new_paths.append((newp, vec2(d.y, d.x)))
                continue
            if sym == "|":
                if abs(d.x) != 0:
                    new_paths.append((newp, vec2(0, -1)))
                    new_paths.append((newp, vec2(0, 1)))
                    continue
            if sym == "-":
                if abs(d.y) != 0:
                    new_paths.append((newp, vec2(1, 0)))
                    new_paths.append((newp, vec2(-1, 0)))
                    continue 
            new_paths.append((newp, vec2(d.x, d.y)))
        paths = new_paths
    return len(trace)



print("part 1")
print(calculate_energetization([(vec2(-1,0), vec2(1,0))]))

print("part 2")
maxlen = 0 
for x in range(grid.width):
    maxlen = max(maxlen, calculate_energetization([(vec2(x,-1), vec2(0,1))]))
    maxlen = max(maxlen, calculate_energetization([(vec2(x,grid.height), vec2(0,-1))]))

for y in range(grid.height):
    maxlen = max(maxlen, calculate_energetization([(vec2(-1,y), vec2(1,0))]))
    maxlen = max(maxlen, calculate_energetization([(vec2(grid.width,y), vec2(-1,0))]))

print(maxlen)





exit()
# did not work - too many recursions

trace = grid2([[vec2(0,0) for x in line] for line in grid])
mark = set()

def recursive_step(p, d):
    newp = p + d
    if grid.in_bounds(newp) == False:
        return 
    
    if (newp, d) in mark:
        return
    
    mark.add((newp, d))

    trace[newp] = d

    sym = grid[newp]
    
    if sym == "/" :
        recursive_step(newp, vec2(-d.y, -d.x))
        return
    if sym == "\\":
        recursive_step(newp, vec2(d.y, d.x))
        return
    if sym == "|":
        if abs(d.x) != 0:
            recursive_step(newp, vec2(0, -1))
            recursive_step(newp, vec2(0, 1))
            return
    if sym == "-":
        if abs(d.y) != 0:
            recursive_step(newp, vec2(1, 0))
            recursive_step(newp, vec2(-1, 0))
            return 
    
    recursive_step(newp, vec2(d.x, d.y))

recursive_step(vec2(-1,0), vec2(1,0))







