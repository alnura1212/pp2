def solve(numheads, numlegs):
    r=int((numlegs-numheads*2)/2)
    c=int(numheads-r)
    print("rabbits=", r)
    print("chickens=", c)
solve(35, 94)